def printer(arg):
    n = 0
    if (arg == 'M'):
        for i in datastore['office']['medical']:
            print(n, ".", i)
            n = n + 1
    if (arg == 'P'):

        for i, j in datastore['office']['parking'].items():
            print(n, ".", i, ":", j)
            n = n + 1


def add(arg):
    if (arg == 'M'):
        datastore['office']["medical"].append(
            {"room-number": input("enter room number : "), "use": input("Enter use of room : "),
             "sq-ft": input("Enter sq-ft :"), "price": input("Enter price :")})
        n = 0
        printer(arg)
    if (arg == 'P'):
        datastore['office']['parking'][input("enter key: ")] = input("Enter value :")
        n = 0
        printer(arg)


def update(arg):
    if (arg == 'M'):
        choice = int(
            input("Enter 1 to change whole list or enter 2 to change a particular value-key pair of any List : "))
        if (choice == 1):
            printer(arg)
            i = int(input("enter field to change : "))
            datastore['office']["medical"][i] = {"room-number": input("enter room number : "),
                                                 "use": input("Enter use of room : "), "sq-ft": input("Enter sq-ft :"),
                                                 "price": input("Enter price :")}
            n = 0
            printer(arg)

        if (choice == 2):
            printer(arg)
            i = int(input("enter field to change : "))
            k, j = map(str, input("enter key and value to update : ").split(" "))
            datastore['office']["medical"][i][k] = j
            n = 0
            printer(arg)

    if (arg == 'P'):
        n = 0
        select = int(
            input("Enter 1 to change whole list or enter 2 to change a particular value-key pair of any List :"))
        if (select == 1):
            printer(arg)
            for x in datastore['office']['parking']:
                val = input("enter value of  {0} : ".format(x))
                datastore['office']['parking'][x] = val
            n = 0
            printer(arg)

        if (select == 2):
            printer(arg)
            k, j = map(str, input("enter key and value to update : ").split(" "))
            datastore['office']["parking"][k] = j

            n = 0
            printer(arg)


def delete(arg):
    n = 0
    if (arg == 'M'):
        choice = int(
            input("Enter 1 to Delete whole list or enter 2 to Delete a particular value-key pair of any List : "))
        if (choice == 1):
            printer(arg)
            i = int(input("enter field to delete : "))
            del (datastore['office']['medical'][i])
            n = 0
            printer(arg)

        if (choice == 2):
            n = 0
            for i in datastore['office']['medical']:
                print(n, ".", i)
                n = n + 1
            i = int(input("enter field to delete : "))
            k = input("enter key to delete : ")
            del (datastore['office']['medical'][i][k])

            printer(arg)

    if (arg == 'P'):
        select = int(
            input("Enter 1 to delete whole list or enter 2 to delete a particular value-key pair of any List :"))
        if (select == 1):
            datastore['office']['parking'].clear()

            print(datastore['office']['parking'])

        if (select == 2):
            printer(arg)
            k = input("enter key to delete : ")
            del (datastore['office']["parking"][k])
            printer(arg)


def main():
    while (True):
        print("1.ADD")
        print("2.UPDATE")
        print("3.DELETE")
        print("4.Exit")
        ch = int(input("Enter your choice : "))
        if (ch == 1):
            print("Medical or parking-> ")
            c = input("Where you want to add : ")
            add(c)
        if (ch == 2):
            print("Medical or parking-> ")
            c = input("Where you want to update : ")
            update(c)
        if (ch == 3):
            print("Medical or parking-> ")
            c = input("Where you want to Delete : ")
            delete(c)
        if (ch == 4):
            exit()


main()