
from flask import Flask
from flask_cors import CORS, cross_origin
import ijson
from pages.home import Home

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = 'Content-Type'


@app.route("/")
@cross_origin()
def home():
    return Home()

@app.route("/spells/<spell_name>")
@cross_origin()
def get_spell(spell_name):
    with open("spells.json", "r", encoding="utf8") as f:
        spells = ijson.items(f, "item")
        for i in spells:
            if i["name"].lower() == spell_name.lower():
                spell = {i["name"]: i["description"]}
                return spell, 200
        else:
            return "Spell Not Found", 404

@app.route("/spells/")
@cross_origin()
def spells():
    with open("spells.json", "r", encoding="utf8") as f:
        spells = ijson.items(f, "item")
        spellList = []
        for i in spells:
            spellList.append(i['name'])
        return spellList
    
@app.route("/classes/<class_name>")
@cross_origin()
def get_class(class_name):
    with open("classes.json", "r", encoding="utf8") as f:
        classes = ijson.items(f, "item")

        for i in classes:
            for n in i.keys():
                if n.lower() == class_name.lower():
                    return i[n]

@app.route("/classes/")
@cross_origin()
def classes_home():
    with open("classes.json", "r", encoding="utf8") as f:
        classes = ijson.items(f, "item")
        classlist = []
        for i in classes:
            for n in i.keys():
                classlist.append(n)
        return classlist
                
@app.route("/races/<race_name>")
@cross_origin()
def get_race(race_name):
    with open('races.json', "r", encoding="utf8") as f:
        races =  ijson.items(f, "item")
        print(races)
        for i in races:
            for n in i:
                if n.lower() == race_name.lower():
                    return i[n], 200
            else:
                return "Pick Dwarf, Elf, Haflfing, Human, DragonBorn, Gnome, Half-Elf, Half-Orc, or Tiefling"

@app.route("/races/")
@cross_origin()
def race_home():
    raceList = []
    with open('races.json', "r", encoding="utf8") as f:
        races = ijson.items(f, "item")
        for i in races:
            for n in i:
                raceList.append(n)
    return raceList

            

if __name__ == "__main__":
    app.run(debug=True)