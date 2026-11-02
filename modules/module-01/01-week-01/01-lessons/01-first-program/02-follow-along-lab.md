# 02. Guided Follow-Along Lab

## 1. Understand what you are about to run

You will execute a program and distinguish a shell command from Python source. The input and output are simulated, so you can investigate safely without credentials or a payment provider.

## 2. Check Python and prepare your location

First ask Python to report its installed version. python3 selects the executable and --version requests a version report instead of running a script. Expect Python followed by your actual version number. This course uses Python 3.12 or later; the reference environment version is recorded with the weekly project. If the command is unavailable, stop and use the repository's environment setup guide rather than pretending the lab ran.

```bash
python3 --version
```


Choose a practice location you can write to. mkdir creates the named folder and -p allows it to exist already; it does not remove existing files. Then cd enters that folder. Run the commands in order, one at a time.

```bash
mkdir -p veriqta-week-01
cd veriqta-week-01
```

pwd prints your current directory. Expect an absolute path ending in veriqta-week-01; the earlier part depends on your machine. There is no universal expected home-directory path.

```bash
pwd
```

## 3. Open the file

Use vi to open first_agent.py in your current folder. If it already contains work, inspect it before deciding whether to edit.

```bash
vi first_agent.py
```

vi opens the named text file. Press i for insertion mode, enter the complete code below, press Esc, then type :wq and Enter to save and exit. If the parent directory does not exist, create or select it first. Do not put editor commands inside Python source. Use :q! only when you intentionally want to abandon unsaved edits.

## 4. Read and enter the complete implementation

```python
# Introductory Python execution example. No model or agent loop is used.
print("Welcome to Agentic AI Engineering")
```

Before running it, follow [the walkthrough](03-code-walkthrough.md). Identify the function name, its string argument and where the output goes. This first program contains no custom function definition or decision branch.

## 5. Execute and observe

Now start Python with the filename you saved. The interpreter reads that file and executes its print statement.

```bash
python3 first_agent.py
```

python3 starts the interpreter. The next path selects the file you saved. No extra arguments are needed for this milestone because the example values are in the source. The command runs locally and does not change real course access.

Expected output:

```text
Welcome to Agentic AI Engineering
```



## 6. Verify the milestone

Compare your actual result with the expected behavior. If it differs, record the command and first relevant error rather than pasting expected text into an evidence file. Explain which program runs and which statement produces the output.

## 7. Keep the result and continue

Keep the saved source and actual output. Attempt the knowledge check and practical assessment. The weekly project will integrate these milestones and add automated verification. A successful run is evidence about execution, not a substitute for understanding.
