class FileNode:
    def __init__(self, name, size):
        self.name = name
        self.size = size # in KB

class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
        self.files = []

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)
        def add_file(self, file):
        self.files.append(file)

class FileSystem:
    def __init__(self):
        self.root = DirectoryNode("Root"
                                  )
    def search_file(self, directory, file_name, path=""):
        ###
        Your coding
        ###
        return None
    
    def calculate_size(self, directory):
        ###
        Your coding
        ###
        return total_size
    
    def list_contents(self, directory, indent=0):
        ###
        Your coding
        ###
