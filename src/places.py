class City(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Street(object):
    def __init__(self, properties):
        self.prefix = properties.split(";")[6]
        self.additional_name = properties.split(";")[8]
        self.proper_name = properties.split(";")[7]
        self.city_id = properties.split(";")[4]
        self.city = None

    def get_full_name(self):
        name = self.prefix + " " + self.additional_name + " " + self.proper_name
        return " ".join(name.split())

    def set_city(self, city):
        self.city = city
