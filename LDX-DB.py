# LDOS X DB
# run ldx-db.py

class entry:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        try:
            self.intage=int(age)
        except Exception:
            self.intage=0
        self.job=job
    def printData(self):
        if not "!!" in self.age:
            print(f"""Name: {self.name}\nAge: {self.age} years old\nJob: {self.job}""")
        else:
            print(f"""Name: {self.name}\nAge: {self.age[2:len(self.age)]}\nJob: {self.job}""")
        
default=entry("L-DOS X DB","!!!2022","Database program for L-DOS X.")
database=[default]

while True:
    choice=input("Press N for a new person.\nPress V to view a person. \nPress A to view a summary of all entries.\nPress E to edit an entry.\nPress X to exit.\nChoice: ").lower()
    if choice=="n":
        database.append(entry(input("Name: "),input("Age: "),input("Job: ")))
    if choice=="v":
        pid=input("Person ID: ")
        try:
            print(database[int(pid)].printData())
        except IndexError or TypeError:
            print("That person does not exist.")
    if choice=="a":
        for i in range(len(database)):
            print(f"{i}: {database[i].name}")
    if choice=="e":
        pid=input("Person ID: ")
        choice=input("Press N to edit the name, A to edit the age, or J to edit the job.").lower()
        try:
            if choice=="n":
                database[int(pid)].name=input("New data: ")
            if choice=="a":
                database[int(pid)].age=input("New data: ")
            if choice=="j":
                database[int(pid)].job=input("New data: ")
            else:
                print("Invalid choice entered.")
        except IndexError or TypeError:
            print("An error occured.")
    if choice=="x":
        print("Closing L-DOS X DB.")
        break
