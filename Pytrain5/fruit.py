a = {'fruit': [
    {"name": "Apple", "biological name": "Malus Domestica", "major_producers": ["China", "United States", "Turkey"],
     "nutrition": {"carbohydartes": "13.81g", "fat": "0.17g", "protein": "0.26g"}},
    {"name": "Orange", "biological name": "Citrus x sinensis", "major_producers": ["China", "United States", "India"],
     "nutrition": {"carbohydartes": "11.75g", "fat": "0.12g", "protein": "0.94g"}}],
     }
p = []
p1 = []
for i in range(len(a['fruit'])):
    p.append((a['fruit'][i]['nutrition']['protein'], a['fruit'][i]['name']))

for i in range(len(a['fruit'])):
    for b in range(i + 1):
        if ((a['fruit'][i]["major_producers"][b]) == "China"):
            p1.append((a['fruit'][i]['nutrition']['protein'], a['fruit'][i]['name']))

p = max(p)
p1 = max(p1)
print("Name of Fruit: {1} Highest protein value is: {0}".format(p[0], p[1]))
print("Name of Fruit : {0} Highest protein value in China is : {1}".format(p1[1], p1[0]))