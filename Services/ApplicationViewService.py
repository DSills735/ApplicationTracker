import sqlite3

class ApplicationViewService:
    
    def ViewApplications(self):
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT * FROM applications")
        applications = c.fetchall()
        conn.close()
        if not applications:
            print("No applications found.")
            return
        print("\nAll Applications:")
        for app in applications:
            print(f"Company: {app[0]}, Date Applied: {app[1]}, Status: {app[2]}, Position: {app[3]}, Notes: {app[4]}")