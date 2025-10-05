import os
import json
import spacy

# ------------------------------
# Testing modele
# ------------------------------

nlp2 = spacy.load("model_forms")

for file in os.listdir("data/formtest"):
    if file.endswith(".json"):
        with open(os.path.join("data/formtest", file), "r", encoding="utf-8") as f:
            data = json.load(f)
            text_testing = " \n ".join([str(v) for v in data])

        doc = nlp2(text_testing)
        print("\n🔎 Resulte :")
        for ent in doc.ents:
            print(ent.text, ent.label_)
