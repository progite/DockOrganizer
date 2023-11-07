class File:
    def __init__(self, filename):
        self.filename = filename
    def read_file(self):
        file = open("docs/" + self.filename, "r")
        content = file.read()
        return content