# Curated reference review

## Major concern — the claimed autonomy boundary excludes human actions that are necessary for the loop to continue

**Claim under review**

The manuscript describes the platform as “fully autonomous” and states that the four-day optimization campaign operated without human intervention.

**Evidence anchor**

The operational procedure states that a researcher reseated hardware after pipetting faults, manually excluded bubble-containing samples, cleaned the optical cell, repeated measurements, and restarted interrupted runs.

**Failure mode**

These are not peripheral observations outside the experimental system. They affect execution, data acceptance, measurement recovery, and whether an observation is returned to the optimizer. The current performance accounting conditions on successful human-assisted recovery while the headline claim assigns the resulting campaign to the autonomous system.

**Why this matters**

Autonomy is a system-level engineering claim. Its evidence must include exception handling, failure recovery, data-quality decisions, and uptime—not only nominal candidate selection and robot actuation. Hidden operator recovery can materially change throughput, reliability, and optimization performance.

**Alternative explanation**

The reported campaign may demonstrate a highly automated human-supervised laboratory rather than a fully autonomous laboratory.

**Required revision**

The authors should define the autonomy boundary operationally and report the intervention burden. At minimum:

1. count robot faults, repeated runs, manual exclusions, cleaning events, and restarts;
2. report human intervention time and the fraction of experimental cycles requiring intervention;
3. specify which data-quality decisions are algorithmic versus manual;
4. include failures and repeated experiments in throughput and success-rate metrics; and
5. either automate the recovery/quality-control steps or recalibrate the claim to “automated, human-supervised closed-loop optimization.”

A stronger autonomy claim would require pre-specified machine-executable fault detection, recovery, and data-quality rules that allow the loop to continue without discretionary operator decisions.

**Severity:** Major

**Calibrated conclusion from the current evidence**

The platform demonstrates closed-loop algorithmic experiment selection with robotic execution under human supervision; the excerpt does not establish fully autonomous operation.
