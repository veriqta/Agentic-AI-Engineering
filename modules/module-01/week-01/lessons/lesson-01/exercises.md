# Improvement Exercises

These are future practice tasks, not completed achievements.

1. Add CLI tests for missing required flags and a whitespace-only name. Require nonzero status and no success JSON. Explain whether argparse or application validation handles each failure.
2. Extend response tests to pending and refunded using subtests. Preserve the current policy and explain the difference between a recognized status and approval.
3. Design a structured result containing a decision code alongside the message. Define its contract and tests before changing the implementation. Do not infer real payment evidence from the new structure.
4. Propose where a future trusted payment lookup belongs. Identify timeout, authentication and stale-data failures. Implementation waits for the external-systems milestone.

Discuss which behavior is required before accepting an AI-generated improvement. Review its diff, tests, new dependencies and side effects. Keep each change on a feature branch and request review through a PR.
