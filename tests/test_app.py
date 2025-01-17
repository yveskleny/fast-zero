from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_hello_word(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_hello_world_deve_retornar_hello_world_html(client):
    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Hello World </h1>' in response.text
