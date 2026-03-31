---
title:          "Optimization and Evaluation of Container-Based EtherCAT Communication in Virtual PLCs"
date:           2026-3-31 00:01:00 +0800
selected:       true
pub:            "IEEE Transactions on Industrial Electronics"
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">Journal</span>'
pub_date:       "2026"
abstract: >-
  Deploying EtherCAT in container-based virtualized programmable logic controllers (vPLCs) faces critical challenges regarding driver portability, network determinism, and synchronization scalability. This article proposes a container-native architecture named vECAT by leveraging the data plane development kit (DPDK) for high-performance user-space packet processing, which eliminates kernel dependencies and ensures cross-platform portability. We develop a latency model that characterizes the end-to-end packet processing pipeline and guides systematic optimizations at the task, OS, and hardware levels. We also introduce an enhanced synchronization algorithm to address error accumulation in large-scale networks. Validated on x86, ARM, and RISC-V platforms running PREEMPT_RT Linux, the proposed solution achieves maximum jitters of 11, 12, 24 µs at a 125 µs cycle time on three typical types of vPLCs CPUs under various kinds of stress loads. Furthermore, the optimized synchronization mechanism eliminates the linear accumulation of synchronization error, achieving bounded precision validated on networks with up to 8 subdevices.

authors:
  - Nan Zhou
  - Yingfei Yao
  - Xiaojun Liang
  - Shunchun Yao
  - Chunhua Yang
  - Weihua Gui
links:
  Paper: https://ieeexplore.ieee.org/abstract/document/11436082
---
