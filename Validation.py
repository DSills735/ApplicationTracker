import MainMenu 
import Helpers

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
     

