from application import Todo

def test_model():
    a_todo = Todo(title="To wash car", complete=False)
    assert a_todo.complete == False

def test_page_load(client):
    response = client.get("/")
    assert b"<label>Todo Title</label>" in response.data

def test_create_todo(client):
    response = client.post("/add", data={
        "title": "To learn pytest"
    }, follow_redirects=True)
    assert response.status_code == 200

def test_update_todo(client):
    response = client.get("/update/1", follow_redirects=True)
    assert b'<span class="ui green label">Completed</span>' in response.data

def test_delete_todo(client):
    response = client.get("/delete/2", follow_redirects=True)
    assert response.status_code == 200
