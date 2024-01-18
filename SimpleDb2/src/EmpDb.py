from EmpDbEntry import EmpDbEntry
from tkinter import filedialog
import csv


class EmpDb:
    """
    - simple database to store EmpDbEntry objects
    """    

    def __init__(self, init=False, dbName='EmpDb.csv', importdbName='DbImport.csv', dbNameJSON='EmpDb.json'):
        """
        - initialize database variables here
        - mandatory :
            - any type can be used to store database entries for EmpDbEntry objects
            - e.g. list of class, list of dictionary, list of tuples, dictionary of tuples etc.
        """
        # CSV filename 
        self.dbName = dbName
        self.importdbName = importdbName
        self.dbNameJSON = dbNameJSON
        # initialize container of database entries 
        self.dbEntries = []
        print('TODO: __init__')


    def fetch_employees(self):
        """
        - returns a list of tuples containing Employee entry fields
        - example
          [('123', 'Brian Baker', 'SW-Engineer', 'Male', 'On-Site'),
           ('124', 'Eileen Dover', 'SW-Engineer', 'Male', 'On-Site'),
           ('125', 'Ann Chovey', 'SW-Engineer', 'Male', 'On-Site')]
        """
        tupleList = []
        print('TODO: fetch_orders')
        for entry in self.dbEntries:
            tupleList.append((entry.id, entry.name, entry.role, entry.gender, entry.status))
        return tupleList

    def insert_employee(self, id, name, role, gender, status):
        """
        - inserts an entry in the database
        - no return value
        """
        newEntry = EmpDbEntry(id=id, name=name, role=role, gender=gender, status=status)
        self.dbEntries.append(newEntry)
        print('TODO: insert_order')

    def delete_employee(self, id):
        """
        - deletes the corresponding entry in the database as specified by 'id'
        - no return value
        """
        print('TODO: delete_order')
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                self.dbEntries.remove(entry)


    def update_employee(self, new_name, new_role, new_gender, new_status, id):
        """
        - updates the corresponding entry in the database as specified by 'id'
        - no return value
        """
        print('TODO: update_order')
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                entry.name = new_name
                entry.role = new_role
                entry.gender = new_gender
                entry.status = new_status

    def export_csv(self):
        """
        - exports database entries as a CSV file
        - CSV : Comma Separated Values
        - no return value
        - example
        12,Eileen Dover,SW-Engineer,Male,On-Site
        13,Ann Chovey,HW-Engineer,Female,On-Site
        14,Chris P. Bacon,SW-Engineer,Male,On-Leave
        15,Russell Sprout,SW-Engineer,Male,Remote
        16,Oscar Lott,Project-Manager,Male,On-Site        
        """
        print('TODO: export_csv')
        with open(self.dbName, "w") as file:
            for entry in self.dbEntries:
                file.write(f"{entry.id},{entry.name},{entry.role},{entry.gender},{entry.status} \n")

    def import_csv(self):
        print('TODO: import_csv')
        self.dbEntries.clear()
        fld = filedialog.askopenfilename(title="Open CSV", filetypes = (('CSV File', '*.csv'), ("All Files", "*.*")))
        with open(fld) as file:
            csv_reader = csv.reader(file, delimiter=",")
            for row in csv_reader:
                newId = row[0]
                newName = row[1]
                newRole = row[2]
                newGender = float(row[3])
                newStatus = row[4]
                self.insert_employee(newId, newName, newRole, newGender, newStatus)
                

    def export_json(self):
        print('TODO: export_json')
        with open(self.dbNameJSON, "w") as file:
            for entry in self.dbEntries:
                file.write(f"{entry.id},{entry.name},{entry.role},{entry.gender},{entry.status} \n")


    def id_exists(self, id):
        """
        - returns True if an entry exists for the specified 'id'
        - else returns False
        """
        for entry in self.dbEntries:
            if getattr(entry, "id") == id:
                return True
        else:
            return False
        
    
