dagen = [
    "maandag",
    "dinsdag",
    "woensdag",
    "donderdag",
    "vrijdag",
    "zaterdag",
    "zondag"
]

x = 1

i = int(input('kies een dag\n1 = maandag \n2 = dinsdag \n3 = woensdag \n4 = donderdag \n5 = vrijdag \n6 = zaterdag \n7 = zondag\n'))

while x <= i:
    print(dagen[x-1])
    x += 1
