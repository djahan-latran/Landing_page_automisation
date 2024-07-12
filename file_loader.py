
class FileLoader:

    def load_file(self, filepath):

        with open(filepath, "r", encoding="utf8") as file:
            content = file.read()
            town_names = content.split(",")

        return town_names