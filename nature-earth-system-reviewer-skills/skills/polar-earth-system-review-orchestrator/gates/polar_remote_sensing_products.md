# Polar Remote Sensing Products

Retrieval algorithms, version lineage, sensor transitions, coverage gaps, resolution, radar ambiguity and validation scale.

## Internal questions

- **Retrieval product treated as direct truth:** A satellite retrieval is used as a direct observation without describing algorithm assumptions, flags, known failure modes, or product uncertainty. Resolution: Cite the exact product version and algorithm documentation, apply quality flags, and propagate retrieval uncertainty into the main result.
- **Melt ponds and wet snow bias sea-ice retrieval:** Summer sea-ice concentration or type is interpreted without testing melt-pond, wet-snow, atmospheric, and thin-ice ambiguity. Resolution: Use season-appropriate products, compare independent sensors or algorithms, and bound the effect of surface-state ambiguity.
- **Sensor transition creates artificial trend:** A long record spans missions, processing streams, or orbit changes without an explicit homogeneity assessment. Resolution: Perform overlap calibration, breakpoint tests, product intercomparison, and sensitivity to transition treatment.
- **Polar gap or coverage mask is ignored:** Orbit geometry, pole holes, cloud screening, darkness, topographic shadow, or coastal masks exclude nonrandom parts of the domain. Resolution: Show coverage through time, distinguish observed from infilled cells, and test conclusions under conservative gap treatments.
- **Spatial resolution cannot resolve mechanism:** The product grid or radar footprint is too coarse to resolve grounding zones, narrow fjords, leads, small glaciers, thermokarst features, or coastal gradients invoked in the mechanism. Resolution: Demonstrate scale compatibility, aggregate the claim to resolvable scales, or add higher-resolution evidence.
- **Radar interpretation lacks dielectric alternatives:** Radar backscatter, interferometric phase, attenuation, or reflectors are assigned to water, brine, layer geometry, or damage without excluding other dielectric and geometric causes. Resolution: Use multi-frequency, temporal, geometric, or in situ constraints and present the interpretation as conditional where alternatives remain.
- **Validation scale mismatches product scale:** Point or transect field measurements are compared directly with large grid cells or temporally averaged products. Resolution: Upscale field data with a defensible model, sample the grid footprint, and separate measurement from representativeness uncertainty.
- **Algorithm comparison is not independent:** Products compared as independent evidence share sensors, weather filters, ancillary fields, training data, or common retrieval heritage. Resolution: Map data lineage, select genuinely independent observations where possible, and qualify ensemble agreement by shared dependencies.

Use only when relevant to a central claim. Do not expose this gate name or pattern IDs in the final referee report.
