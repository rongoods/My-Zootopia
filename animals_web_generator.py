import json

def read_html(template):
    with open(template, "r") as data:
        return data.read()

html_contents = read_html('animals_template.html')
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file:
        return json.load(file)

def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'

    if 'name' in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'<p class="card__text"><strong>Diet:</strong> {animal_obj["diet"]}</p>\n'
    if 'locations' in animal_obj:
        locations = animal_obj['locations']
        output += f'<p class="card__text"><strong>First Location:</strong> {animal_obj["locations[0]"]}</p>\n'
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'<p class="card__text"><strong>Type:</strong> {animal_obj["type_of_animal"]}</p>\n'
    output += '</li>'
    print(output)

def main():
    animals_data = load_data('animals_data.json')
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    finished_html = html_contents.replace("__REPLACE_ANIMALS_INFO__", output)

    with open('animals.html', "w") as file:
        file.write(finished_html)

if __name__ == "__main__":
    main()