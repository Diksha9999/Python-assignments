class Contact:
    def __init__(self,name,ph,email):
        self.name=name
        self.ph=ph
        self.email=email


    def get_name(self):
        return self.name

    def get_ph(self):
        return f'{self.ph}'
    def get_email(self):
        return f'{self.email}'

obj=Contact("diksha",909,'yahoo.com')

print(obj.get_name())
print(obj.get_ph())
print(obj.get_email())

