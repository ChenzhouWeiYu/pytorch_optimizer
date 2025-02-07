import math
from typing import Dict, Tuple

import torch
from torch.optim.optimizer import Optimizer

from pytorch_optimizer.base.exception import NoSparseGradientError
from pytorch_optimizer.base.optimizer import BaseOptimizer
from pytorch_optimizer.base.types import CLOSURE, DEFAULTS, LOSS, PARAMETERS


class AccSGD(Optimizer, BaseOptimizer):
    r"""Accelerating Stochastic Gradient Descent For Least Squares Regression.

    :param params: PARAMETERS. iterable of parameters to optimize or dicts defining parameter groups.
    :param lr: float. learning rate.
    :param kappa: float. ratio of long to short step.
    :param xi: float. statistical advantage parameter.
    :param constant: float. any small constant under 1.
    :param weight_decay: float. weight decay.
    """

    def __init__(
        self,
        params: PARAMETERS,
        lr: float = 1e-3,
        kappa: float = 1000.0,
        xi: float = 10.0,
        constant: float = 0.7,
        weight_decay: float = 0.0,
    ):
        self.lr = lr
        self.kappa = kappa
        self.xi = xi
        self.constant = constant
        self.weight_decay = weight_decay

        self.validate_parameters()

        defaults: DEFAULTS = {
            'lr': lr,
            'kappa': kappa,
            'xi': xi,
            'constant': constant,
            'weight_decay': weight_decay,
        }
        super().__init__(params, defaults)

    def validate_parameters(self):
        self.validate_learning_rate(self.lr)
        self.validate_kappa(self.kappa)
        self.validate_xi(self.xi)
        self.validate_weight_decay(self.weight_decay)
        self.validate_constant(self.constant, boundary=1.0)

    def __str__(self) -> str:
        return 'AccSGD'

    @torch.no_grad()
    def reset(self):
        for group in self.param_groups:
            for p in group['params']:
                state = self.state[p]

                state['momentum_buffer'] = p.clone()

    @torch.no_grad()
    def step(self, closure: CLOSURE = None) -> LOSS:
        loss: LOSS = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            if 'step' in group:
                group['step'] += 1
            else:
                group['step'] = 1

            large_lr: float = group['lr'] * group['kappa'] / group['constant']
            alpha: float = 1.0 - (group['xi'] * (group['constant'] ** 2) / group['kappa'])
            beta: float = 1.0 - alpha
            zeta: float = group['constant'] / (group['constant'] + beta)

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad
                if grad.is_sparse:
                    raise NoSparseGradientError(str(self))

                state = self.state[p]

                if len(state) == 0:
                    state['momentum_buffer'] = p.clone()

                if group['weight_decay'] > 0.0:
                    grad.add_(p, alpha=group['weight_decay'])

                buf = state['momentum_buffer']
                buf.mul_((1.0 / beta) - 1.0).add_(grad, alpha=-large_lr).add_(p).mul_(beta)

                p.add_(grad, alpha=-group['lr']).mul_(zeta).add_(buf, alpha=1.0 - zeta)

        return loss


class SGDW(Optimizer, BaseOptimizer):
    r"""Decoupled Weight Decay Regularization.

    :param params: PARAMETERS. iterable of parameters to optimize or dicts defining parameter groups.
    :param lr: float. learning rate.
    :param momentum: float. momentum factor.
    :param weight_decay: float. weight decay (L2 penalty).
    :param weight_decouple: bool. the optimizer uses decoupled weight decay as in AdamW.
    :param dampening: float. dampening for momentum.
    :param nesterov: bool. enables Nesterov momentum
    """

    def __init__(
        self,
        params: PARAMETERS,
        lr: float = 1e-4,
        momentum: float = 0.0,
        weight_decay: float = 0.0,
        weight_decouple: bool = True,
        dampening: float = 0.0,
        nesterov: bool = False,
    ):
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay

        self.validate_parameters()

        defaults: DEFAULTS = {
            'lr': lr,
            'momentum': momentum,
            'weight_decay': weight_decay,
            'weight_decouple': weight_decouple,
            'dampening': dampening,
            'nesterov': nesterov,
        }

        super().__init__(params, defaults)

    def validate_parameters(self):
        self.validate_learning_rate(self.lr)
        self.validate_momentum(self.momentum)
        self.validate_weight_decay(self.weight_decay)

    def __str__(self) -> str:
        return 'SGDW'

    @torch.no_grad()
    def reset(self):
        for group in self.param_groups:
            for p in group['params']:
                state = self.state[p]

                if group['momentum'] > 0.0:
                    state['momentum_buffer'] = p.grad.clone()

    @torch.no_grad()
    def step(self, closure: CLOSURE = None) -> LOSS:
        loss: LOSS = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            momentum = group['momentum']
            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad
                if grad.is_sparse:
                    raise NoSparseGradientError(str(self))

                state = self.state[p]

                if len(state) == 0 and momentum > 0.0:
                    state['momentum_buffer'] = grad.clone()

                if momentum > 0.0:
                    buf = state['momentum_buffer']
                    buf.mul_(momentum).add_(grad, alpha=1.0 - group['dampening'])

                    if group['nesterov']:
                        grad.add_(buf, alpha=momentum)
                    else:
                        grad = buf

                if group['weight_decay'] > 0.0:
                    if group['weight_decouple']:
                        p.mul_(1.0 - group['lr'] * group['weight_decay'])
                    else:
                        grad.add_(p, alpha=group['weight_decay'])

                p.add_(grad, alpha=-group['lr'])

        return loss


