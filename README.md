# PYTHON FLASK TODO APP - UNIT-TEST BRANCH
This is a traditional Python 3 TODO app with [Flask framework](https://flask.palletsprojects.com). This project is based on [Patrick Loeber's video](https://www.youtube.com/watch?v=3vfum74ggHE) analysing three Python frameworks for Web apps.

This branch adds unit tests with [Pytest](https://docs.pytest.org).

> If you want to understand the underlying application, please check out the [main branch](https://github.com/gabrielcostasilva/python-flask-todo.git).

## Overview
Adding unit tests with Pytest requires three steps, as detailed below:

1. Install dependency with `pip install pytest`
2. Create the [`tests` folder](./tests/) to group unit tests. Notice this folder has an empty `__init__.py` file to enable importing Python modules.
3. Create the [`conftest.py` file](./tests/conftest.py). This is a configuration file. It basically sets the test client.
4. Create unit tests. In this project, all our tests are in the [`test_application.py` file](./tests/test_application.py).

### Unit tests
Both the file and the tests start with `test_`. It seems this is a requirement. 

If you are familiar with software testing, each tests consists of one or more _assertions_.

The code below shows the full test for testing the DB model. The code imports the `Todo` model from the application, and checks whether the attribute is set as expected - unnecessary, but I am just practicing.

```python
from application import Todo

def test_model():
    a_todo = Todo(title="To wash car", complete=False)
    assert a_todo.complete == False
```

All other tests in the `test_application` file uses the test client to access the **running** application. Therefore, they receive the test client as a parameter.

```python
(...)

def test_page_load(client):

(...)
```

The test client provides features for accessing the application and evaluating its response. The code snippet below examplify three features. The snippet sends a `POST` request to the `/add` route, with the `data` content, following all redirects till reach the final response (`follow_redirects=True`).

```python
(...)

response = client.post("/add", 
            data={"title": "To learn pytest"}, 
            follow_redirects=True)

(...)
```

Once the `response` is populated, one can check whether a text is part of it (`b"<label>Todo Title</label>" in response.data`) or the status code matches the expectation (`response.status_code == 200`).

## Testing the Project
With the application running, just run `pytest` from your terminal. 

> Be aware that the tests reach out the DB!

## Additional References

- [Testing Flask Applications](https://flask.palletsprojects.com/en/2.2.x/testing/) is a guide from the official Flask docs. It helped to understand how to use the test client.
- [Testing Flask Applications with Pytest](https://testdriven.io/blog/flask-pytest/) shows how to test DB models, and clarify a typical testing directory structure.
- [How to add a basic unit test to a Python Flask app using Pytest](https://medium.com/globant/how-to-add-a-basic-unit-test-to-a-python-flask-app-using-pytest-79e61da76fc2) explains the use of fixtures for a simple Flask structure, such as the one used in this project. 