import json
import pytest
from flask_app import app


def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Testing Flask"

# @pytest.mark.get_request
def test_get_all_books():
    response = app.test_client().get('/bookapi/books')
    res = json.loads(response.data.decode("utf-8")).get("Books")
    assert res[0]['author'] == 'Miguel Grinberg'
    assert res[1]['author'] == 'Tony Gaddis'
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert type(res[1]) is dict


# @pytest.mark.get_request
def test_get_book_by_id():
    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode("utf-8")).get("Book")
    print(res)
    assert res['id'] == 1
    assert res['author'] == 'Miguel Grinberg'
    assert res['title'] == "Flask Web Development"
    assert response.status_code == 200