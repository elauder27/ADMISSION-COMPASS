🧾 Model Card – Admission Compass
Project: Admission Compass

Purpose: Admission probability estimation for Nigerian universities

1. Model Overview

Admission Compass is a machine learning–powered decision-support system designed to estimate the probability that an applicant may be admitted into a selected university and course of study.

Instead of producing binary outcomes (admitted / not admitted), the system provides probabilistic guidance (e.g., “68% chance of admission”) to help applicants better understand competitiveness and make informed decisions.

Admission Compass is advisory, not authoritative.

2. Intended Use

Admission Compass is intended for:

Student self-assessment and guidance

Academic research and learning

Demonstration of admission modeling techniques

Portfolio and educational use

It is designed to help applicants understand relative chances, not to determine outcomes.

3. Out-of-Scope Uses

Admission Compass must NOT be used for:

Official admission decisions

Automated acceptance or rejection of applicants

Institutional applicant ranking

Policy enforcement or quota allocation

Predictions are not guarantees and must not replace institutional discretion.

4. Data Description

Admission Compass models are trained using synthetic datasets generated from:

Publicly available admission guidelines

Known cut-off benchmarks

O’level grading structures

Eligibility rules commonly applied by institutions

⚠️ Important:
No official admission records from any university are used.
Synthetic data may not fully capture real-world applicant distributions, yearly competition, or institutional discretion.

5. Input Features

Across supported institutions, models may use combinations of the following features:

Feature	Description
UTME_Score	Applicant UTME score
Faculty	Selected faculty
Department	Selected course/department
Olevel_Valid	Whether minimum O’level requirements are met
Olevel_Avg_Points	Average O’level grade points
Screening/Aggregate Scores	Institution-specific aggregate calculations

Features Explicitly Excluded

To reduce bias and ethical risk, Admission Compass does not use:

Gender

Religion

Ethnicity

State or LGA of origin

Applicant names or identity

Socio-economic indicators

6. Model Architecture

Admission Compass uses a modular modeling approach, typically involving:

Tree-based classifiers (e.g., Random Forest)

Proper preprocessing pipelines

Probability calibration (e.g., isotonic regression)

Leakage-aware feature engineering

Models are trained to learn patterns, not enforce rules.

7. Probability Calibration

All probability outputs are calibrated, meaning:

A 70% probability approximates a real-world likelihood

Outputs are smoother and less overconfident

Low-probability outcomes are still meaningfully represented

This ensures probabilities are informative even for non-admitted applicants.

8. Evaluation Metrics

Models are evaluated using:

Accuracy

Precision

Recall

F1-score

⚠️ Interpretation Note:
High accuracy does not imply certainty.
Admission is competitive and relative to the applicant pool.

9. Explainability

Admission Compass includes an explainability layer that:

Contextualizes UTME scores relative to benchmarks

Explains aggregate score positioning

Highlights eligibility constraints

Avoids opaque “black-box” decisions

This improves user trust and understanding.

10. Known Limitations

Admission Compass does not currently model:

Yearly applicant pool strength variations

Departmental quota enforcement

Post-UTME or interview performance

Institutional discretionary decisions

Predictions should be interpreted as guidance, not outcomes.

11. Ethical Considerations

Admission Compass is designed with the following principles:

No protected attributes used

No deterministic acceptance/rejection

Transparent probability reporting

Clear disclaimers for users

The system prioritizes fairness, transparency, and responsible use.

12. Versioning & Scope

Models are institution-specific but follow a unified framework

Each model version is trained and evaluated independently

Future expansions may include:

Cross-university normalization

Confidence intervals

Applicant pool competitiveness indices

13. Disclaimer

Admission Compass is an informational and advisory tool only.

It does not represent JAMB, any Nigerian university, or any admission authority.
Final admission decisions remain solely with the institutions.

14. Author & Project

Developed as part of Admission Compass
By: Okedinachi Chibundu Chosen
