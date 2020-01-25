import pickle

dict1 = {0: "Asthaa"}


class Contact:
    def __init__(self, name, phonenumber, emailaddress):
        self.name = name
        self.phonenumber = phonenumber
        self.emailaddress = emailaddress

    def setEmail(self, email):
        self.emailaddress = email

    def setPhone(self, phone):
        self.phonenumber = phone

    def setName(self, name):
        self.name = name

    def getEmail(self):
        return self.emailaddress

    def getName(self):
        return self.name

    def getPhone():
        return self.phonenumber

    def __str__(self):
        return "Name : " + self.name + " ,Email : " + self.emailaddress + " ,Phone-Number : " + self.phonenumber


with open('dict1', 'rb') as a:
    dict1 = pickle.load(a)