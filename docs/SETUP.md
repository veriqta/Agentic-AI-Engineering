# Development Environment Setup

## Prerequisites

- Ubuntu or another supported Linux distribution
- Python version compatible with each lesson's pinned dependencies
- Git and an editor such as vi
- GitHub account

## Initial checks

```bash
python3 --version
git --version
```

## Clone and work

```bash
git clone https://github.com/veriqta/Agentic-AI-Engineering.git
cd Agentic-AI-Engineering
```

From the selected project's directory, create its own virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install dependencies from the project's documented, tested requirements. This scaffold has no executable project or pinned dependencies yet. Each published project must specify its tested Python version and dependency installation command. Never commit `.env`, credentials or `.venv`.
