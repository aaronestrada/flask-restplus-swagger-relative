import pytest
from tests.test_application import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_hello_resource(client):
    """
    Test if it is possible to access to /hello resource
    :param client: Test client object
    :return:
    """
    response = client.get('/hello').get_json()
    assert response['hello'] == 'world'


def test_asset_found(client):
    """
    Test if Swagger assets are accessible from the new path
    :param client: Test client object
    :return:
    """
    response = client.get('/this_is_a_new/path_for_swagger/swaggerui/swagger-ui-bundle.js')
    assert response.status_code is 200
