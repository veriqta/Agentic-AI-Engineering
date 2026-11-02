# 13. Verification, Provenance and Completion State

## Scope

This record describes reference software and classroom material. It does not certify a reader's understanding, a real payment or production deployment. The numbered edition is a new layout and was checked separately from the earlier interactive execution.

## Actual reference execution

Publisher environment: Python 3.12.14, operating-system family Linux. The reference evidence runner executed the numbered application and tests in an isolated temporary directory. Actual streams, arguments and exit codes are retained in [02-reference-run](20-evidence/02-reference-run/08-manifest.json).

| Check | Actual outcome | Evidence |
|---|---|---|
| Normalized paid request | Exit 0, expected JSON | [Success record](20-evidence/02-reference-run/03-success.json) |
| Numbered test suite | Nine test methods passed | [Test record](20-evidence/02-reference-run/04-tests.json) |
| Unsupported status | Exit 2, empty stdout, controlled error | [Invalid record](20-evidence/02-reference-run/05-invalid.json) |
| Deliberate removal of lower in temporary copy | Suite failed as intended | [Regression record](20-evidence/02-reference-run/06-regression.json) |
| Restored source in temporary copy | Nine methods passed again | [Recovery record](20-evidence/02-reference-run/07-recovery.json) |

The four [SVG execution-output panels](19-images/00-README.md) render real recorded results. They are not AI-generated terminal images or screenshots of a learner host. The raw output is authoritative. Rendering wraps lines and labels excerpts; it does not run the application again. Timings are observations, not performance benchmarks.

## Errors encountered while preparing this edition

The first attempt used unittest discovery with a digit-prefixed filename. It ran zero tests. A wildcard pattern alone did not fix the module-name restriction. The final commands execute the numbered test script directly, and the actual nine-method and recovery runs passed. This cause and correction are taught in testing and troubleshooting rather than hidden behind a passing summary.

The final evidence bundle contains the corrected execution. No unexecuted outcome or failed attempt is represented as success. A browser screenshot renderer was unavailable, so exact SVG panels were created from raw records instead; they are labeled output renderings rather than screen photographs.

## Source fingerprints

Application SHA-256: `fced808680111e38a5ffed56b0a43076bf0dbe829bc765dbf859461fa8ee3e7f`.

Test source SHA-256: `1197d2e363313d011042c462ae57f502cec9ec84237d037cf99c5161bb03df1c`.

The environment record retains these values. A changed source or test requires fresh evidence rather than reusing an older passing image.

## Earlier evidence preserved

Introductory welcome execution, the decision script's approval branch, baseline paid/unpaid responses and the improved nine-method test milestone were previously reviewed in learner-provided screenshots. Earlier environment evidence reported Ubuntu on EC2 with Python 3.14.4. The scripts here are instructional transcriptions, not byte-for-byte exports from that host. Names and explanatory comments were adapted for public teaching. The final added test's named successful run was visible; its exact saved body was not independently exported after execution.

The numbered source loading and reference evidence runner are publisher additions. Their execution does not retroactively establish that a learner executed the new layout or completed its assessment. No live connection to the learner's EC2 environment was used.

Raw learner screenshots remain excluded because they contain environment identifiers and unrelated personal content. Public comparison visuals now come from actual local reference execution without those identifiers.

## Progress by scope

| Scope | State | Remaining criteria |
|---|---|---|
| Reference application | Executed and verified for documented cases | Future integrations need their own checks |
| Reference testing workflow | Executed and verified | No universal coverage claim |
| Reference failure/recovery demonstration | Executed and verified by publisher | Learner investigation must be reviewed separately |
| Interactive detailed walkthrough | In progress | Remaining components and understanding review |
| Knowledge check | Not fully assessed | Review reasoning and address gaps |
| Payment-authority scenario | Pending | No answer or grade invented |
| Learner practical assessment | In progress | Debugging and judgment evidence |
| Lesson 01 | Not marked completed | Essential understanding and required assessment |
| Week 01 | In progress | Full weekly objectives and project review |
| Module 01 | In progress | Four-week objectives and module assessment |
| Publication | Proposed in feature-branch PR | Owner review and merge |

## Known limitations

No LLM, authenticated payment lookup, actual entitlement change, durable storage, public API, external credentials, network reliability, deployment or production readiness is established. The application uses a small explicit status contract. Tests prove their assertions for supplied cases and environments. Portfolio claims must stay within that evidence.
