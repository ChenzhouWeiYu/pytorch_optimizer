=================
pytorch-optimizer
=================

+--------------+------------------------------------------+
| Build        | |workflow| |Documentation Status|        |
+--------------+------------------------------------------+
| Quality      | |codecov| |black| |ruff|                 |
+--------------+------------------------------------------+
| Package      | |PyPI version| |PyPI pyversions|         |
+--------------+------------------------------------------+
| Status       | |PyPi download| |PyPi month download|    |
+--------------+------------------------------------------+
| License      | |apache|                                 |
+--------------+------------------------------------------+

| **pytorch-optimizer** is optimizer & lr scheduler collections in PyTorch.
| I just re-implemented (speed & memory tweaks, plug-ins) the algorithm while based on the original paper. Also, It includes useful and practical optimization ideas.
| Currently, 43 optimizers, 6 lr schedulers are supported!
|
| Highly inspired by `pytorch-optimizer <https://github.com/jettify/pytorch-optimizer>`__.

Getting Started
---------------

For more, see the `documentation <https://pytorch-optimizers.readthedocs.io/en/latest/>`__.

Most optimizers are under MIT or Apache 2.0 license, but a few optimizers like `Fromage` have BY-NC-SA 4.0 license, which is non-commercial.
So, please double-check the license before using it at your work.

Installation
~~~~~~~~~~~~

::

    $ pip3 install -U pytorch-optimizer

If there's a version issue when installing the package, try with `--no-deps` option.

::

    $ pip3 install -U --no-deps pytorch-optimizer

Simple Usage
~~~~~~~~~~~~

::

    from pytorch_optimizer import AdamP

    model = YourModel()
    optimizer = AdamP(model.parameters())

    # or you can use optimizer loader, simply passing a name of the optimizer.

    from pytorch_optimizer import load_optimizer

    model = YourModel()
    opt = load_optimizer(optimizer='adamp')
    optimizer = opt(model.parameters())

Also, you can load the optimizer via `torch.hub`

::

    import torch

    model = YourModel()
    opt = torch.hub.load('kozistr/pytorch_optimizer', 'adamp')
    optimizer = opt(model.parameters())

If you want to build the optimizer with parameters & configs, there's `create_optimizer()` API.

::

    from pytorch_optimizer import create_optimizer

    optimizer = create_optimizer(
        model,
        'adamp',
        lr=1e-3,
        weight_decay=1e-3,
        use_gc=True,
        use_lookahead=True,
    )

Supported Optimizers
--------------------

You can check the supported optimizers & lr schedulers.

::

    from pytorch_optimizer import get_supported_optimizers, get_supported_lr_schedulers

    supported_optimizers = get_supported_optimizers()
    supported_lr_schedulers = get_supported_lr_schedulers()

