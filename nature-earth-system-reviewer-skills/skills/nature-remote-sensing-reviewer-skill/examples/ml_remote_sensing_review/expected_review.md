Referee #2 (Remarks to the Author):
The manuscript targets an important agricultural monitoring problem and the proposed product could be valuable if its generality is established. The present validation design is not sufficient to support the claimed global applicability.

The major concern is spatial leakage. A random pixel-level split across spatially autocorrelated samples can inflate apparent accuracy because nearby pixels share crop type, management, soil, climate, and acquisition conditions. The authors should repeat validation using spatially blocked folds and leave-region-out tests, and should report performance by province, crop type, and acquisition condition.

A second concern is the lack of transparent baselines. The manuscript should compare the neural network with simpler spectral-index, classical machine-learning, or other provided baseline approaches, and should include ablations to show which model components drive performance. Until those tests are provided, the global generalization claim should be calibrated to the sampled provinces.
