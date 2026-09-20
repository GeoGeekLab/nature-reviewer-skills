# Curated reference review

## Major concern — the inferred ecological breakpoint is not separated from the sensor transition

**Claim under review**

The manuscript interprets the stronger post-2014 greening slope and the 2014 breakpoint as a climate-driven acceleration in vegetation productivity.

**Evidence anchor**

The Methods state that Sensor A is used through 2013 and Sensor B from 2014 onward. The Results then identify 2014 as the breakpoint in the merged time series.

**Failure mode**

The observing system changes at exactly the point where the manuscript detects a change in the Earth-system signal. Reprojection to a common grid does not establish radiometric or spectral equivalence. Differences in spectral response, retrieval processing, resolution, compositing behavior, or product calibration could introduce an offset or slope discontinuity that the segmented regression would interpret as a physical breakpoint.

**Why this matters**

The central attribution depends on the post-2014 acceleration being geophysical rather than instrumental. With the current design, those explanations are not distinguishable from the excerpt.

**Alternative explanation**

Part or all of the detected breakpoint could arise from the product transition rather than from a change in vegetation response to warming.

**Required revision**

The manuscript should demonstrate temporal consistency across the sensor transition. At minimum:

1. use an overlap period, if available, to quantify Sensor A–Sensor B bias and uncertainty;
2. test the trend with an explicit sensor/platform term or harmonization model;
3. repeat the breakpoint analysis using same-sensor subsets or an independently harmonized record;
4. propagate harmonization uncertainty into the pre/post slope comparison; and
5. weaken the climate-attribution claim unless the breakpoint remains robust to these tests.

**Severity:** Major

**Calibrated conclusion if additional harmonization is unavailable**

The current analysis supports a change in the **combined product record**, but it does not yet establish that the 2014 breakpoint represents an acceleration in ecosystem greening caused by warming.
