
import os.path, pickle

'''
This is a database module that stores objects like dictionaries
into appropriate files which act as databases to store and retrive
information. This makes use of a builtin python module called as
'Pickle'. The database files are stored with an extension .dat
'''

class database:
    # Initiation: Creates a new db if that file is not found
    #             opens the old db if found
    def __init__(self, name=""):
        self.status = False
        if len(name) > 0 and not self.open(name):
            self.create(name)
            
    # Opens database with provided name
    def open(self,name):
        if os.path.isfile(name+".dat") and not self.status:
            self.name = name
            file = open(name+".dat", 'rb')
            self.data = pickle.load(file)
            file.close()
            self.status = True
            return True
        else:
            return False
            
    # Creates a new database
    def create(self,name):
        if os.path.isfile(name+".dat") or self.status:
            return False
        else:
            data = {}
            file = open(name+".dat", 'wb')
            pickle.dump(data, file)
            file.close()
            self.open(name)
            
    # Rewrites current self.data into database
    @property
    def save(self):
        if self.status:
            file = open(self.name+".dat", 'wb')
            pickle.dump(self.data, file)
            file.close()
            return True
        else:
            return False
        
    # Adds a column to the database, if some entries are already
    # made in other columns this new column has 'None' in those
    # entries
    def addColumn(self,name):
        if name in self.data.keys():
            return False
        self.data[name] = []
        if len(self.data) > 1:
            othername = name
            i = 0
            while othername == name:
                othername = self.data.keys()[i]
                i+=1
            for _ in self.data[othername]:
                self.data[name].append(None)
        self.save
        return True
    
    # Inserts into respective places. Takes a dictionary with appropriate
    # keys with names of columns containing the value to be inserted into
    # that paerticular column
    def insert(self,dat):
        if len(set(dat.keys()).intersection(self.data.keys())) == len(dat.keys()):
            for i in dat:
                self.data[i].append(dat[i])
            self.save
            return True
        else:
            return False
    
    # Gets the row by a value in row
    def get(self,key,value):
        res = []
        if key in self.data.keys():
            for i in range(len(self.data[key])):
                if self.data[key][i] == value:
                    dat = {}
                    for j in self.data.keys():
                        dat[j] = self.data[j][i]
                    res.append(dat)
            return res
        else:
            return False
            
    # Delete a row by value
    def delete(self,key,value):
        if key in self.data.keys():
            var = True
            while var:
                var = False
                for i in range(len(self.data[key])):
                    if self.data[key][i] == value:
                        for j in self.data.keys():
                            self.data[j].pop(i)
                        var = True
                        break
            self.save
            return True
        else:
            return False
    
    # Returns a list of columns
    @property
    def columns(self):
        return self.data.keys()
    
    # Changes a value by finding another value
    def change(self, key, value, key2, value2):
        if key in self.data.keys():
            var = True
            while var:
                var = False
                for i in range(len(self.data[key])):
                    if self.data[key][i] == value and self.data[key2][i] != value2:
                        self.data[key2][i] = value2
                        var = True
                        break
            self.save
            return True
        else:
            return False
            
    # Returns all rows as a list of rows as dictionaries
    @property
    def rows(self):
        res = []
        for i in range(len(self.data[self.data.keys()[0]])):
            dat = {}
            for j in self.data.keys():
                dat[j] = self.data[j][i]
            res.append(dat)
        return res

# Test cases
'''
if __name__ == "__main__":
    db = database("people")
    db.addColumn("name")
    db.addColumn("rn")
    db.insert({"name":"vinaya","rn":1})
    db.insert({"name":"vinayb","rn":2})
    db.insert({"name":"vinayc","rn":3})
    db.insert({"name":"vinayd","rn":4})
    db.insert({"name":"vinaye","rn":4})
    print db.data
    print db.addColumn("shape")
    print db.data
    print db.change("rn",4,"shape","triangle")
    print db.data
    print db.get("rn",4)
    print db.data
    print db.rows
    print db.columns
    print db.delete("rn",4)
    print db.data
'''