+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Optimizer    | Description                                                                                     | Official Code                                                                     | Paper                                                                                         |
+==============+=================================================================================================+===================================================================================+===============================================================================================+
| AdaBelief    | *Adapting Step-sizes by the Belief in Observed Gradients*                                       | `github <https://github.com/juntang-zhuang/Adabelief-Optimizer>`__                | `https://arxiv.org/abs/2010.07468 <https://arxiv.org/abs/2010.07468>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdaBound     | *Adaptive Gradient Methods with Dynamic Bound of Learning Rate*                                 | `github <https://github.com/Luolc/AdaBound/blob/master/adabound/adabound.py>`__   | `https://openreview.net/forum?id=Bkg3g2R9FX <https://openreview.net/forum?id=Bkg3g2R9FX>`__   |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdaHessian   | *An Adaptive Second Order Optimizer for Machine Learning*                                       | `github <https://github.com/amirgholami/adahessian>`__                            | `https://arxiv.org/abs/2006.00719 <https://arxiv.org/abs/2006.00719>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdamD        | *Improved bias-correction in Adam*                                                              |                                                                                   | `https://arxiv.org/abs/2110.10828 <https://arxiv.org/abs/2110.10828>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdamP        | *Slowing Down the Slowdown for Momentum Optimizers on Scale-invariant Weights*                  | `github <https://github.com/clovaai/AdamP>`__                                     | `https://arxiv.org/abs/2006.08217 <https://arxiv.org/abs/2006.08217>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| diffGrad     | *An Optimization Method for Convolutional Neural Networks*                                      | `github <https://github.com/shivram1987/diffGrad>`__                              | `https://arxiv.org/abs/1909.11015v3 <https://arxiv.org/abs/1909.11015v3>`__                   |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| MADGRAD      | *A Momentumized, Adaptive, Dual Averaged Gradient Method for Stochastic*                        | `github <https://github.com/facebookresearch/madgrad>`__                          | `https://arxiv.org/abs/2101.11075 <https://arxiv.org/abs/2101.11075>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| RAdam        | *On the Variance of the Adaptive Learning Rate and Beyond*                                      | `github <https://github.com/LiyuanLucasLiu/RAdam>`__                              | `https://arxiv.org/abs/1908.03265 <https://arxiv.org/abs/1908.03265>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Ranger       | *a synergistic optimizer combining RAdam and LookAhead, and now GC in one optimizer*            | `github <https://github.com/lessw2020/Ranger-Deep-Learning-Optimizer>`__          | `https://bit.ly/3zyspC3 <https://bit.ly/3zyspC3>`__                                           |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Ranger21     | *a synergistic deep learning optimizer*                                                         | `github <https://github.com/lessw2020/Ranger21>`__                                | `https://arxiv.org/abs/2106.13731 <https://arxiv.org/abs/2106.13731>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Lamb         | *Large Batch Optimization for Deep Learning*                                                    | `github <https://github.com/cybertronai/pytorch-lamb>`__                          | `https://arxiv.org/abs/1904.00962 <https://arxiv.org/abs/1904.00962>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Shampoo      | *Preconditioned Stochastic Tensor Optimization*                                                 | `github <https://github.com/moskomule/shampoo.pytorch>`__                         | `https://arxiv.org/abs/1802.09568 <https://arxiv.org/abs/1802.09568>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Nero         | *Learning by Turning: Neural Architecture Aware Optimisation*                                   | `github <https://github.com/jxbz/nero>`__                                         | `https://arxiv.org/abs/2102.07227 <https://arxiv.org/abs/2102.07227>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Adan         | *Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models*                        | `github <https://github.com/sail-sg/Adan>`__                                      | `https://arxiv.org/abs/2208.06677 <https://arxiv.org/abs/2208.06677>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Adai         | *Disentangling the Effects of Adaptive Learning Rate and Momentum*                              | `github <https://github.com/zeke-xie/adaptive-inertia-adai>`__                    | `https://arxiv.org/abs/2006.15815 <https://arxiv.org/abs/2006.15815>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| GSAM         | *Surrogate Gap Guided Sharpness-Aware Minimization*                                             | `github <https://github.com/juntang-zhuang/GSAM>`__                               | `https://openreview.net/pdf?id=edONMAnhLu- <https://openreview.net/pdf?id=edONMAnhLu->`__     |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| D-Adaptation | *Learning-Rate-Free Learning by D-Adaptation*                                                   | `github <https://github.com/facebookresearch/dadaptation>`__                      | `https://arxiv.org/abs/2301.07733 <https://arxiv.org/abs/2301.07733>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdaFactor    | *Adaptive Learning Rates with Sublinear Memory Cost*                                            | `github <https://github.com/DeadAt0m/adafactor-pytorch>`__                        | `https://arxiv.org/abs/1804.04235 <https://arxiv.org/abs/1804.04235>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Apollo       | *An Adaptive Parameter-wise Diagonal Quasi-Newton Method for Nonconvex Stochastic Optimization* | `github <https://github.com/XuezheMax/apollo>`__                                  | `https://arxiv.org/abs/2009.13586 <https://arxiv.org/abs/2009.13586>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| NovoGrad     | *Stochastic Gradient Methods with Layer-wise Adaptive Moments for Training of Deep Networks*    | `github <https://github.com/lonePatient/NovoGrad-pytorch>`__                      | `https://arxiv.org/abs/1905.11286 <https://arxiv.org/abs/1905.11286>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Lion         | *Symbolic Discovery of Optimization Algorithms*                                                 | `github <https://github.com/google/automl/tree/master/lion>`__                    | `https://arxiv.org/abs/2302.06675 <https://arxiv.org/abs/2302.06675>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Ali-G        | *Adaptive Learning Rates for Interpolation with Gradients*                                      | `github <https://github.com/oval-group/ali-g>`__                                  | `https://arxiv.org/abs/1906.05661 <https://arxiv.org/abs/1906.05661>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| SM3          | *Memory-Efficient Adaptive Optimization*                                                        | `github <https://github.com/google-research/google-research/tree/master/sm3>`__   | `https://arxiv.org/abs/1901.11150 <https://arxiv.org/abs/1901.11150>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdaNorm      | *Adaptive Gradient Norm Correction based Optimizer for CNNs*                                    | `github <https://github.com/shivram1987/AdaNorm>`__                               | `https://arxiv.org/abs/2210.06364 <https://arxiv.org/abs/2210.06364>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| RotoGrad     | *Gradient Homogenization in Multitask Learning*                                                 | `github <https://github.com/adrianjav/rotograd>`__                                | `https://openreview.net/pdf?id=T8wHz4rnuGL <https://openreview.net/pdf?id=T8wHz4rnuGL>`__     |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| A2Grad       | *Optimal Adaptive and Accelerated Stochastic Gradient Descent*                                  | `github <https://github.com/severilov/A2Grad_optimizer>`__                        | `https://arxiv.org/abs/1810.00553 <https://arxiv.org/abs/1810.00553>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AccSGD       | *Accelerating Stochastic Gradient Descent For Least Squares Regression*                         | `github <https://github.com/rahulkidambi/AccSGD>`__                               | `https://arxiv.org/abs/1704.08227 <https://arxiv.org/abs/1704.08227>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| SGDW         | *Decoupled Weight Decay Regularization*                                                         | `github <https://github.com/loshchil/AdamW-and-SGDW>`__                           | `https://arxiv.org/abs/1711.05101 <https://arxiv.org/abs/1711.05101>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ASGD         | *Adaptive Gradient Descent without Descent*                                                     | `github <https://github.com/ymalitsky/adaptive_GD>`__                             | `https://arxiv.org/abs/1910.09529 <https://arxiv.org/abs/1910.09529>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Yogi         | *Adaptive Methods for Nonconvex Optimization*                                                   |                                                                                   | `NIPS 2018 <https://papers.nips.cc/paper/8186-adaptive-methods-for-nonconvex-optimization>`__ |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| SWATS        | *Improving Generalization Performance by Switching from Adam to SGD*                            |                                                                                   | `https://arxiv.org/abs/1712.07628 <https://arxiv.org/abs/1712.07628>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Fromage      | *On the distance between two neural networks and the stability of learning*                     | `github <https://github.com/jxbz/fromage>`__                                      | `https://arxiv.org/abs/2002.03432 <https://arxiv.org/abs/2002.03432>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| MSVAG        | *Dissecting Adam: The Sign, Magnitude and Variance of Stochastic Gradients*                     | `github <https://github.com/lballes/msvag>`__                                     | `https://arxiv.org/abs/1705.07774 <https://arxiv.org/abs/1705.07774>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AdaMod       | *An Adaptive and Momental Bound Method for Stochastic Learning*                                 | `github <https://github.com/lancopku/AdaMod>`__                                   | `https://arxiv.org/abs/1910.12249 <https://arxiv.org/abs/1910.12249>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| AggMo        | *Aggregated Momentum: Stability Through Passive Damping*                                        | `github <https://github.com/AtheMathmo/AggMo>`__                                  | `https://arxiv.org/abs/1804.00325 <https://arxiv.org/abs/1804.00325>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| QHAdam       | *Quasi-hyperbolic momentum and Adam for deep learning*                                          | `github <https://github.com/facebookresearch/qhoptim>`__                          | `https://arxiv.org/abs/1810.06801 <https://arxiv.org/abs/1810.06801>`__                       |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| PID          | *A PID Controller Approach for Stochastic Optimization of Deep Networks*                        | `github <https://github.com/tensorboy/PIDOptimizer>`__                            | `CVPR 18 <http://www4.comp.polyu.edu.hk/~cslzhang/paper/CVPR18_PID.pdf>`__                    |
+--------------+-------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Useful Resources
----------------

