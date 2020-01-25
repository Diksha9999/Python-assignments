def get_info(x):
    A=datastore['office'].get(x,{})
    print(A)

'''
def delete_info(A):
    del datastore['office']['medical'][A]
    print(A)
'''


datastore={"office":{"medical":[
    {"room-num":100,"use":"reception","sq-ft":50,"price":75},
    {"room-num":101,"use":"waiting","sq-ft":250,"price":75},
    {"room-num":102,"use":"examination","sq-ft":125,"price":150},
    {"room-num":103,"use":"examination","sq-ft":125,"price":150},
    {"room-num":104,"use":"office","sq-ft":150,"price":100}],
"parking":{"location":"premium","style":"covered","price":750}}}




A=input('enter info of dept:')
get_info(A)



