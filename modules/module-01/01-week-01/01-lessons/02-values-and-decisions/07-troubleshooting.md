# 07. Troubleshooting

| Symptom | What to inspect | Correction and verification |
|---|---|---|
| python3 unavailable | Check the environment where your shell runs | Use approved installation setup, then check python3 --version |
| File not found | Inspect pwd, filename and relative path | Select the correct directory, then rerun the intended command |
| Syntax or indentation error | Read the indicated source line and preceding line | Compare the complete code, correct structure and rerun |
| Editor commands appear in source | Check whether you left vi insertion mode | Remove accidental text; press Esc before :wq |
| Unexpected message | Trace input and selected branch | Compare the behavior with the lesson contract, not only the expected words |
| Test loading failure | Check PYTHONPATH and the documented project directory | Run the supplied suite command from the project root |

Record expected behavior, actual behavior, the first relevant error, your suspected cause, inspected code, correction and rerun result. A failure is information to investigate, not a reason to invent a passing record. Do not use root privileges, delete existing work or install unrelated packages to bypass a path or source mistake.
