import os


class FileNode:
    def __init__(self, name, path):
        self.name = name
        self.size = os.path.getsize(path) // 1024  # in KB
        self.os_path = path

    def __str__(self):
        return f"{ self.os_path }\t {self.size} \t {self.name}"


class DirectoryNode:
    def __init__(self, name, parent, path):
        self.name = name
        self.parentdir = parent
        self.subdirectories = []
        self.files = []
        self.size = 0
        self.os_path = path
        self.build_tree()

    def remove(self, name):
        """
        removes whatever is in directory (directly) with name `name`
        """
        for file in self.files:
            if file.name == name:
                file.delete()
                return
        for dir in self.subdirectories:
            if dir.name == name:
                dir.delete()
                return
        print("no file or directory called {name}")

    def add_subdirectory(self, name):
        """
        adds `name` directory as subdirectory, creates new `name` directory in OS.
        """
        subdir_path = f"{self.os_path}{name}"
        os.mkdir(subdir_path)
        node = DirectoryNode(name, self, subdir_path)
        self.subdirectories.append(node)

    def add_file(self, file):
        """
        adds new file to directory, creates new file in OS.
        """
        # TODO: finish this one...
        self.files.append(file)
        self.size += file.size

    def build_tree(self):
        """
        checks the self.os_path for directory contents and refreshes all child nodes to match
        """
        contents = os.listdir()
        for item in contents:
            item_path = f"{self.os_path} + {item}"
            if os.isdir():
                node = DirectoryNode(item, self, item_path)
                self.subdirectories.append(node)
                self.size += node.size()
            else:
                node = FileNode(item, item_path)
                self.files.append(node)
                self.size += node.size()

    def __str__(self):
        return f"{ self.os_path }\t {self.name}"

    def delete(self):
        # TODO: gotta delete and delete it's contents too
        pass


class Browser:
    def __init__(self):
        self.current_dir = DirectoryNode(
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

    # TODO: add a search
