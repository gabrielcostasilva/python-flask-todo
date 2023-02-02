# PYTHON FLASK TODO APP - DOCKER-PROD
This is a traditional Python 3 TODO app with [Flask framework](https://flask.palletsprojects.com). The original project is based on [Patrick Loeber's video](https://www.youtube.com/watch?v=3vfum74ggHE) analysing three Python frameworks for Web apps.

**This branch containerises the web application with Docker using [Gunicorn](https://docs.gunicorn.org/en/latest/index.html#).** Gunicorn is a Web server for Python applications. 

As a reference, we use [Patrick Loeber's video](https://www.youtube.com/watch?v=bi0cKgmRuiA) on containerising Python applications.

> If you want to understand the underlying application, please check out the [main branch](https://github.com/gabrielcostasilva/python-flask-todo.git).

## Overview
Unlike the [docker-dev branch](https://github.com/gabrielcostasilva/python-flask-todo/tree/docker-dev), this branch uses production server - Gunicorn. 

Apart from the dependency, there are little changes to the application and the Dockerfile. Please checkout the changes in the commit.

## Running the Project
First, ensure you have Docker desktop installed **and running**. 

Then: 
1. Build the image: `docker build -t flask-app .`
2. Run the container: `docker run -d -p 5000:5000`

Use your favorite browser to access the application at [`http://localhost:5000`](http://localhost:5000/).
