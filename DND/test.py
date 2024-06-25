import json
import ijson

inpspell = "burning hands"
inpclass = "Paladin"
inprace = "Dwarf"


# with open("DND\spells.json", "r", encoding="utf8") as f:
#    spells = ijson.items(f, "item")
#    print(spells)
#    for i in spells:
#        if inpspell.lower() == i["name"].lower():
#            print(i["name"])
#            print(i["description"])
           
            
# with open("DND\classes.json", "r", encoding="utf8") as f:
#     classes = ijson.items(f, "item")

#     for i in classes:
#         for n in i.keys():
#             if n.lower() == inpclass.lower():
#                 print(i[n])

with open('DND/races.json', "r", encoding="utf8") as f:
    races =  ijson.items(f, "item")
    print(races)
    for i in races:
        for n in i:
            if n == inprace:
                print(i[n])