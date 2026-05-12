class MainMenu:
    def __init__(self):
        print("Welcome to the Main Menu!")

    def display_menu(self):
        print("Please select an option:")
        print("1. Add Application")
        print("2. View all Applications")
        print("3. View Open Applications")
        print("4. Update Application Status")
        print("5. Delete Application")
        print("6. Exit")

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice (1-6): ")
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    match choice:   
        case '1':
            add_application()

        case '2':
            view_all_applications()

        case '3':
            view_open_applications()

        case '4':
            update_application_status()

        case '5':
            delete_application()

        case '6':
            print("Exiting the application. Goodbye!")
            exit()
