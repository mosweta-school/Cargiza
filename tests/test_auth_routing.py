from services.auth_service import AuthService

def test_admin_role():
    service = AuthService()

    user = {
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    }

    assert service.get_route(user) == "admin_dashboard"


def test_customer_role():
    service = AuthService()

    user = {
        "username": "john",
        "password": "john123",
        "role": "customer"
    }

    assert service.get_route(user) == "customer_dashboard"