import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_NINJAS_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_animal_data(animal_name):
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(API_URL + animal_name, headers=headers)
    response.raise_for_status()
    return response.json()


def build_animal_cards(animals):
    cards = ""

    for animal in animals:
        name = animal.get("name", "Unknown")
        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        location = animal.get("locations", ["Unknown"])[0]
        animal_type = animal.get("characteristics", {}).get("type")

        cards += f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <p class="card__text"><strong>Diet:</strong> {diet}</p>
            <p class="card__text"><strong>First Location:</strong> {location}</p>"""

        if animal_type:
            cards += f'<p class="card__text"><strong>Type:</strong> {animal_type}</p>'

        cards += "</li>\n"

    return cards


def generate_html_page(content_html, animal_name):
    with open("animals.html", "w") as file:
        file.write(f"""
<html>
    <head>
        <style>
        html {{
          background-color: #ffe9e9;
        }}
        h1 {{
            text-align: center;
            font-size: 40pt;
            font-weight: normal;
        }}
        body {{
          font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
          padding: 1rem;
          width: 900px;
          margin: auto;
        }}
        .cards {{
          list-style: none;
          margin: 0;
          padding: 0;
        }}
        .cards__item {{
          background-color: white;
          border-radius: 0.25rem;
          box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
          padding: 1rem;
          margin: 50px;
        }}
        .card__title {{
          color: #696969;
          font-size: 1.25rem;
          font-weight: 300;
          letter-spacing: 2px;
          text-transform: uppercase;
        }}
        .card__text {{
          font-size: 0.95rem;
          line-height: 2;
          margin-bottom: 1.25rem;
        }}
        </style>
    </head>
    <body>
        <h1>Results for "{animal_name}"</h1>
        <ul class="cards">
        {content_html}
        </ul>
    </body>
</html>
""")


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    try:
        animals = fetch_animal_data(animal_name)

        if animals:
            cards_html = build_animal_cards(animals)
        else:
            cards_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

        generate_html_page(cards_html, animal_name)
        print("Website was successfully generated to the file animals.html.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