Several optimization ideas to regularize & stabilize the training. Most
of the ideas are applied in ``Ranger21`` optimizer.

Also, most of the captures are taken from ``Ranger21`` paper.

+------------------------------------------+---------------------------------------------+--------------------------------------------+
| `Adaptive Gradient Clipping`_            | `Gradient Centralization`_                  | `Softplus Transformation`_                 |
+------------------------------------------+---------------------------------------------+--------------------------------------------+
| `Gradient Normalization`_                | `Norm Loss`_                                | `Positive-Negative Momentum`_              |
+------------------------------------------+---------------------------------------------+--------------------------------------------+
| `Linear learning rate warmup`_           | `Stable weight decay`_                      | `Explore-exploit learning rate schedule`_  |
+------------------------------------------+---------------------------------------------+--------------------------------------------+
| `Lookahead`_                             | `Chebyshev learning rate schedule`_         | `(Adaptive) Sharpness-Aware Minimization`_ |
+------------------------------------------+---------------------------------------------+--------------------------------------------+
| `On the Convergence of Adam and Beyond`_ | `Gradient Surgery for Multi-Task Learning`_ |                                            |
+------------------------------------------+---------------------------------------------+--------------------------------------------+

Adaptive Gradient Clipping
--------------------------

| This idea originally proposed in ``NFNet (Normalized-Free Network)`` paper.
| ``AGC (Adaptive Gradient Clipping)`` clips gradients based on the ``unit-wise ratio of gradient norms to parameter norms``.

