import pytest
from src import app  # Import the Flask instance directly from your app module


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client
        


def test_home(client):
    """Test the home route."""
    
    expected = """<h1> Flask Crud APP</h1>
                <p> A flask rest api implementation using Docker Container. </p>
            """
 
    
    response = client.get('/')
    
    assert response.status_code == 200
    
    assert expected == response.get_data(as_text=True)
    
 