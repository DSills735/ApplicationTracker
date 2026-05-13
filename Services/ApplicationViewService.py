import sqlite3
import pandas as pd
import Helpers

class ApplicationViewService:
    def ViewApplications(self, open = False):
        Helpers.Helpers().Clear()
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT * FROM applications")
        applications = c.fetchall()
        conn.close()
        
        if not applications:
            print("No applications found.")
            return
            
        df = pd.DataFrame(applications, columns=['ID', 'Company', 'Date Applied', 'Status if Known', 'Position', 'Notes'])
        
        print("\n=== CURRENT JOB APPLICATIONS ===")

        print(df.to_markdown(tablefmt="grid", index=False))
        print(f"Total Applications: {len(df)}\n")

        if (open):
            print("Press Enter to return to the main menu.")
            input()


    def ViewOpenApplications(self, open = False):
        Helpers.Helpers().Clear()
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        c.execute("SELECT * FROM applications WHERE status_if_known != 'Declined' AND status_if_known != 'Closed' AND status_if_known != 'Ghosted'")
        applications = c.fetchall()
        conn.close()
        
        if not applications:
            print("No open applications found.")
            return
            
        df = pd.DataFrame(applications, columns=['ID', 'Company', 'Date Applied', 'Status if Known', 'Position', 'Notes'])
        
        print("\n=== OPEN JOB APPLICATIONS ===")
        print(df.to_markdown(tablefmt="grid", index=False))
        print(f"Total Open Applications: {len(df)}\n")

        if (open):
            print("Press Enter to return to the main menu.")
            input()