-  code : `github <https://github.com/deepmind/deepmind-research/tree/master/nfnets>`__
-  paper : `arXiv <https://arxiv.org/abs/2102.06171>`__

Gradient Centralization
-----------------------

+-----------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/gradient_centralization.png  |
+-----------------------------------------------------------------------------------------------------------------+

``Gradient Centralization (GC)`` operates directly on gradients by centralizing the gradient to have zero mean.

-  code : `github <https://github.com/Yonghongwei/Gradient-Centralization>`__
-  paper : `arXiv <https://arxiv.org/abs/2004.01461>`__

Softplus Transformation
-----------------------

By running the final variance denom through the softplus function, it lifts extremely tiny values to keep them viable.

-  paper : `arXiv <https://arxiv.org/abs/1908.00700>`__

Gradient Normalization
----------------------

Norm Loss
---------

+---------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/norm_loss.png  |
+---------------------------------------------------------------------------------------------------+

-  paper : `arXiv <https://arxiv.org/abs/2103.06583>`__

Positive-Negative Momentum
--------------------------

+--------------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/positive_negative_momentum.png  |
+--------------------------------------------------------------------------------------------------------------------+

-  code : `github <https://github.com/zeke-xie/Positive-Negative-Momentum>`__
-  paper : `arXiv <https://arxiv.org/abs/2103.17182>`__

Linear learning rate warmup
---------------------------

+----------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/linear_lr_warmup.png  |
+----------------------------------------------------------------------------------------------------------+

-  paper : `arXiv <https://arxiv.org/abs/1910.04209>`__

Stable weight decay
-------------------

+-------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/stable_weight_decay.png  |
+-------------------------------------------------------------------------------------------------------------+

-  code : `github <https://github.com/zeke-xie/stable-weight-decay-regularization>`__
-  paper : `arXiv <https://arxiv.org/abs/2011.11152>`__

Explore-exploit learning rate schedule
--------------------------------------

+---------------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/kozistr/pytorch_optimizer/main/assets/explore_exploit_lr_schedule.png  |
+---------------------------------------------------------------------------------------------------------------------+

-  code : `github <https://github.com/nikhil-iyer-97/wide-minima-density-hypothesis>`__
-  paper : `arXiv <https://arxiv.org/abs/2003.03977>`__

Lookahead
---------

