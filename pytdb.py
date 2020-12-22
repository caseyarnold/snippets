"""
    Text File database management solution
"""
class Pytdb:
    def __init__(self, file_location):
        self.file_location = file_location
        self.file = None

    def connect(self, file_location = False):
        if file_location is False:
            file_location = self.file_location

            if file_location is None:
                print("File is required in order to use pytdb")
                return

        self.file = open(file_location)
