# What is it

> WARNING! DO NOT USE THIS API ON PRODUCTION, THIS API CONTAINS VULNERABILITIES!

It's just a small vulnerable API, which you can use to test some security issues.

Currently there is an SQL injection in place.

# How to run
1. Create a python virtual environment
2. Update pip:
```bash
pip install -U pip
```
3. Install project requirements:
```bash
pip install -r requirements.txt
```
4. Run the project using the bash script:
```bash
bash ./start.sh
```

# Development
## Setting the development environment
1. Create a python virtual environment
2. Update pip:
```bash
pip install -U pip
```
3. Install project requirements:
```bash
pip install -r requirements-dev.txt
```
4. Run the project using the bash script:
```bash
bash ./start.sh
```

## Running integration tests
1. Ensure the API is not running
2. Run pytest tests from the project root:
```bash
pytest
```

## Before git commit
Please, run the pre-commit before commiting to your branch and fix all notifications:
```
git add .
pre-commit
```
