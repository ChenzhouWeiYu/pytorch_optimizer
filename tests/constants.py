from typing import Any, Dict, List, Tuple, Union

from pytorch_optimizer import (
    LARS,
    MADGRAD,
    OPTIMIZERS,
    PNM,
    SGDP,
    SM3,
    AdaBelief,
    AdaBound,
    AdaFactor,
    Adai,
    AdamP,
    AdamS,
    Adan,
    AdaNorm,
    AdaPNM,
    AliG,
    Apollo,
    DAdaptAdaGrad,
    DAdaptAdam,
    DAdaptSGD,
    DiffGrad,
    DiffRGrad,
    Lamb,
    Lion,
    Nero,
    NovoGrad,
    RAdam,
    RaLamb,
    Ranger,
    Ranger21,
    ScalableShampoo,
    Shampoo,
)
from tests.utils import build_lookahead

ADAPTIVE_FLAGS: List[bool] = [True, False]
PULLBACK_MOMENTUM: List[str] = ['none', 'reset', 'pullback']

VALID_OPTIMIZER_NAMES: List[str] = list(OPTIMIZERS.keys())
INVALID_OPTIMIZER_NAMES: List[str] = [
    'asam',
    'sam',
    'gsam',
    'pcgrad',
    'adamd',
    'lookahead',
]

SPARSE_OPTIMIZERS: List[str] = ['madgrad', 'dadaptadagrad', 'sm3']
NO_SPARSE_OPTIMIZERS: List[str] = [
    optimizer for optimizer in VALID_OPTIMIZER_NAMES if optimizer not in SPARSE_OPTIMIZERS
]

BETA_OPTIMIZER_NAMES: List[str] = [
    'adabelief',
    'adabound',
    'adamp',
    'diffgrad',
    'diffrgrad',
    'lamb',
    'radam',
    'ranger',
    'ranger21',
    'ralamb',
    'pnm',
    'adapnm',
    'adan',
    'adai',
    'scalableshampoo',
    'dadaptadam',
    'adams',
    'adafactor',
    'novograd',
    'lion',
    'adanorm',
]

VALID_LR_SCHEDULER_NAMES: List[str] = [
    'CosineAnnealingWarmupRestarts',
    'ConstantLR',
    'CosineAnnealingLR',
    'CosineAnnealingWarmRestarts',
    'CyclicLR',
    'OneCycleLR',
]
INVALID_LR_SCHEDULER_NAMES: List[str] = ['dummy']

