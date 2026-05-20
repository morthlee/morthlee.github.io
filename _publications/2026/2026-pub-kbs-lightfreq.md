---
title:          "LightFreq: Adaptive Frequency Learning for Efficient and Multi-Domain Time Series Forecasting"
date:           2026-1-01 00:01:00 +0800
selected:       false
pub:            "Knowledge-Based Systems"
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">Journal</span>'
pub_date:       "2026"
abstract: >-
  Time series forecasting is essential for decision-making and optimization in various fields, including energy, healthcare, and smart manufacturing. Adapting forecasting models across different domains is crucial to enable knowledge shift to new tasks with minimal domain-specific engineering and minimal development costs. However, the diversities among different domains, such as variations in data distribution, frequency, and noise, demand models with strong representation capabilities. This often, in turn, leads to increased complexity and large parameter calculation. Furthermore, time series data frequently involves privacy concerns, necessitating local deployment on resource-constrained edge devices where computational efficiency is paramount. To address these challenges, we propose a lightweight yet effective neural network, termed as LightFreq, that adaptively integrates temporal and frequency information through a dynamic weighting strategy. The case studies demonstrate that LightFreq achieves competitive forecasting accuracy on eight real-world datasets, matching or even surpassing state-of-the-art models with only 100k trainable parameters. Specifically, extensive experiments demonstrate that LightFreq achieves the best or competitive results in up to 21 out of 32 forecasting settings. Our model achieves an average reduction in forecasting error by 10% compared to state-of-the-art baselines under full-shot experiments. Furthermore, our model demonstrates competitive in-domain zero-shot forecasting capabilities, performing on par with large time series baselines on unseen sequences without prior exposure to their historical data. Notably, while maintaining high precision, our approach adheres to a strict resource-constrained design, requiring less than 1% of the parameters compared with Time-MoE. Overall, LightFreq offers a compelling trade-off, delivering superior accuracy with minimal computational cost, and is particularly suited for scalable deployment in real-world, resource-constrained scenarios.

cover:          /assets/images/covers/default.png
authors:
  - Wei Wu
  - Xuening Li
  - Xiaojun Liang
  - Chunhua Yang
  - Weihua Gui
  - Yiqi Liu
  - Nan Zhou
links:
  Paper: https://www.sciencedirect.com/science/article/pii/S0950705126002984
---
