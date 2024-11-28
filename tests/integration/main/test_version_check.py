"""
Test routes for version control
"""
# pylint: disable=redefined-outer-name,unused-argument

def test_version_control_route(client):
    """
    Test that version route exists.
    """
    response = client.get("/version")
    assert response.status_code == 200
    assert b"Current version!" in response.data
    
