import sqlite3
import MainMenu


class Application:
      def __init__(self, company, date_applied, status_if_known, position, notes):
           self.company = company
           self.date_applied = date_applied
           self.status_if_known = status_if_known
           self.position = position
           self.notes = notes

def init_db():
    conn = sqlite3.connect('applications.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            company TEXT, 
            date_applied TEXT, 
            status_if_known TEXT, 
            position TEXT, 
            notes TEXT
        )
    """)
    #c.execute("CREATE TABLE IF NOT EXISTS ClosedApplications( company TEXT, position TEXT, notes TEXT)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    menu = MainMenu.MainMenu()
    menu.display_menu()

