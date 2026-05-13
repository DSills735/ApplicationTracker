import Validation

class ApplicationService:
    
    def add_application(self):
       
        def welcome_message(self):
            print("Welcome to the application creator menu. If at any point you wish to exit, press 0.\n")
        valid = False
        welcome_message(self)

        company = input("Enter the company name: ")

        while(not valid):
            valid = Validation.Validation().name_validation(company)
            if not valid:
                company = input("Enter the company name: ")
        
        valid = False
        date_applied = input("Enter the date applied (YYYY-MM-DD): ")

        status_if_known = input("Enter the application status (if known): ")
        position = input("Enter the position applied for: ")
        notes = input("Enter any additional notes: ")
        application = Application(company, date_applied, status_if_known, position, notes)
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("INSERT INTO applications (company, date_applied, status_if_known, position, notes) VALUES (?, ?, ?, ?, ?)",
                  (application.company, application.date_applied, application.status_if_known, application.position, application.notes))
        conn.commit()
        conn.close()


        def welcome_message(self):
            print("Welcome to the application creator menu. If at any point you wish to exit, press 0.")