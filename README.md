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


## Running the Test Suite natively
To execute the tests, please run the following command:
```bash
$ poetry run pytest
```
The tests can also be triggered using Github Actions once activated in your repository using a Docker container. Please check the Docker section if you would like to test via Docker

## Deploying the app to Ansilbe
To deploy the app to Ansible, copy the Ansible folder to your controlled node.
Update the inventory file [To include all the control nodes you'd like to deploy to.]

Setup SSH access from your control node to all your managed nodes

Then run the following command:
```bash
$ ansible-playbook playbook.yaml -i inventory.yaml
```

# Running the app via Docker
To build, test and run the app using Docker use the following commands below

Development
```bash
$ docker build --target development --tag todo-app:dev .
$ docker run --env-file ./.env -p 5100:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

Test
```bash
$ docker build --target test --tag todo-app:test .
$ docker run todo-app:test
```

Production
```bash
$ docker build --target production --tag todo-app:prod .
$ docker run --env-file ./.env -p 5100:5000 todo-app:prod
```

# Running the app via Azure App Service
To run the app using Azure App Service use the following commands below

Login to Docker Hub using your login details via the terminal
```bash
$ docker login
```

Next, build your app and push it to Docker Hub. Here you could build the development, test or production version.<br>
`Hint:`Your `<image-tag>` should include your username, e.g.: `<username>/todo-app:prod`
```bash
$ docker build --target <my_build_phase> --tag <image-tag> .
$ docker push <image-tag>
```

Next, create a App Service Plan in Azure

```azure
$ az appservice plan create --resource-group <resource_group_name> -n <appservice_plan_name> --sku B1 --is-linux
```

<p>Then, create a App Service in Azure</p>

```azure
$ az webapp create --resource-group <resource_group_name> --plan <appservice_plan_name> --name <webapp_name> --deployment-container-image-name docker.io/<dockerhub_username>/<container-image-name>:latest
```

<p>Via the App portal, enter all of the environment variables</p>
Portal:<br>
<ul><li>Settings -> Configuration in the Portal</li>
<li>Add all the environment variables as “New application setting”</li>
<li>Add an entry for the website port to expose:  WEBSITES_PORT=5000</li>
</ul>

The app should be available if you browse to: `http://<webapp_name>.azurewebsites.net/`