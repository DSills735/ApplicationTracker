import sqlite3
import pandas as pd

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
            
        df = pd.DataFrame(applications, columns=['ID', 'Company', 'Date Applied', 'Status if Known', 'Position', 'Notes'])
        
        print("\n=== CURRENT JOB APPLICATIONS ===")

        print(df.to_markdown(tablefmt="grid", index=False))
        print(f"Total Applications: {len(df)}\n")
