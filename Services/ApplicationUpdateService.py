from email.mime import application
import sqlite3
from turtle import update
import Helpers

from Services.ApplicationViewService import ApplicationViewService

class ApplicationUpdateService:
    validInput = True
    def UpdateApplication(self):
        Helpers.Helpers().Clear()
        ApplicationViewService().ViewOpenApplications()
        num = input("\n\nPlease enter the ID of the application to update: ")

        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT * FROM applications WHERE id = ?", (num,))

        print ("\n\nPlease select the field to update:")
        print("1. Company")
        print ("2. Date Applied")
        print ("3. Status if Known")
        print ("4. Position")
        print ("5. Notes")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            new_company = input("Enter the new company name: ")
            c.execute("UPDATE applications SET company = ? WHERE id = ?", (new_company, num))

        elif choice == '2':
            new_date_applied = input("Enter the new date applied (DD-MM-YYYY): ")
            c.execute("UPDATE applications SET date_applied = ? WHERE id = ?", (new_date_applied, num))

        elif choice == '3':
            new_status = input("Enter the new status (if known): ")
            c.execute("UPDATE applications SET status_if_known = ? WHERE id = ?", (new_status, num))

        elif choice == '4':
            new_position = input("Enter the new position: ")
            c.execute("UPDATE applications SET position = ? WHERE id = ?", (new_position, num))

        elif choice == '5':
            new_notes = input("Enter the new notes: ")
            c.execute("UPDATE applications SET notes = ? WHERE id = ?", (new_notes, num))

        else:
            print("Invalid choice. Please try again.")
            self.validInput = False

        conn.commit()
        conn.close()

    if not validInput:
        UpdateApplication();






