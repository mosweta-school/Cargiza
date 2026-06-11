from cli.auth_cli import AuthCLI
from cli.customer_cli import CustomerCLI
from storage.json_repository import JsonRepository


def test_login_flow():
    repo = JsonRepository()

    repo.save_data({
        "users": [{
            "id": 1,
            "username": "john",
            "password": "$2b$12$FwXJnPSCl4FJHjOyuqlX8.VNeaDeHG.6ARi0S6Abz3WceZREPEg5u",  # assume hashed
            "role": "customer"
        }],
        "cars": [],
        "bookings": []
    })

    auth = AuthCLI(repo)

    result = auth.show_login("john", "john12345")

    assert result["role"] == "customer"