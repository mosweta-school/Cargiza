from cli.auth_cli import AuthCLI
from cli.admin_cli import AdminCLI
from cli.customer_cli import CustomerCLI


def main():
    auth_cli = AuthCLI()

    while True:

        print("\n======================")
        print("      CARGIZA         ")
        print("======================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            user = auth_cli.show_login()

            if user:
                route_user(user)

        elif choice == "2":
            auth_cli.show_register()

        elif choice == "3":
            print("Goodbye!")
            break


def route_user(user):
    if user["role"] == "admin":
        admin_cli = AdminCLI(user)
        admin_cli.run()

    elif user["role"] == "customer":
        customer_cli = CustomerCLI(user)
        customer_cli.run()


if __name__ == "__main__":
    main()