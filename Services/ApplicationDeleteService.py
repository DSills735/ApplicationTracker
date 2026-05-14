from Services import ApplicationViewService
import sqlite3
import Helpers

class ApplicationDeleteService:
    
    def DeleteApplication(self):
        Helpers.Helpers().Clear()

        appViewService = ApplicationViewService.ApplicationViewService()
        appViewService.ViewApplications()
        
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        
        app_id = int(input("Enter the ID of the application you want to delete: "))
            
        c.execute("DELETE FROM applications WHERE id = ?", (app_id,))   
        if c.rowcount == 0:
           print(f"No application found with ID {app_id}.")
        else:
           print(f"Application with ID {app_id} has been deleted.")

        conn.commit()
        conn.close()
           
        
