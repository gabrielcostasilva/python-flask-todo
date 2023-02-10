# PYTHON FLASK TODO APP - MYSQL
This is a traditional Python 3 TODO app with [Flask framework](https://flask.palletsprojects.com). This project is based on [Patrick Loeber's video](https://www.youtube.com/watch?v=3vfum74ggHE) analysing three Python frameworks for Web apps.

**This branch replaces SQLLite with MySQL DB.** 

> If you want to understand the underlying application, please check out the [main branch](https://github.com/gabrielcostasilva/python-flask-todo.git).

## Overview
There are two main differences between this and the main branch. First, we add [PyMySQL](https://pypi.org/project/PyMySQL/) to the [requirements.txt](./requirements.txt) file. PyMySQL is a MySQL client for Python. 

Second, we changed application.py to consider MySQL URL and retrieve necessary data from environment variables, like so:

```python
(...)

import os

(...)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(
	os.getenv("RDS_USERNAME"),
	os.getenv("RDS_PASSWORD"),
	os.getenv("RDS_HOSTNAME"),
	os.getenv("RDS_DB_NAME"),
)

(...)
```

## Running the Project Locally
1. Clone the project locally

```
git clone https://github.com/gabrielcostasilva/python-flask-todo.git
```

2. In the project folder, create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate

```

3. Install dependencies

```
pip install -r requiments.txt
```

4. Create four environment variables with required data for accessing the MySQL DB as follows

```
export RDS_USERNAME=USERNAME-TO-ACCESS-DB
export RDS_PASSWORD=PASSWD-TO-ACCESS-DB
export RDS_HOSTNAME=LOCALHOST
export RDS_DB_NAME=DB-NAME
```

5. Start the application

```
python3 application.py
```

6. Access the app with your browser at [`http://localhost:5000`](http://localhost:5000)

## Running the Project on AWS Elastic Beanstalk
First, ensure you have [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) and [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) installed and configured.

1. Clone the project locally

```
git clone https://github.com/gabrielcostasilva/python-flask-todo.git
```

2. In the project folder, initilize the application 

```
eb init \
    -r us-east-1 \
    -p python-3.8
```

3. Create your Beanstalk environment 

```
eb create -s -db.engine mysql
```

4. When the environment is ready, access the app

```
eb open
```

5. Terminate your environment 
```
eb terminate
```

> Note that you can use a MySQL client (e.g. Workbench) to access your database on AWS RDS using the connection URL presented on your console during the environment creation.