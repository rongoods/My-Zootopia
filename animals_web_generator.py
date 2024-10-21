import json

def read_html(template):
    with open(template, "r") as data:
        return data.read()

html_contents = read_html('animals_template.html')
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file:
        return json.load(file)

animals_data = load_data('animals_data.json')

output = ''
for animal in animals_data:
    if 'name' in animal:
        name = animal['name']
        output += f"Name: {name}\n"
    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        diet = animal['characteristics']['diet']
        output += f"Diet: {diet}\n"
    if 'locations' in animal:
        locations = animal['locations']
        output += f"First Location: {locations[0]}\n"
    if 'characteristics' in animal and 'type' in animal['characteristics']:
        type_of_animal = animal['characteristics']['type']
        output += f"Type: {type_of_animal}\n"
    output += "\n"

finished_html = html_contents.replace("__REPLACE_ANIMALS_INFO__", output)

with open('animals.html', "w") as file:
    file.write(finished_html)