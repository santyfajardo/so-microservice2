#import pytest
#from op_stats.app import app
#
#@pytest.fixture
#def client():
#  return app.test_client()
#
#def test_cpu_percent(client):
#  response = client.get('/v1/stats/cpu')
#  assert '{"cpu_percent":100}' in response.data.decode('utf-8')
#  assert response.status_code == 200
