import requests

API_KEY = "aTap3/8ErjpLphigqe6Fcw==deLuV38G8sgyJ5ug"


def fetch_animal_data(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        "X-Api-Key": aTap3/8ErjpLphigqe6Fcw==deLuV38G8sgyJ5ug
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
