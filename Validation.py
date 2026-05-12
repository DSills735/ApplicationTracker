class Validation:

    def name_validation(self, name):
        if name is None or name.strip() == "":
            raise ValueError("Company name cannot be empty.")
        return False
     

