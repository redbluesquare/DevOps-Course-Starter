# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
$ cp .env.template .env.test  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Setup Trello

<a href="https://trello.com/signup" target="NEW_WINDOW">Create a Trello account</a> and <a href="https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#managing-your-api-key">API Key</a>

Once you have your Trello API key and secret, update the .env files with the variables.

TRELLO_API_KEY=API_KEY
TRELLO_API_TOKEN=API_TOKEN
TRELLO_API_OPEN_LIST=API_OPEN_LIST
TRELLO_API_CLOSED_LIST=API_CLOSED_LIST
TRELLO_API_BOARD=API_BOARD



## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


## Running the Test Suite
To execute the tests, please run the following command:
```bash
$ poetry run pytest
```

## Deploying the app to Ansilbe
To deploy the app to Ansible, copy the Ansible folder to your controlled node.
Update the inventory file [To include all the control nodes you'd like to deploy to.]

Setup SSH access from your control node to all your managed nodes

Then run the following command:
```bash
$ ansible-playbook playbook.yaml -i inventory.yaml
```

