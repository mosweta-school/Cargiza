from services.auth_service import AuthService
from storage.json_repository import JsonRepository
from storage.fake_json_repository import FakeRepository

def make_clean_repo():
    repo = JsonRepository("data/test_db.json")
    repo.save_data({
        "users": [],
        "cars": [],
        "bookings": []
    })
    return repo


def test_register_and_login():
    repo = FakeRepository()
    auth = AuthService(repo)

    user = auth.register("testuser", "1234", "customer")

    assert user["username"] == "testuser"

    logged_in = auth.login("testuser", "1234")

    assert logged_in is not None
    assert logged_in["username"] == "testuser"

def test_duplicate_user_registration():
    auth = AuthService()

    auth.register("testuser", "1234", "customer")

    result = auth.register("testuser", "9999", "customer")

    assert "error" in result
def test_login_failure_wrong_password():
    auth = AuthService()

    auth.register("testuser", "1234", "customer")

    result = auth.login("testuser", "wrongpass")

    assert result is None or "error" in result

def test_password_is_hashed():
    auth = AuthService()

    # reset DB (VERY IMPORTANT)
    auth.repo.save_data({"users": [], "cars": [], "bookings": []})

    user = auth.register("testuser", "1234", "customer")

    assert user["password"] != "1234"

    assert user["password"] != "1234"

def test_duplicate_user_error():
    auth = AuthService()
    auth.repo.save_data({"users": [], "cars": [], "bookings": []})

    auth.register("john", "1234", "customer")
    result = auth.register("john", "9999", "customer")

    assert "error" in result