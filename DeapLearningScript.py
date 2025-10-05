from math import e
import os
import random
import json
import spacy
from spacy.training import Example

# ------------------------------
# Recovering data
# ------------------------------

TRAIN_DATA = []
label_map = {
    "Agent Name": "AGENT_NAME",
    "Agent Id code": "AGENT_ID_CODE",
    "Agent Adresse": "AGENT_ADDRESS",
    "Agent Email": "AGENT_EMAIL",
    "Agent Phone": "AGENT_PHONE",
    "Nice Class": "NICE_CLASS",
    "Nature": "NATURE",
    "Traditional": "TRADITIONAL"
}

for file in os.listdir("data/form"):
    if file.endswith(".json") and file.startswith("form_label"):
        with open(os.path.join("data/form", file), "r", encoding="utf-8") as f:
            data = json.load(f)
            text = " \n ".join([f"{k}: {v}" for k, v in data.items()])
            entities = []
            for k, v in data.items():
                start = text.find(str(v))
                if start != -1:
                    end = start + len(str(v))
                    label = k.upper().replace(" ", "_")
                    entities.append((start, end, label))
                TRAIN_DATA.append((text, {"entities": entities}))

def filter_overlapping(entities):
    entities = sorted(entities, key=lambda x: x[0])
    filtered = []
    last_end = -1
    for start, end, label in entities:
        if start >= last_end:
            filtered.append((start, end, label))
            last_end = end
    return filtered

for text, ann in TRAIN_DATA:
    ann["entities"] = filter_overlapping(ann["entities"])

print(f"✅ {len(TRAIN_DATA)} Exemple generated for spacy.")

# ------------------------------
# Training spacy NER
# ------------------------------

nlp = spacy.load("./model_forms")
ner = nlp.get_pipe("ner")

for label in label_map.values():
    ner.add_label(label)

optimizer = nlp.resume_training()
for itn in range(200):  # epochs
    losses = {}
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.2, losses=losses)
    print(f"Iteration {itn} - Losses: {losses}")

# ------------------------------
# Saving model
# ------------------------------

nlp.to_disk("model_formsV2")
print("✅ Spacy model saved")