class ASGD(Optimizer, BaseOptimizer):
    r"""Adaptive SGD with estimation of the local smoothness (curvature).

    :param params: PARAMETERS. iterable of parameters to optimize or dicts defining parameter groups.
    :param lr: float. learning rate.
    :param amplifier: float. amplifier.
    :param weight_decay: float. weight decay (L2 penalty).
    :param weight_decouple: bool. the optimizer uses decoupled weight decay as in AdamW.
    :param theta: float. theta.
    :param dampening: float. dampening for momentum.
    :param eps: float. term added to the denominator to improve numerical stability.
    """

    def __init__(
        self,
        params: PARAMETERS,
        lr: float = 1e-2,
        amplifier: float = 0.02,
        weight_decay: float = 0.0,
        weight_decouple: bool = True,
        theta: float = 1.0,
        dampening: float = 1.0,
        eps: float = 1e-5,
    ):
        self.lr = lr
        self.amplifier = amplifier
        self.theta = theta
        self.weight_decay = weight_decay
        self.eps = eps

        self.validate_parameters()

        defaults: DEFAULTS = {
            'lr': lr,
            'amplifier': amplifier,
            'weight_decay': weight_decay,
            'weight_decouple': weight_decouple,
            'theta': theta,
            'dampening': dampening,
            'eps': eps,
        }

        super().__init__(params, defaults)

    def validate_parameters(self):
        self.validate_learning_rate(self.lr)
        self.validate_amplifier(self.amplifier)
        self.validate_weight_decay(self.weight_decay)
        self.validate_epsilon(self.eps)

    def __str__(self) -> str:
        return 'ASGD'

    @torch.no_grad()
    def reset(self):
        for group in self.param_groups:
            for _ in group['params']:
                pass

    @staticmethod
    def get_norms_by_group(group: Dict, device: torch.device) -> Tuple[torch.Tensor, torch.Tensor]:
        r"""Get parameter & gradient norm by group."""
        p_norm = torch.zeros(1, dtype=torch.float32, device=device)
        g_norm = torch.zeros(1, dtype=torch.float32, device=device)

        for p in group['params']:
            if p.grad is None:
                continue

            p_norm.add_(p.norm().pow(2))
            g_norm.add_(p.grad.norm().pow(2))

        p_norm.sqrt_()
        g_norm.sqrt_()

        return p_norm, g_norm

    @torch.no_grad()
    def step(self, closure: CLOSURE = None) -> LOSS:
        loss: LOSS = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            if 'prev_param_norm' not in group and 'prev_grad_norm' not in group:
                group['prev_param_norm'], group['prev_grad_norm'] = self.get_norms_by_group(
                    group,
                    device=group['params'][0].device,
                )

            group['curr_param_norm'], group['curr_grad_norm'] = self.get_norms_by_group(
                group,
                device=group['params'][0].device,
            )

            param_diff_norm: float = (group['curr_param_norm'] - group['prev_param_norm']).item()
            grad_diff_norm: float = (group['curr_grad_norm'] - group['prev_grad_norm']).item()

            new_lr: float = group['lr'] * math.sqrt(1 + group['amplifier'] * group['theta'])
            if param_diff_norm > 0 and grad_diff_norm > 0:
                new_lr = min(new_lr, param_diff_norm / (group['dampening'] * grad_diff_norm)) + group['eps']

            group['theta'] = new_lr / group['lr']
            group['lr'] = new_lr

            group['prev_param_norm'].copy_(group['curr_param_norm'])
            group['prev_grad_norm'].copy_(group['curr_grad_norm'])

            for p in group['params']:
                if p.grad is None:
                    continue

                grad = p.grad
                if grad.is_sparse:
                    raise NoSparseGradientError(str(self))

                if group['weight_decay'] > 0.0:
                    if group['weight_decouple']:
                        p.mul_(1.0 - group['lr'] * group['weight_decay'])
                    else:
                        grad.add_(p, alpha=group['weight_decay'])

                p.add_(grad, alpha=-new_lr)

        return loss
