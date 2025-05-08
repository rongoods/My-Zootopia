import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv("API_NINJAS_KEY")

def fetch_animal_data(animal_name):
    response = requests.get(
        API_URL + animal_name,
        headers={"X-Api-Key": API_KEY}
    )
    response.raise_for_status()
    return response.json()

def build_animal_cards(animals):
    card_html = ""
    for animal in animals:
        name = animal.get("name", "Unknown")
        diet = animal.get("diet", "Unknown")
        location = animal.get("locations", ["Unknown"])[0]
        animal_type = animal.get("characteristics", {}).get("type", "Unknown")

        card_html += f"""
<li class="cards__item">
    <div class="card__title">{name}</div>
    <p class="card__text"><strong>Diet:</strong> {diet}</p>
    <p class="card__text"><strong>First Location:</strong> {location}</p>
    <p class="card__text"><strong>Type:</strong> {animal_type}</p>
</li>
"""
    return card_html

def generate_html_page(cards_html):
    with open("animals.html", "r") as f:
        template = f.read()

    updated_html = template.replace("<!-- ANIMAL_CARDS_PLACEHOLDER -->", cards_html)

    with open("animals.html", "w") as f:
        f.write(updated_html)

def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = fetch_animal_data(animal_name)
    cards_html = build_animal_cards(animals_data)
    generate_html_page(cards_html)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()

