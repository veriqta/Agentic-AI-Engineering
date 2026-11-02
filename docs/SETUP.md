# Set Up Your Development Environment

You need a Linux terminal, Python 3.12 or later and an editor such as vi for Week 01. Ubuntu is the reference platform. The project uses Python's standard library, so you do not need API keys, a cloud subscription or third-party packages. Check your installed environment rather than assuming a version from a screenshot applies to your machine.

## 1. Check Python

python3 selects the interpreter. --version asks it to display its version and exit without running a script.

```bash
python3 --version
```

Expect Python followed by your actual version. If the command is unavailable, install a supported Python through your operating system's documented process before attempting the lab. Do not replace Ubuntu's system interpreter or change system symlinks to match a tutorial. Seek version-specific setup guidance if your environment needs installation.

## 2. Choose how to obtain the course

You can read the classroom on GitHub and enter the complete examples into your practice folder. If you want a local copy, check that Git is installed. git selects the version-control program and --version displays its installed version.

```bash
git --version
```

The clone command below downloads the public repository and its history into a new Agentic-AI-Engineering directory under your current location. You do not need write access to read a public clone. Choose a location where that directory does not already exist.

```bash
git clone https://github.com/veriqta/Agentic-AI-Engineering.git
```

cd changes your shell's current directory. Enter the downloaded course before using repository-relative paths.

```bash
cd Agentic-AI-Engineering
```

Network failures, missing Git and an existing destination are different problems. Read the actual message before retrying. Never delete an existing working directory merely because clone reports that the destination exists.

## 3. Begin Week 01

Open [Week 01](../modules/module-01/01-week-01/README.md) and read the numbered lessons. Lesson 01 explains practice folders, paths, vi and your first execution. After completing the milestones, you can run the reference project from its own directory. The following cd path is relative to the repository root you entered above.

```bash
cd modules/module-01/01-week-01/02-weekly-project
```

The [project lab](../modules/module-01/01-week-01/02-weekly-project/02-follow-along-project.md) explains its application and test commands before execution. Keep practice changes and evidence separate from reference material when possible.

## 4. Understand environments before adding dependencies

Week 01 requires no pip installation. Later projects will document their tested dependencies and isolation requirements. A Python virtual environment keeps a project's packages separate from system packages; it is not a separate operating system or a security sandbox. Creating and activating one will be taught when dependency management becomes part of the application. Never commit .venv, .env files, access tokens or private keys.

## 5. Know where your commands run

A terminal connected over SSH runs commands on the remote machine. A local terminal runs them on your current computer. Files and installed packages belong to that environment. Before debugging a missing file or package, confirm that you are using the intended session. Public evidence should omit host identifiers, credentials and unnecessary personal information.
