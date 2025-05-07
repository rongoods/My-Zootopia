
# import json
# import requests
#
#
# def read_html(template_path):
#     """Read an HTML template file and return its contents."""
#     with open(template_path, "r", encoding="utf-8") as file:
#         return file.read()
#
#
# def fetch_animal_data(animal_name):
#     """Fetch animal data from the API based on a search term."""
#     url = f"https://api.api-ninjas.com/v1/animals?search={animal_name}"
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json()
#
#
# def serialize_animal(animal_obj):
#     """Generate HTML for a single animal entry."""
#     output = '<li class="cards__item">\n'
#
#     if "name" in animal_obj:
#         output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
#
#     characteristics = animal_obj.get("characteristics", {})
#
#     diet = characteristics.get("diet")
#     if diet:
#         output += f'<p class="card__text"><strong>Diet:</strong> {diet}</p>\n'
#
#     locations = animal_obj.get("locations", [])
#     if locations:
#         output += f'<p class="card__text"><strong>First Location:</strong> {locations[0]}</p>\n'
#
#     animal_type = characteristics.get("type")
#     if animal_type:
#         output += f'<p class="card__text"><strong>Type:</strong> {animal_type}</p>\n'
#
#     output += '</li>\n'
#     return output
#
#
# def generate_html(animals_data, html_template):
#     """Generate the final HTML content by inserting animal data."""
#     output = ''.join(serialize_animal(animal) for animal in animals_data)
#     return html_template.replace("__REPLACE_ANIMALS_INFO__", output)
#
#
# def main():
#     """Main function to fetch data, generate HTML, and write to a file."""
#     html_template = read_html('animals_template.html')
#     animals_data = fetch_animal_data("Fox")
#
#     finished_html = generate_html(animals_data, html_template)
#
#     with open('animals.html', "w", encoding="utf-8") as file:
#         file.write(finished_html)
#
#
# if __name__ == "__main__":
#     main()
#


# import json
# import requests
#
#
# def read_html(template_path):
#     """Read an HTML template file and return its contents."""
#     with open(template_path, "r", encoding="utf-8") as file:
#         return file.read()

import requests

API_KEY = "aTap3/8ErjpLphigqe6Fcw==deLuV38G8sgyJ5ug"


def fetch_animal_data(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        "X-Api-Key": API_KEY
    }
    params = {
        "name": animal_name
    }

    response = requests.get(url, headers=headers, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP Error: {e}")
        print(f"[DEBUG] Status Code: {response.status_code}")
        print(f"[DEBUG] Response: {response.text}")
        raise

    return response.json()


def generate_html(animals_data):
    html = "<html><head><title>Animal Info</title></head><body>"
    html += "<h1>Animal Information</h1>"

    if not animals_data:
        html += "<p>No information found.</p>"
    else:
        for animal in animals_data:
            html += f"<h2>{animal.get('name', 'Unknown')}</h2>"
            html += f"<p><strong>Scientific Name:</strong> {animal.get('taxonomy', {}).get('scientific_name', 'N/A')}</p>"
            html += f"<p><strong>Habitat:</strong> {animal.get('characteristics', {}).get('habitat', 'N/A')}</p>"
            html += f"<p><strong>Diet:</strong> {animal.get('characteristics', {}).get('diet', 'N/A')}</p>"

    html += "</body></html>"

    with open("animal_info.html", "w") as file:
        file.write(html)

    print("[INFO] HTML file 'animal_info.html' created!")


def main():
    animal_name = "Fox"
    print(f"[INFO] Fetching data for: {animal_name}")
    animals_data = fetch_animal_data(animal_name)
    generate_html(animals_data)


if __name__ == "__main__":
    main()
