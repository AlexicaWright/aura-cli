import pytest
from click.testing import CliRunner
from unittest.mock import Mock

from aura.tenants import get as get_tenant

def mock_response():
    mock_res = Mock()
    mock_res.status_code = 200
    mock_res.json.return_value = {"data": {'id': '123', 'name': 'Personal tenant'}}
    return mock_res


def test_get_tenant(api_request):
    runner = CliRunner()

    api_request.return_value = mock_response()

    result = runner.invoke(get_tenant, ["--tenant-id", "123"])
    
    assert result.exit_code == 0
    assert result.output == "{'id': '123', 'name': 'Personal tenant'}\n"

    api_request.assert_called_once_with(
        "GET", 
        "https://api.neo4j.io/v1beta3/tenants/123", 
        headers={"Content-Type": "application/json", "Authorization": f"Bearer dummy-token"}
    )
