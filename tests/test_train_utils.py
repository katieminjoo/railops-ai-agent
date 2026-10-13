from app.train_utils import get_train_status

def test_cancelled_train():
    result = get_train_status ("15:45", "On time", True)

    assert result == "cancelled"
    # assert result == "on_time"

def test_delayed_train():
    result = get_train_status("15:45", "15:52", False)
    assert result == "delayed"