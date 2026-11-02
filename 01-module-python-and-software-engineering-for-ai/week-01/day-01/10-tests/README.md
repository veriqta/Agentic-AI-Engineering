# 10. Automated Checks

[test_day01.py](test_day01.py) contains three process-level execution tests: welcome output, complete briefing behavior and briefing execution from another working directory.

Read [Testing and verification](../05-testing-and-verification.md) for the complete implementation, explained command and expected results. From the day-01 directory, python3 -m unittest discover -s 10-tests -v runs the built-in runner. No third-party dependency or special import-path setting is required.

The tests inspect actual stdout, stderr and exit status. Each child process has a 10-second timeout. Passing establishes the checked local behavior; it does not demonstrate external payment verification or individual understanding.
