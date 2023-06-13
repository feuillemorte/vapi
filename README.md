# What is it

> WARNING! DO NOT USE THIS API ON PRODUCTION, THIS API CONTAINS VULNERABILITIES!

VAPI - Vulnerable API - is a project that aims to be used for RapiDAST e2e test, to make sure RapiDAST works as expected during development.

It is a small vulnerable API (oops, it's no more API only since it contain a frontend part), which you can use to test some security issues.

Currently there is an SQL injection in place. **Here's a challenge for you! Where is it? :)**

# How to run


1. Create a python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Update pip:
```bash
pip install -U pip
```
3. Install project requirements:
```bash
pip install -r requirements.txt
```
4. Run the project using the bash script:

Note: by default the frontend refers to the backend API endpoints on 127.0.0.1:5000. This will cause errors when accessing the frontend via the external IP. In this case, set the API_HOST environment variable to the external IP first.

```bash
bash ./start.sh
```

## Podman/Docker

### Build an image
```bash
$ podman build . -t local-vapi
```

### Run example

The port 3000 is used for frontend and 5000 is used for backend. The env var API_HOST needs to be set for backend to be accessble through the frontend.

```bash
$ podman run -it --rm -p 3000:3000 -p 5000:5000 -e API_HOST=192.168.1.115:5000 local-vapi
```

# Development
## Setting the development environment
1. Create a python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
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
