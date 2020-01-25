
contacts = {1:{'name':'diksha','ph':'9909099090','email':'123@gmail.com'},
            2:{'name':'isha','ph':'9900987654','email':'isha@gmail.com'},
            3:{'name': 'priyanka', 'ph': '9900987654', 'email': 'shethecarbongirl.com'},
            }



def fetch_details(ph):
    print(f'\ndetails of employee {ph}')
    for key, value in contacts[ph].items():
        print(f'{key}: {value}')


fetch_details(1)


class dict(contacts):
    def __init__(self):
        self=contacts()
    def add(self,key,value):
        self[key]=value

obj=dict()
obj.add(3:'neha')

