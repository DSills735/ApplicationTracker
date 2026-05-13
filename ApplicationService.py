import Validation
import Helpers
import Main
import sqlite3

class ApplicationService:
    
    def add_application(self):
       
        def welcome_message(self):
            print("Welcome to the application creator menu. If at any point you wish to exit, press 0.\n")
        valid = False
        welcome_message(self)

        company = input("Enter the company name: ")

        while(not valid):
            valid = Validation.Validation().string_validation(company)
            if not valid:
                company = input("Enter the company name: ")
        
        valid = False
        Helpers.Helpers().Clear()
        date_applied = input("Enter the date applied (YYYY-MM-DD): ")

        while (not valid):
            valid = Validation.Validation().date_validation(date_applied)
            if not valid:
                date_applied = input("Enter the date applied (YYYY-MM-DD): ")

        valid = False
        Helpers.Helpers().Clear()


        status_if_known = input("Enter the application status (if known): ")

        while (not valid):
                valid = Validation.Validation().string_validation(status_if_known)
                if not valid:
                    status_if_known = input("Enter the application status (if known): ")
        valid = False
        Helpers.Helpers().Clear()

        position = input("Enter the position applied for: ")

        while(not valid):
            valid = Validation.Validation().string_validation(position)
            if not valid:
                position = input("Enter the position applied for: ")
        valid = False
        Helpers.Helpers().Clear()

        notes = input("Enter any additional notes: ")
        while(not valid):
            valid = Validation.Validation().string_validation(notes)
            if not valid:
                notes = input("Enter any additional notes: ")

        Helpers.Helpers().Clear()

        application = Main.Main().Application(company, date_applied, status_if_known, position, notes)
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("INSERT INTO applications (company, date_applied, status_if_known, position, notes) VALUES (?, ?, ?, ?, ?)",
                  (application.company, application.date_applied, application.status_if_known, application.position, application.notes))
        conn.commit()
        conn.close()

        print("Application added successfully!")

        def welcome_message(self):
            print("Welcome to the application creator menu. If at any point you wish to exit, press 0.")