from app.train_utils import get_train_status

def test_cancelled_train():
    result = get_train_status ("15:45", "On time", True)

    assert result == "cancelled"