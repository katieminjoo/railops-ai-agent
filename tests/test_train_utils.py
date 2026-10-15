from app.train_utils import get_train_status
import pytest

@pytest.mark.parametrize(
        "scheduled, estimated, cancelled, expected",
        [
            ("15:45","On time", False, "on_time"),
            ("15:45", "15:52", False, "delayed"),
            ("15:45", "Cancelled", False, "cancelled")
        ]
)

def test_train_status(scheduled, estimated, cancelled, expected) :
    result = get_train_status(scheduled, estimated, cancelled)
    assert result == expected

def test_cancelled_train():
    result = get_train_status ("15:45", "On time", True)

    assert result == "cancelled"
    # assert result == "on_time"

def test_delayed_train():
    result = get_train_status("15:45", "15:52", False)
    assert result == "delayed"