from storage.json_repository import JsonRepository


def test_repository_load_and_save():
    repo = JsonRepository("data/test_db.json")

    data = repo.load_data()

    assert "users" in data
    assert "cars" in data
    assert "bookings" in data


def make_clean_repo():
    repo = JsonRepository()
    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": []
    })
    return repo