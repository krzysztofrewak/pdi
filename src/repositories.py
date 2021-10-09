from src.places import City, Street


class Cities(object):
    def __init__(self, file):
        self.file = file

    def find_by_id(self, city_id):
        with open(self.file) as fp:
            lines = fp.readlines()
            city = self.__find_exact_city(lines, city_id)

            if not city:
                city = self.__find_fallback_city(lines, city_id)

            if city:
                return city

        return City("? (" + city_id + ")")

    @staticmethod
    def __find_exact_city(lines, city_id):
        for line in lines:
            if city_id + ";" + city_id in line:
                return City(line.split(";")[6])

    @staticmethod
    def __find_fallback_city(lines, city_id):
        for line in lines:
            if city_id in line:
                return City(line.split(";")[6])


class Streets(object):
    def __init__(self, file, cities):
        self.file = file
        self.cities = cities

    def find_by_street_name(self, street_name):
        with open(self.file) as fp:
            lines = fp.readlines()
            for line in lines:
                if street_name.lower() in line.lower():
                    street = Street(line)
                    street.set_city(self.cities.find_by_id(street.city_id))
                    yield street
