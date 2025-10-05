from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from faker import Faker
from PIL import Image
import os
import json
import random

# Crée le dossier si inexistant
os.makedirs("data/form", exist_ok=True)

# Faker pour données françaises
fake = Faker("en_GB")

# Champs possibles
FIELDS = ["Agent Name", "Agent Id code", "Agent Adresse", "Agent Email", "Agent Phone", "Nice Class", "Nature", "Traditional"]
IMAGE_PATH ="wipo-logo1-scaled.png"

img = Image.open(IMAGE_PATH)
img_width, img_height = img.size
page_width, page_height = A4

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os

# Assume IMAGE_PATH exists
img = Image.open(IMAGE_PATH)
img_width, img_height = img.size

page_width, page_height = A4  # dimensions A4 in points

def create_random_form_label_random_order(filename):
    random.shuffle(FIELDS)
    c = canvas.Canvas(filename, pagesize=A4)

    # Dessiner l'image en haut
    if os.path.exists(IMAGE_PATH):
        draw_width = img_width * 0.75
        draw_height = img_height * 0.75
        x = (page_width - draw_width) / 2
        y = page_height - draw_height
        c.drawImage(IMAGE_PATH, x, y, width=draw_width, height=draw_height)

    # Positions verticales, descendantes
    y_start = page_height - draw_height - 50
    y_positions = list(range(int(y_start), int(y_start) - len(FIELDS)*30, -30))

    # Générer les valeurs pour chaque champ
    field_values = {}
    for field in FIELDS:
        if field == "Agent Name":
            value = fake.last_name() + " " + fake.first_name()
        elif field == "Agent Id code":
            value = str(random.randint(1, 100000))
        elif field == "Agent Adresse":
            value = fake.address().replace("\n", ", ")
        elif field == "Agent Email":
            value = fake.email()
        elif field == "Agent Phone":
            value = fake.phone_number()
        elif field == "Nice Class":
            value = str(random.randint(1, 35))
        elif field == "Nature":
            value = random.choice(["Word", "Figurative", "Word and Figurative"])
        elif field == "Traditional":
            value = random.choice(["Traditional", "Non-traditional"])
        field_values[field] = value

    x = 60

    # Dessiner les champs et les valeurs dans l'ordre original
    for y, field in zip(y_positions, FIELDS):
        c.rect(x, y-2, 300, 18, stroke=1, fill=0)
        c.drawString(x, y, f"{field} : {field_values[field]}")

    c.save()
    return field_values

def create_random_form_nolabel_random_order(filename):
    random.shuffle(FIELDS)
    c = canvas.Canvas(filename, pagesize=A4)

    # Dessiner l'image en haut
    if os.path.exists(IMAGE_PATH):
        draw_width = img_width * 0.75
        draw_height = img_height * 0.75
        x = (page_width - draw_width) / 2
        y = page_height - draw_height
        c.drawImage(IMAGE_PATH, x, y, width=draw_width, height=draw_height)

    # Positions verticales, descendantes
    y_start = page_height - draw_height - 50
    y_positions = list(range(int(y_start), int(y_start) - len(FIELDS)*30, -30))
    i=0

    # Générer les valeurs pour chaque champ
    field_values = {}
    for field in FIELDS:
        if field == "Agent Name":
            value = fake.last_name() + " " + fake.first_name()
        elif field == "Agent Id code":
            value = str(random.randint(1, 100000))
        elif field == "Agent Adresse":
            value = fake.address().replace("\n", ", ")
        elif field == "Agent Email":
            value = fake.email()
        elif field == "Agent Phone":
            value = fake.phone_number()
        elif field == "Nice Class":
            value = str(random.randint(1, 35))
        elif field == "Nature":
            value = random.choice(["Word", "Figurative", "Word and Figurative"])
        elif field == "Traditional":
            value = random.choice(["Traditional", "Non-traditional"])
        field_values[field] = value

    x = 60 

    # Dessiner les champs et les valeurs dans l'ordre original
    for y, field in zip(y_positions, FIELDS):
        c.rect(x, y-2, 300, 18, stroke=1, fill=0)
        c.drawString(x, y, f"{field_values[field]}")

    c.save()

    json_data = list(field_values.values())

    return json_data


# Générer plusieurs formulaires
NUM_FORMS_LABEL = 750
NUM_FORMS_NO_LABEL = 250
 
for i in range(NUM_FORMS_NO_LABEL):
    pdf_name = f"data/form/form_nolabel_{i+1}.pdf"
    json_data = create_random_form_nolabel_random_order(pdf_name)

    # sauvegarder le JSON correspondant
    json_name = pdf_name.replace(".pdf", ".json")
    with open(json_name, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"{NUM_FORMS_NO_LABEL} formulaires generes no label dans le dossier data/")

for i in range(NUM_FORMS_LABEL):
    pdf_name = f"data/form/form_label_{i+1}.pdf"
    labels = create_random_form_label_random_order(pdf_name)

    # sauvegarder le JSON correspondant
    json_name = pdf_name.replace(".pdf", ".json")
    with open(json_name, "w", encoding="utf-8") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)

print(f"{NUM_FORMS_LABEL} formulaires label generes dans le dossier data/")