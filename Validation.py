import MainMenu 
import Helpers
from datetime import datetime 
class Validation:

    def name_validation(self, name):
        if name is None or name.strip() == "":
            print("Company name cannot be empty.")
            return False
        elif name == "0":
            print("Exiting the application creator menu. Returning to main menu.")
            Helpers.Helpers().Clear()
            MainMenu.MainMenu().display_menu()
            return True
        return True
     
    def date_validation(self, date_str):
        if date_str == "0":
            print("Exiting the application creator menu. Returning to main menu.")
            Helpers.Helpers().Clear()
            MainMenu.MainMenu().display_menu()
            return True
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            return False

