from unittest.mock import patch, Mock
from app.rail_data import get_trains
import requests

def test_get_trains_with_mock():
    fake_data = {
        "trainServices" :[
            {
                "destination":[
                    {"locationName" : "London Waterloo"}
                ],
                "sta" : "15:45",
                "eta" : "15:52",
                "platform" : "2",
                "isCancelled" : False
            }
        ]
    }
    fake_response = Mock()
    fake_response.json.return_value = fake_data

    with patch("app.rail_data.requests.get") as mock_get:
        mock_get.return_value = fake_response

        result = get_trains("WOK", "London Waterloo")

        assert result[0]["delay_minutes"] == 7.0
        assert result[0]["status"] == "delayed"
        mock_get.assert_called_once()


def test_get_trains_connection_error():
    with patch("app.rail_data.requests.get") as mock_get :
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")
        result = get_trains("WOK", "London Waterloo")

        assert result == {"error" : "Failed to retrieve train data"}

def test_get_trains_empty_services():
    fake_response = Mock()
    fake_response.json.return_value = {"trainServices" : []}

    with patch("app.rail_data.requests.get") as mock_get:
        mock_get.return_value = fake_response

        result = get_trains("WOK", "London Waterloo")

        assert result == []