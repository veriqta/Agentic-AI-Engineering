# Verification and Completion Record

## State definitions

Planned means specified but not started. In progress means active work. Executed means run with actual output. Verified means that output and required checks were reviewed. Assessed means understanding or practical criteria were evaluated. Completed requires the lesson's required criteria. Published means merged classroom material available on main, not merely a proposed branch or PR.

## Current milestone

| Item | State | Evidence boundary |
|---|---|---|
| Introductory Python examples | Execution verified | Reviewed source/output screenshots; instructional transcriptions included |
| Baseline support responses | Execution verified | Paid and unpaid output reviewed; public example name is Sarah |
| Improved support implementation | Source reviewed, execution verified | Application source visible across supplied screenshots |
| Initial test suite | Eight methods verified | Learner execution screenshot |
| Added unpaid CLI check | Nine-method run verified | Later screenshot lists added method and OK; exact saved final method body was not separately exported |
| Publication layout | Locally verified | Packaged reference source and tests executed in publication environment |
| Detailed walkthrough | In progress | Instruction delivered in stages; not all understanding established |
| Knowledge check and trust scenario | Pending assessment | No answer or grade invented |
| Debugging exercise | Planned | Expected behavior documented; learner execution not established |
| Lesson completion | In progress | Assessment requirements remain open |
| Week 01 and Module 01 | In progress | Remaining weekly objectives and module assessment not complete |
| Main publication | Pending PR review and merge | Branch material is a proposal |

## Reproducibility and provenance

The application is an instructional transcription of reviewed screenshot-visible code, not a byte-for-byte file transfer from EC2. The initial eight-test source was reviewed in screenshots. The ninth reference method follows the instructed assessment implementation and was tested locally. Publication moves application and tests into src and tests, adjusts the test application path and supplies PYTHONPATH=src. Those layout changes are verified locally rather than represented as a learner rerun.

Learner environment evidence reports Ubuntu on EC2 with Python 3.14.4. Actual screenshots show the paid/unpaid responses and nine passing methods. Timing is not used as a benchmark. No live EC2 connection was used by the publisher.

Raw screenshots are deliberately excluded because terminal prompts and tabs expose cloud host identifiers and unrelated personal surroundings. They were reviewed as evidence, not regenerated. Public-safe genuine screenshots remain a follow-up; no synthetic terminal images are included.

## Actual publication checks

Python 3.12.14. The nine-method suite passed. Paid normalization, unpaid JSON, invalid-status exit behavior and three introductory examples were also executed and checked. See [actual test output](evidence/publication-test-results.txt) and [actual CLI results](evidence/publication-cli-results.json).

An initial test invocation from the repository root failed because the lesson's tests directory was not the selected start directory. Running the documented command from the lesson directory corrected the invocation; this was a publisher working-directory error, not an application test failure.

Application SHA-256: `fced808680111e38a5ffed56b0a43076bf0dbe829bc765dbf859461fa8ee3e7f`.

## Known limits

No model, real payment lookup, authentication, access grant, durable storage, deployment, network failure handling or production readiness is established. The current checks cover defined examples only. Full understanding assessments, debugging evidence, remaining module work and merge approval are outstanding.