| ``k`` steps forward, 1 step back. ``Lookahead`` consisting of keeping an exponential moving average of the weights that is
| updated and substituted to the current weights every ``k_{lookahead}`` steps (5 by default).

-  code : `github <https://github.com/alphadl/lookahead.pytorch>`__
-  paper : `arXiv <https://arxiv.org/abs/1907.08610v2>`__

Chebyshev learning rate schedule
--------------------------------

Acceleration via Fractal Learning Rate Schedules

-  paper : `arXiv <https://arxiv.org/abs/2103.01338v1>`__

(Adaptive) Sharpness-Aware Minimization
---------------------------------------

| Sharpness-Aware Minimization (SAM) simultaneously minimizes loss value and loss sharpness.
| In particular, it seeks parameters that lie in neighborhoods having uniformly low loss.

-  SAM paper : `paper <https://arxiv.org/abs/2010.01412>`__
-  ASAM paper : `paper <https://arxiv.org/abs/2102.11600>`__
-  A/SAM code : `github <https://github.com/davda54/sam>`__

On the Convergence of Adam and Beyond
-------------------------------------

- paper : `paper <https://openreview.net/forum?id=ryQu7f-RZ>`__

Gradient Surgery for Multi-Task Learning
----------------------------------------

- paper : `paper <https://arxiv.org/abs/2001.06782>`__

Citations
---------

`AdamP <https://github.com/clovaai/AdamP#how-to-cite>`__

`Adaptive Gradient Clipping <https://ui.adsabs.harvard.edu/abs/2021arXiv210206171B/exportcitation>`__

`Chebyshev LR Schedules <https://ui.adsabs.harvard.edu/abs/2021arXiv210301338A/exportcitation>`__

`Gradient Centralization <https://github.com/Yonghongwei/Gradient-Centralization#citation>`__

`Lookahead <https://ui.adsabs.harvard.edu/abs/2019arXiv190708610Z/exportcitation>`__

`RAdam <https://github.com/LiyuanLucasLiu/RAdam#citation>`__

`Norm Loss <https://ui.adsabs.harvard.edu/abs/2021arXiv210306583G/exportcitation>`__

`Positive-Negative Momentum <https://github.com/zeke-xie/Positive-Negative-Momentum#citing>`__

`Explore-Exploit Learning Rate Schedule <https://ui.adsabs.harvard.edu/abs/2020arXiv200303977I/exportcitation>`__

`On the adequacy of untuned warmup for adaptive optimization <https://ui.adsabs.harvard.edu/abs/2019arXiv191004209M/exportcitation>`__

`Stable weight decay regularization <https://github.com/zeke-xie/stable-weight-decay-regularization#citing>`__

`Softplus transformation <https://ui.adsabs.harvard.edu/abs/2019arXiv190800700T/exportcitation>`__

`MADGRAD <https://github.com/facebookresearch/madgrad#tech-report>`__

`AdaHessian <https://github.com/amirgholami/adahessian#citation>`__

`AdaBound <https://github.com/Luolc/AdaBound#citing>`__

`Adabelief <https://ui.adsabs.harvard.edu/abs/2020arXiv201007468Z/exportcitation>`__

`Sharpness-aware minimization <https://ui.adsabs.harvard.edu/abs/2020arXiv201001412F/exportcitation>`__

`Adaptive Sharpness-aware minimization <https://ui.adsabs.harvard.edu/abs/2021arXiv210211600K/exportcitation>`__

`diffGrad <https://ui.adsabs.harvard.edu/abs/2019arXiv190911015D/exportcitation>`__

`On the Convergence of Adam and Beyond <https://ui.adsabs.harvard.edu/abs/2019arXiv190409237R/exportcitation>`__

`Gradient surgery for multi-task learning <https://ui.adsabs.harvard.edu/abs/2020arXiv200106782Y/exportcitation>`__

`AdamD <https://ui.adsabs.harvard.edu/abs/2021arXiv211010828S/exportcitation>`__

`Shampoo <https://ui.adsabs.harvard.edu/abs/2018arXiv180209568G/exportcitation>`__