OPTIMIZERS: List[Tuple[Any, Dict[str, Union[float, bool, int]], int]] = [
    (build_lookahead, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'amsgrad': True}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'fixed_decay': True}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'rectify': False}, 10),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3}, 75),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'fixed_decay': True}, 75),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'weight_decouple': False}, 75),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'amsbound': True}, 75),
    (Adai, {'lr': 2e-1, 'weight_decay': 0.0}, 25),
    (Adai, {'lr': 2e-1, 'weight_decay': 0.0, 'use_gc': True}, 75),
    (Adai, {'lr': 2e-1, 'weight_decay': 0.0, 'dampening': 0.9}, 25),
    (Adai, {'lr': 2e-1, 'weight_decay': 1e-4, 'weight_decouple': False}, 25),
    (Adai, {'lr': 2e-1, 'weight_decay': 1e-4, 'weight_decouple': True}, 25),
    (Adai, {'lr': 2e-1, 'weight_decay': 1e-4, 'weight_decouple': False, 'use_stable_weight_decay': True}, 25),
    (Adai, {'lr': 2e-1, 'weight_decay': 1e-4, 'weight_decouple': True, 'use_stable_weight_decay': True}, 25),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True}, 10),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'nesterov': True}, 10),
    (DiffGrad, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (DiffRGrad, {'lr': 5e-1, 'weight_decay': 1e-3}, 50),
    (Lamb, {'lr': 1e-1, 'weight_decay': 1e-3}, 50),
    (Lamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'pre_norm': True, 'max_grad_norm': 0.0}, 50),
    (Lamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'grad_averaging': False}, 50),
    (Lamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'adam': True, 'eps': 1e-8}, 50),
    (Lamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'pre_norm': True, 'eps': 1e-8}, 100),
    (LARS, {'lr': 5e-1, 'weight_decay': 1e-3}, 50),
    (LARS, {'lr': 5e-1, 'nesterov': True}, 50),
    (RaLamb, {'lr': 1e-1, 'weight_decay': 1e-3}, 50),
    (RaLamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'pre_norm': True}, 50),
    (RaLamb, {'lr': 1e-1, 'weight_decay': 1e-3, 'degenerated_to_sgd': True}, 50),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3}, 25),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3, 'eps': 0.0}, 25),
    (MADGRAD, {'lr': 1e-2, 'weight_decay': 1e-3, 'momentum': 0.0}, 25),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3, 'decouple_decay': True}, 25),
    (RAdam, {'lr': 1e-1, 'weight_decay': 1e-3}, 50),
    (RAdam, {'lr': 1e-1, 'weight_decay': 1e-3, 'degenerated_to_sgd': True}, 50),
    (SGDP, {'lr': 5e-2, 'weight_decay': 1e-4}, 50),
    (SGDP, {'lr': 5e-2, 'weight_decay': 1e-4, 'nesterov': True}, 50),
    (Ranger, {'lr': 5e-1, 'weight_decay': 1e-3}, 150),
    (Ranger21, {'lr': 5e-1, 'weight_decay': 1e-3, 'num_iterations': 500}, 200),
    (Shampoo, {'lr': 5e-1, 'weight_decay': 1e-3, 'momentum': 0.1}, 10),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 9,
            'graft_type': 0,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 2,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-2,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 3,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 4,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 0,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 2,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'inverse_exponent_override': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'nesterov': False,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'decoupled_weight_decay': True,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-0,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'decoupled_learning_rate': False,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'moving_average_for_momentum': True,
        },
        10,
    ),
    (PNM, {'lr': 3e-1}, 50),
    (PNM, {'lr': 3e-1, 'weight_decouple': False}, 50),
    (AdaPNM, {'lr': 3e-1, 'weight_decay': 1e-3}, 50),
    (AdaPNM, {'lr': 3e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 50),
    (AdaPNM, {'lr': 3e-1, 'weight_decay': 1e-3, 'amsgrad': False}, 50),
    (Nero, {'lr': 5e-1}, 50),
    (Nero, {'lr': 5e-1, 'constraints': False}, 50),
    (Adan, {'lr': 5e-1}, 75),
    (Adan, {'lr': 5e-1, 'max_grad_norm': 1.0}, 75),
    (Adan, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True}, 100),
    (Adan, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True, 'weight_decouple': True}, 75),
    (DAdaptAdaGrad, {'lr': 2.0, 'weight_decay': 1e-3}, 100),
    (DAdaptAdaGrad, {'lr': 2.0, 'weight_decay': 1e-3, 'momentum': 0.1}, 100),
    (DAdaptAdam, {'lr': 1.0, 'weight_decay': 1e-2}, 50),
    (DAdaptAdam, {'lr': 1.0, 'weight_decay': 1e-2, 'weight_decouple': True}, 50),
    (DAdaptSGD, {'lr': 2.0, 'weight_decay': 1e-2}, 25),
    (DAdaptSGD, {'lr': 2.0, 'momentum': 0.9, 'weight_decay': 1e-3}, 25),
    (AdamS, {'lr': 1.0, 'weight_decay': 1e-3}, 25),
    (AdamS, {'lr': 1.0, 'weight_decay': 1e-3, 'amsgrad': True}, 25),
    (AdaFactor, {'lr': 5e-1, 'weight_decay': 1e-2, 'scale_parameter': False}, 100),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3, 'rebound': 'belief'}, 10),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decay_type': 'stable', 'warmup_steps': 0}, 50),
    (NovoGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'grad_averaging': True}, 50),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AliG, {'max_lr': 5e-1, 'momentum': 0.9}, 10),
    (AliG, {'max_lr': 5e-1, 'momentum': 0.9, 'adjusted_momentum': True}, 10),
    (SM3, {'lr': 5e-1, 'momentum': 0.9, 'beta': 0.9}, 10),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'fixed_decay': True}, 10),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'amsgrad': True}, 10),
]
ADAMD_SUPPORTED_OPTIMIZERS: List[Tuple[Any, Dict[str, Union[float, bool, int]], int]] = [
    (build_lookahead, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 25),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 50),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (DiffGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (DiffRGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 25),
    (RaLamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 25),
    (RAdam, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 50),
    (Ranger, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 75),
    (Ranger21, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True, 'num_iterations': 150}, 150),
    (AdaPNM, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (AdamS, {'lr': 2e1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (NovoGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'adamd_debias_term': True}, 10),
]
