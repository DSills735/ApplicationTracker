import ApplicationService

class MainMenu:
    def __init__(self):
        print("Welcome to the Main Menu!")

    def display_menu(self):
        print("\nPlease select an option:")
        print("1. Add Application")
        print("2. View all Applications")
        print("3. View Open Applications")
        print("4. Update Application Status")
        print("5. Delete Application")
        print("6. Exit")
        
        choice = self.get_user_choice()
        self.execute_choice(choice)

    def get_user_choice(self):
        while True:
            choice = input("Enter your choice (1-6): ")
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            print("Invalid choice. Please enter a number between 1 and 6.")

    def execute_choice(self, choice):
        match choice:
            case '1':
                appService = ApplicationService.ApplicationService()
                appService.add_application()
                
            case '2':
                self.view_all_applications()
            case '3':
                self.view_open_applications()
            case '4':
                self.update_application_status()
            case '5':
                self.delete_application()
            case '6':
                print("Exiting the application. Goodbye!")
                exit()

