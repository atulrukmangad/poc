import spacy
import re

def extract_info(prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(prompt)

    # Extracting name
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON" or ent.label == 'ORG':
            name = ent.text
            break

    # Extracting age
    age = None
    for token in doc:
        if token.like_num:
            if token.i+1 < len(doc) and doc[token.i+1].text == "years":
                age = int(token.text)
                break
            if token.i+1 == len(doc):
                age = int(token.text)
                break

    # Extracting location
    location = None
    for ent in doc.ents:
        if ent.label_ == "GPE":
            location = ent.text
            break

    # Extracting insurance product
    insurance_product = None
    for token in doc:
        if token.text.lower() in ["health", "life", "car", "home"]:
            insurance_product = token.text.lower()
            break

    return name, age, location, insurance_product

def extract_age(prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(prompt)

    # Extracting age
    age = None
    for token in doc:
        if token.like_num:
            if token.i+1 < len(doc) and doc[token.i+1].text == "years":
                age = int(token.text)
                break
    return age

def extract_name(prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(prompt)

    # Extracting name
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON" or ent.label == 'ORG':
            name = ent.text
            break
    return name

def extract_product(prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(prompt)

    # Extracting insurance product
    insurance_product = None
    for token in doc:
        if token.text.lower() in ["health", "life", "car", "home"]:
            insurance_product = token.text.lower()
            break
    return insurance_product

def extract_location(prompt):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(prompt)

    # Extracting location
    location = None
    for ent in doc.ents:
        if ent.label_ == "GPE":
            location = ent.text
            break
    return location



def extract_cardetails(prompt):
    nlp = spacy.load("en_core_web_sm")
    # Define regular expressions to match car make and year
    make_pattern = re.compile(r"(?i)(Honda|Toyota|Ford|Chevrolet|Nissan|BMW|Audi|Mercedes|Volkswagen)")
    year_pattern = re.compile(r"\b(19|20)\d{2}\b")

    # Process the text with spaCy
    doc = nlp(prompt)

    # Initialize variables for car make, model, and year
    make = None
    model = None
    year = None

    # Iterate over each token in the processed document
    for token in doc:
        # Check if the token matches the make pattern
        if make_pattern.search(token.text):
            make = token.text
        # Check if the token matches the year pattern
        elif year_pattern.search(token.text):
            year = token.text
        # Check if the token is a car model (assuming it follows the car make)
        elif make is not None and model is None:
            model = token.text

    # Return the extracted car information as a dictionary
    return make, model, year
