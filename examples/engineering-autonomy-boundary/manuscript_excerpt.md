# Synthetic manuscript excerpt

## Claim

We present a fully autonomous closed-loop platform for optimizing a polymer formulation. A Bayesian optimization algorithm selects the next composition, a liquid-handling robot prepares the sample, and an inline optical measurement returns the objective value to the optimizer.

The system completed 120 optimization experiments over four days and identified a formulation with a 31% higher objective value than the initial design. We therefore conclude that the platform enables autonomous materials discovery without human intervention.

## Operational procedure

During the campaign, a researcher remained on site. If the robot reported a pipetting fault, the researcher reseated the affected tip rack and restarted the run. Samples showing visible bubbles were manually flagged and their optical measurements were excluded before the optimizer was updated. When the optical cell fouled, the researcher cleaned the cell and repeated the previous measurement.

The manuscript reports the 120 completed optimization experiments but does not report the number of failed robot actions, repeated measurements, manually excluded samples, intervention time, or how optimization performance changes when those interventions are counted.

## Interpretation

Because candidate selection and nominal sample preparation were algorithmically controlled, we describe the complete workflow as fully autonomous.
