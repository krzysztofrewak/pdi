from src.map import Map


def get_searched_phrase(argv):
    if len(argv) < 2:
        exit("Try to pass argument: python3 main.py Legnicka")

    return argv[1]


def get_mapbox(argv):
    if len(argv) == 3:
        return Map(argv[2])

    return None
