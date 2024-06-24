from flask import Flask, request, jsonify
import ijson
app = Flask(__name__)


@app.route("/")
def home():
    return "Home"

@app.route("/spells/<spell_name>")
def get_spell(spell_name):
    with open("DND\spells.json", "r", encoding="utf8") as f:
        spells = ijson.items(f, "item")
        for i in spells:
            if i["name"].lower() == spell_name.lower():
                spell = {i["name"]: i["description"]}
                return spell, 200
        else:
            return "Spell Not Found", 404

@app.route("/classes/<class_name>")
def get_class(class_name):
    with open("DND\classes.json", "r", encoding="utf8") as f:
        classes = ijson.items(f, "item")

        for i in classes:
            for n in i.keys():
                if n.lower() == class_name.lower():
                    return i[n]

            

if __name__ == "__main__":
    app.run(debug=True)