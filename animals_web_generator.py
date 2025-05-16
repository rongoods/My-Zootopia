import data_fetcher

def generate_html_page(content_html):
    html_content = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #ffe9e9;
                    width: 900px;
                    margin: auto;
                    padding: 1rem;
                }}
                h1 {{
                    text-align: center;
                    font-size: 40pt;
                    font-weight: normal;
                }}
                h2 {{
                    text-align: center;
                    color: red;
                }}
                .cards {{
                    list-style: none;
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
                    font-size: 1.25rem;
                    font-weight: bold;
                }}
                .card__text {{
                    font-size: 1rem;
                    line-height: 1.5;
                }}
            </style>
        </head>
        <body>
            <h1>My Animal Repository</h1>
            {content_html}
        </body>
    </html>
    """
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)

def build_cards_html(animals):
    if not animals:
        return ''

    cards_html = '<ul class="cards">'
    for animal in animals:
        name = animal.get("name", "Unknown")
        diet = animal.get("characteristics", {}).get("diet", "Unknown")
        locations = animal.get("locations", [])
        location = locations[0] if locations else "Unknown"
        animal_type = animal.get("taxonomy", {}).get("class", "")

        cards_html += f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <p class="card__text"><strong>Diet:</strong> {diet}</p>
            <p class="card__text"><strong>First Location:</strong> {location}</p>
        """
        if animal_type:
            cards_html += f"<p class=\"card__text\"><strong>Type:</strong> {animal_type}</p>"

        cards_html += "</li>"

    cards_html += "</ul>"
    return cards_html

def main():
    animal_name = input("Please enter an animal: ")
    animals = data_fetcher.fetch_data(animal_name)

    if not animals:
        message = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
        generate_html_page(message)
    else:
        cards_html = build_cards_html(animals)
        generate_html_page(cards_html)

    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()
