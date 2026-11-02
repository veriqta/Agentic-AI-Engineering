# 00. Install Python on Ubuntu, Step by Step

## What you are installing

Python is the program that reads and executes the Python files you will write. vi is the text editor you will use to save those files. Installing an editor does not install Python, and creating a .py file does not execute it.

As checked on November 2, 2026, the latest stable Python release listed by Python.org is Python 3.15.2. This guide pins that exact version. It does not ask you to guess a version number or install an experimental prerelease. The [official release page](https://www.python.org/downloads/release/python-3152/) provides the download and checksum used below.

This installation route is for Ubuntu 24.04 LTS with internet access, a writable home directory and permission to install operating-system packages through sudo. Use a learning machine where you are authorized to install software. If you use an EC2 instance, connect through your existing authorized terminal session first. Do not paste passwords or private keys into a public issue or conversation.

Ubuntu's ordinary python3 package can be older than the latest Python.org release. Therefore this guide builds the pinned official source into your own home directory. The compiler performs the build; you do not need to know C to follow the installation. Allow additional setup time, potentially 20 to 60 minutes on a small instance. This installation is separate from the programming class.

## Before you begin

If python3 --version already reports Python 3.15.2 in your learning shell, you can keep that installation and go directly to the programming lab. Otherwise follow the numbered steps. A different version is not evidence that you ran the current-version setup.

A parent directory means a folder containing another folder. An archive is a compressed bundle of files. A compiler converts source into executable software; the build tools do that work for you. You are not expected to write C code.

Run each command separately. A successful command that returns no text is described as quiet below. If a command fails, investigate its actual error before proceeding to the next step.

## 1. Identify Ubuntu

cat reads a text file and displays its contents. /etc/os-release is the operating system's own identification file. It does not contain your Python source.

```bash
cat /etc/os-release
```

Expected result. Among the displayed lines, this guide expects ID=ubuntu and VERSION_ID="24.04". Other descriptive lines can differ. If you are on another distribution or release, do not assume this package list applies unchanged.

## 2. Refresh the package list

sudo runs this one command with administrative permission. apt is Ubuntu's package manager. update refreshes its list of available packages; it does not itself upgrade the whole operating system. Your terminal may request your own sudo password without displaying the typed characters. Many EC2 Ubuntu accounts do not request a password for authorized sudo commands.

```bash
sudo apt update
```

Expected result. Package index download/status lines followed by a successful return to the shell, commonly including Reading package lists... Done. Exact mirrors and counts vary. Stop for repository, DNS, certificate or permission errors rather than ignoring them.

## 3. Install the editor and build requirements

apt install obtains the named packages and their dependencies. -y accepts the package confirmation for this documented list. build-essential supplies the compiler and make. curl downloads the official archive, ca-certificates enables normal HTTPS certificate checks, xz-utils supports the archive format, and vim supplies a vi-compatible editor.

The development-library packages provide headers needed by Python components: SSL for secure connections, zlib/bzip2/lzma for compression, ffi for native interfaces, readline/ncurses for terminal interaction, SQLite for database support, uuid for identifiers and zstd for additional compression. pkg-config helps the build locate libraries. This is a headless terminal setup; a graphical Tk/IDLE environment is outside this class.

```bash
sudo apt install -y build-essential pkg-config curl ca-certificates xz-utils vim libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev liblzma-dev libncurses-dev uuid-dev libzstd-dev
```

Expected result. Installation progress, configuration messages or reports that some packages are already installed. It should finish without an error. Do not continue after an unable-to-locate-package or permission failure.

## 4. Create a download and build location

mkdir creates a directory. -p permits existing parents. ~ means your own home directory in this shell. This folder stores Python's installation sources, not the support project you will build afterward.

```bash
mkdir -p ~/python-build
```

Expected result. Normally quiet success. Existing contents are not removed.

cd enters that directory in this terminal session.

```bash
cd ~/python-build
```

Expected result. Normally quiet success. The next relative filename will be interpreted here.

pwd prints your current directory so you can confirm the location.

```bash
pwd
```

Expected shape. An absolute path ending in /python-build. The account-specific prefix depends on your machine.

## 5. Download the pinned official source

curl downloads the URL. --fail reports an HTTP failure as an error. --location follows an HTTPS redirect. --output names the local file. The URL identifies Python 3.15.2 on python.org. If this same archive name already exists and you want to retain it, rename or preserve it before downloading over it.

```bash
curl --fail --location --output Python-3.15.2.tar.xz https://www.python.org/ftp/python/3.15.2/Python-3.15.2.tar.xz
```

Expected result. Transfer progress and a saved file named Python-3.15.2.tar.xz, approximately 27 MB in decimal units. A failed download is not an installed interpreter. Do not disable certificate verification to make a download appear successful.

## 6. Verify the download before extraction

The hexadecimal value below is the archive's SHA-256 checksum from the official release page. printf writes a checksum-and-filename line. The pipe sends that line to sha256sum. --check compares the expected checksum with the actual file's bytes. The two spaces before the filename are intentional checksum-file syntax.

```bash
printf '%s\n' '8b5536d280142ecf6cdfe15d12a21ba1c65e300bbf7b28a8d0cdb849575797de  Python-3.15.2.tar.xz' | sha256sum --check
```

Expected result:

```text
Python-3.15.2.tar.xz: OK
```

If verification fails, stop. Do not extract or run the unverified download. Check the exact release, source URL, filename and completed transfer. The expected checksum must come from the trusted release page, not from the same untrusted file you are trying to check.

## 7. Extract the source directory

tar unpacks an archive. -x means extract and -f identifies the following archive filename. This writes a Python-3.15.2 directory in the current build location. If that directory already exists, choose a fresh build location before this command rather than extracting over earlier work.

```bash
tar -xf Python-3.15.2.tar.xz
```

Expected result. Normally quiet success and a new Python-3.15.2 directory. If that directory already exists, preserve prior work and use a separate build location instead of blindly replacing it.

Enter the extracted directory. This matters because ./configure in the next step is a file inside this directory.

```bash
cd Python-3.15.2
```

Expected result. Normally quiet success. Your current directory now ends in /python-build/Python-3.15.2.

## 8. Configure a private installation destination

./configure runs the configuration script in the current directory. The --prefix option chooses where the completed interpreter will be installed. $HOME expands to your home directory. Quotes keep the whole destination together as one argument. --with-ensurepip=install includes Python's standard pip bootstrap during installation.

```bash
./configure --prefix="$HOME/.local/python-3.15.2" --with-ensurepip=install
```

Expected result. Many checking... lines and generated build configuration. Read the final output for missing requirements. It must finish successfully before compilation. The installation destination is inside your account, not /usr/bin or Ubuntu's system-Python directory.

## 9. Build Python

make reads the generated build instructions and compiles Python. -j2 allows two build tasks at a time. This can take several minutes. If a small machine runs out of memory, rerun make -j1 after addressing the resource issue; fewer parallel tasks reduce memory pressure.

```bash
make -j2
```

Expected result. Compiler and module-build output, followed by successful return to the shell. A Killed message, make error or missing required extension is not a successful build. This terminal setup does not promise optional graphical modules such as tkinter.

## 10. Install into the configured home directory

make install copies the built files to the --prefix destination you selected. Do not add sudo here. With this explicit private prefix, the installation does not replace Ubuntu's files in /usr/bin. Omitting or changing the prefix would change that conclusion.

```bash
make install
```

Expected result. File-copy, link and pip-bootstrap messages followed by successful completion. It creates the private bin directory and interpreter commands there. The official Python documentation warns against overwriting a system python3, which is why this guide uses a separate account-owned destination.

## 11. Verify that exact executable

This path directly selects the interpreter you just installed. The quotes preserve the expanded path as one shell argument. --version asks it to report its version.

```bash
"$HOME/.local/python-3.15.2/bin/python3" --version
```

Expected result:

```text
Python 3.15.2
```

A failed command here means the installation has not been verified. Do not claim it succeeded because compilation printed many lines.

## 12. Select it for this learning session

PATH is the shell's ordered search list for executable commands. export makes the updated value available to commands started from this shell. The new bin directory comes first, while the existing $PATH is retained after it. This changes command selection for this session; it does not rename Ubuntu's system interpreter.

```bash
export PATH="$HOME/.local/python-3.15.2/bin:$PATH"
```

Expected result. Quiet success.

command -v reports which executable this shell will now select.

```bash
command -v python3
```

Expected shape. Your home directory followed by /.local/python-3.15.2/bin/python3.

Now verify the short command used throughout the class.

```bash
python3 --version
```

Expected result:

```text
Python 3.15.2
```

When you open a new terminal, repeat the export command before this class's Python commands, then verify the version again. This guide deliberately does not modify shell startup files automatically.

## 13. Verify pip and the editor

-m asks this interpreter to run a module. pip --version checks the package installer associated with this exact Python. You do not need to install any third-party project packages for Day 01.

```bash
python3 -m pip --version
```

Expected shape. A pip version, a path under the private installation and Python 3.15. The precise pip patch version can vary. A missing pip module needs investigation of the installation output.

vi --version checks the Vim-compatible editor installed above.

```bash
vi --version
```

Expected result. Vim version/build information. Other vi implementations can differ, but the vim package installed in this guide supplies the editor used here.

## Continue to the class

Return to the [guided lab](02-follow-along-lab.md). It creates a separate veriqta-day-01 project folder. Python's downloaded build sources do not belong inside that project. Keep installation, source editing and application execution as three distinct activities.

Official references: [release and checksum](https://www.python.org/downloads/release/python-3152/), [Python on Unix](https://docs.python.org/3.15/using/unix.html), [configuration options](https://docs.python.org/3.15/using/configure.html).
