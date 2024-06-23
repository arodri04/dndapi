import json
import ijson

inpspell = "burning hands"
inpclass = "Paladin"



#with open("spells.json", "r", encoding="utf8") as f:
#    spells = ijson.items(f, "item")
#    print(spells)
#    for i in spells:
#        if inpspell.lower() == i["name"].lower():
#            print(i["name"])
#            print(i["description"])
#            
            
with open("classes.json", "r", encoding="utf8") as f:
    classes = ijson.items(f, "item")

    for i in classes:
        for n in i.keys():
            if n.lower() == inpclass.lower():
                print(i[n])