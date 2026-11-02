# 20. Execution Evidence and Reproduction

[01_reproduce_evidence.py](01_reproduce_evidence.py) runs the current application and suite in an isolated temporary layout. It captures source/test fingerprints, environment, successful request, tests, invalid request, deliberate normalization regression and recovery. It makes no payment calls or deployment changes.

From the lesson directory, use `python3 20-evidence/01_reproduce_evidence.py --output veriqta-project-evidence`. The destination must not already exist. Read the [weekly project](../07-weekly-project.md) for the complete code explanation and command purpose.

The [reference-run](02-reference-run/08-manifest.json) directory contains actual publisher output. It does not establish individual learner assessment. The execution captures in [19-images](../19-images/00-README.md) display these records for comparison. The earlier learner screenshots were reviewed but are not republished because they contain environment identifiers and unrelated personal content.

No passing output is recorded unless execution actually succeeds. A controlled failing run is labeled as a deliberate regression. Completion state and evidence limits are recorded in [13-verification](../13-verification.md).

[03_render_output_panels.py](03_render_output_panels.py) reproduces the labeled SVG panels from the saved reference-run records using only the standard library. It is a rendering tool, not another verification run. See the image index for instructions.
