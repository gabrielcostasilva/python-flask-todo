# PYTHON FLASK TODO APP - DOCKER-DEV
This is a traditional Python 3 TODO app with [Flask framework](https://flask.palletsprojects.com). This project is based on [Patrick Loeber's video](https://www.youtube.com/watch?v=3vfum74ggHE) analysing three Python frameworks for Web apps.

**This branch containerises the web application with Docker.**

> If you want to understand the underlying application, please check out the [main branch](https://github.com/gabrielcostasilva/python-flask-todo.git).

## Overview
Wrapping the application into a Docker container requires two steps:

1. Adding the host configuration to the [`application.py` file](./application.py), like so: `app.run(host="0.0.0.0")`
2. Creating the [`Dockerfile`](./Dockerfile).

In addition, we removed the `.ebextensions` folder, previously used for deploying with AWS Beanstalk.

> Please notice this examples uses a dev server, not a production one!

## Running the Project
First, ensure you have Docker desktop installed **and running**. 

Then: 
1. Build the image: `docker build -t flask-app .`
2. Run the container: `docker run -d -p 5000:5000`

Use your favorite browser to access the application at [`http://localhost:5000`](http://localhost:5000/).

## Additional References
- [Using docker platform branch](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker.html) shows how to deploy it using AWS Beanstalk
- [How To Containerize Python Applications](https://www.youtube.com/watch?v=bi0cKgmRuiA) teaches how to set a production-ready container.