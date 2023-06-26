import json

from src.api import crud


def test_create_project(test_app, monkeypatch):
    test_request_project = {
        "project_name": 'Düsseldorf',
        "district": "40549",
        "version": "20230608",
    }
    test_response_project = {
        "id": 1,
        "project_name": 'Düsseldorf',
        "district": "40549",
        "version": "20230608",
    }
    
    monkeypatch.setattr(crud, "post_project", lambda x: 1)

    response = test_app.post("/projects/", content=json.dumps(test_request_project))

    assert response.status_code == 201
    assert response.json() == test_response_project


def test_create_project_invalid_json(test_app):
    response = test_app.post("/projects/", content=json.dumps({"title": "wrong"}))
    assert response.status_code == 422


def test_read_project(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "project_name": 'Düsseldorf',
        "district": "40549",
        "version": "20230608",
    }

    monkeypatch.setattr(crud, 'get_project', lambda x: test_data)

    response = test_app.get("/projects/1")
    print(response)
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_project_incorrect_id(test_app, monkeypatch):
    monkeypatch.setattr(crud, 'get_project', lambda x: None)

    response = test_app.get("/projects/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_read_all_projects(test_app, monkeypatch):
    test_data = [
        {"id": 1, "project_name": 'Düsseldorf', "district": "40549", "version": "20230608"},
        {"id": 2, "project_name": 'Duisburg', "district": "30549", "version": "20230608"}
    ]

    monkeypatch.setattr(crud, "get_all_projects", lambda : test_data)

    response = test_app.get("/projects/")
    assert response.status_code == 200
    assert response.json() == test_data