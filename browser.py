import nodes
import os


class Browser:
    def __init__(self):
        self.current_dir = nodes.DirectoryNode(
            os.path.basename(os.getcwd()), None, os.getcwd()
        )

    def change_directory(self, name):
        if name == "..":
            if self.current_dir.parent is None:
                print("you cannot move above the base directory")
            else:
                self.current_dir = self.current_dir.parent
        for directory in self.subdirectories:
            if directory.name == name:
                self.current_dir = directory
                return
        print("There is no directory by that name. ")

    def list_contents(self):
        for file in self.current_dir.files:
            print(file.name)
        for directory in self.current_dir.subdirectories:
            print(directory.name)

    def tree_contents(self, depth=""):
        # yea ik that's lazy but idk how to do it in python
        for file in self.current_dir.files:
            print(f"{depth}{file.name}")
        for directory in self.curnrent_dir.isubdirectories:
            print(f"{depth}{directory.name}")
            directory.tree_contents(depth + " ")

    def search(self, name):
        # TODO: add a search
        pass
