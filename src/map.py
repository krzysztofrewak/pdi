import urllib.request, json
from urllib.parse import quote


class Map(object):
    def __init__(self, token):
        self.token = token
        self.coordinates = []

    def add_coordinates_for_phrase(self, phrase):
        with urllib.request.urlopen(self.__get_api_url(phrase)) as url:
            data = json.loads(url.read().decode())
            if len(data["features"]) and data["features"][0] and data["features"][0]["center"]:
                self.coordinates.append({
                    "title": phrase,
                    "coordinates": data["features"][0]["center"]
                })

    def __get_api_url(self, phrase):
        return "https://api.mapbox.com/geocoding/v5/mapbox.places/" + quote(
            phrase) + ".json?access_token=" + self.token + "&types=address"

    def prepare_map(self, searched_street):
        index = open("./www/index.html", "w")
        with open("./www/index.html.template") as template:
            template = template.read()
            template = template.replace("$MAPBOX_TOKEN", self.token)
            template = template.replace("$PINS", json.dumps(self.coordinates))
            template = template.replace("$TITLE", searched_street)

            index.write(template)

        print("Index file generated.")
