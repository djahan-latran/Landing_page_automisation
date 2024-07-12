from file_loader import FileLoader


class TownList(FileLoader):

    def __init__(self, filepath):
        self.filepath = filepath

    def create_list(self):

        town_list = self.load_file(self.filepath)

        return town_list