people={1:{'name':'John','age':'27','sex':'Male'},2:{'name':'Marie','age':'22','sex':'female'}}
print(people)


print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])

people[3]={}
people[3]['name']='Luna'
people[3]['age']='25'
people[3]['sex']='male'
people[3]['married']='no'
print(people[3])


people={1:{'name':'John','age':'27','sex':'Male'},2:{'name':'Marie','age':'22','sex':'female'},3:{'name':'Luna','age':'24','sex':'female','married':'no'},4:{'name':'Peter','age':'29','sex':'Male','married':'no'}}

del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])

people={1:{'name':'John','age':'27','sex':'Male'},2:{'name':'Marie','age':'22','sex':'female'}}
for p_id,p_info in people.items():
    print("\nPerson ID",p_id)
    for key in p_info:
        print(key+':',p_info[key])


matrix=[]
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

#Nested list comprehension
matrix=[[j for j in range(5)] for i in range(5)]
print(matrix)



#flatter a given 2d list i.e convert 2d list into 1d
matrix=[[1,2,3],[4,5,6],[7,8,9,10,11]]
flatten_matrix=[]
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)

print(flatten_matrix)


#nested list comprehnsion to flatten of 2d matrix
flatten_matrix=[val for sublist in matrix for val in sublist]
print(flatten_matrix)


planets=[['Mercury','Venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','pluto']]
flatten_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(flatten_planets)


Indian_batsman={1:{'batsman':'Dhoni','type':'right hand','matches':'one day','avg':'50','score':'500','runs':'40'},2:{'batsman':'virat','type':'left hand','matches':'one day','avg':'20','score':'200','runs':'30'}}

print(Indian_batsman[1]['batsman'])







'''
squad={'Batsmen':{Rhohit :{'matches':206,'runs':800,'avg':55.6},'shikhar':{'matches':296,'runs':90,'avg':32.6},'virat':{'matches':196,'runs':100,'avg':33.6}}}
df=pd.DataFrame(squad['Batsmen'])
print(df)
'''



squad={'Batsmen':{'Rhohit' :{'matches':206,'runs':800,'avg':55.6},'shikhar':{'matches':296,'runs':90,'avg':32.6},'virat':{'matches':196,'runs':100,'avg':33.6}}}
print(squad['Batsmen']['virat']['avg'])

'''
fruits={
    'fruit info ':
        {{
    'name':'mango',
    'bionomical name':'Malus Domestica',
    'major producer':["china","us","turkey"],
    'nutrition': {"carbohydrate":13.7,"Fat":0.17,"protein":0.26}
    },

    {
    'name':'mango',
    'bionomical name':'Malus Domestica',
    'major producer':["nepal","india","turkey"],
    'nutrition': {"carbohydrate":32.7,"Fat":0.10,"protein":0.6}
    },

    {
    'name':'apple',
    'bionomical name':'Malus Domestica',
    'major producer':["UK","china","turkey"],
    'nutrition': {"carbohydrate":43.0,"Fat":0.15,"protein":3.26}
    }}
}
print(fruits)
'''

def get_info(x):
    G=datastore.get("x",{})
    print(G)


datastore={"office":{"medical":[
    {"room-num":100,"use":"reception","sq-ft":50,"price":75},
    {"room-num":101,"use":"waiting","sq-ft":250,"price":75},
    {"room-num":102,"use":"examination","sq-ft":125,"price":150},
    {"room-num":103,"use":"examination","sq-ft":125,"price":150},
    {"room-num":104,"use":"office","sq-ft":150,"price":100}],
"parking":{"location":"premium","style":"covered","price":750}}}

print(datastore)

v=datastore.get("office", {})
a=datastore.get("office", {}).get("medical", {})
b=datastore.get("parking",{}).get("parking", {})
print(b)

G=input('enter room no.')
get_info(G)