`Nero <https://ui.adsabs.harvard.edu/abs/2021arXiv210207227L/exportcitation>`__

`Adan <https://ui.adsabs.harvard.edu/abs/2022arXiv220806677X/exportcitation>`__

`Adai <https://github.com/zeke-xie/adaptive-inertia-adai#citing>`__

`GSAM <https://github.com/juntang-zhuang/GSAM#citation>`__

`D-Adaptation <https://ui.adsabs.harvard.edu/abs/2023arXiv230107733D/exportcitation>`__

`AdaFactor <https://ui.adsabs.harvard.edu/abs/2018arXiv180404235S/exportcitation>`__

`Apollo <https://ui.adsabs.harvard.edu/abs/2020arXiv200913586M/exportcitation>`__

`NovoGrad <https://ui.adsabs.harvard.edu/abs/2019arXiv190511286G/exportcitation>`__

`Lion <https://github.com/google/automl/tree/master/lion#citation>`__

`Ali-G <https://github.com/oval-group/ali-g#adaptive-learning-rates-for-interpolation-with-gradients>`__

`SM3 <https://ui.adsabs.harvard.edu/abs/2019arXiv190111150A/exportcitation>`__

`AdaNorm <https://github.com/shivram1987/AdaNorm/tree/main#citation>`__

`RotoGrad <https://github.com/adrianjav/rotograd#citing>`__

`A2Grad <https://ui.adsabs.harvard.edu/abs/2018arXiv181000553D/exportcitation>`__

`AccSGD <https://github.com/rahulkidambi/AccSGD#citation>`__

`SGDW <https://github.com/loshchil/AdamW-and-SGDW#contact>`__

`Adaptive SGD <https://github.com/ymalitsky/adaptive_GD#reference>`__

`Yogi <https://proceedings.neurips.cc/paper_files/paper/2018/hash/90365351ccc7437a1309dc64e4db32a3-Abstract.html>`__

`SWATS <https://ui.adsabs.harvard.edu/abs/2017arXiv171207628S/exportcitation>`__

`Fromage <https://github.com/jxbz/fromage#citation>`__

`MSVAG <https://github.com/lballes/msvag#citation>`__

`AdaMod <https://github.com/lancopku/AdaMod#citation>`__

`AggMo <https://ui.adsabs.harvard.edu/abs/2018arXiv180400325L/exportcitation>`__

`QHAdam <https://github.com/facebookresearch/qhoptim#reference>`__

`PID <https://github.com/tensorboy/PIDOptimizer#citation>`__

Citation
--------

Please cite original authors of optimization algorithms. If you use this software, please cite it as below.
Or you can get from "cite this repository" button.

::

    @software{Kim_pytorch_optimizer_Optimizer_and_2022,
        author = {Kim, Hyeongchan},
        month = {1},
        title = {{pytorch_optimizer: optimizer and lr scheduler collections in PyTorch}},
        version = {1.0.0},
        year = {2022}
    }

Author
------

Hyeongchan Kim / `@kozistr <http://kozistr.tech/about>`__

.. |workflow| image:: https://github.com/kozistr/pytorch_optimizer/actions/workflows/ci.yml/badge.svg?branch=main
.. |Documentation Status| image:: https://readthedocs.org/projects/pytorch-optimizers/badge/?version=latest
   :target: https://pytorch-optimizers.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/pytorch-optimizer.svg
   :target: https://badge.fury.io/py/pytorch-optimizer
.. |PyPi download| image:: https://pepy.tech/badge/pytorch-optimizer
   :target: https://pepy.tech/project/pytorch-optimizer
.. |PyPi month download| image:: https://pepy.tech/badge/pytorch-optimizer/month
   :target: https://pepy.tech/project/pytorch-optimizer
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/pytorch-optimizer.svg
   :target: https://pypi.python.org/pypi/pytorch-optimizer/
.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json
   :target: https://github.com/charliermarsh/ruff
.. |codecov| image:: https://codecov.io/gh/kozistr/pytorch_optimizer/branch/main/graph/badge.svg?token=L4K00EA0VD
   :target: https://codecov.io/gh/kozistr/pytorch_optimizer
.. |apache| image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
