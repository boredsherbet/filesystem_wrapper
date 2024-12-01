import os


class FileNode:
    def __init__(self, name, path):
        self.name = name
        self.os_path = path
        try:
            self.size = os.path.getsize(path) // 1024  # in KB
        except FileNotFoundError:
            print("The file on path {path} was not found. Size has been set to 0KB.")
            self.size = 0

    def __str__(self):
        return f"{self.os_path} \t {self.name} \t {self.size} KB"

    def delete(self):
        """deletes the file"""
        # TODO: this one needs some fixing
        if os.path.exists(self.os_path):
            os.remove(self.os_path)
            print(f"File '{self.os_path}' deleted.")


class DirectoryNode:
    def __init__(self, name, parent, path):
        self.name = name
        self.parentdir = parent
        self.subdirectories = []
        self.files = []
        self.size = 0
        self.os_path = path
        self.is_empty = True
        self.build_tree()

    def build_tree(self):
        """
        checks the self.os_path for directory contents and refreshes all child nodes to match
        """
        try:
            contents = os.listdir(
                self.os_path
            )  # apparently this is an array, so we good here
            for item in contents:
                self.is_empty = False
                item_path = os.path.join(self.os_path, item)
                if os.path.isdir(item_path):
                    node = DirectoryNode(item, self, item_path)
                    self.subdirectories.append(node)
                    self.size += node.size
                else:
                    node = FileNode(item, item_path)
                    self.files.append(node)
                    self.size += node.size
        except Exception as e:
            print(f"Error building directory tree for {self.os_path}: {e}")

    # Adding Files and Subdirectories
    def add_subdirectory(self, name):
        """
        adds `name` directory as subdirectory, creates new `name` directory in OS.
        """
        try:
            subdir_path = os.path.join(self.os_path, name)
            os.mkdir(subdir_path)
            node = DirectoryNode(name, self, subdir_path)
            self.size += node.size
            self.subdirectories.append(node)
            self.isEmpty = False
            print(f"Subdirectory `{name}` created.")
        except FileExistsError:
            print(f"Subdirectory `{name}` already exists!")
        except Exception as e:
            print(f"Error creating subdirectory: {e}")

    def add_file(self, name):
        """
        adds new file to directory, creates new file in OS.
        """
        try:
            path = os.path.join(self.os_path, name)
            with open(path, "w") as file:
                file.write("")
            file_node = FileNode(name, path)
            self.files.append(file_node)
            self.size += file.size
            self.isEmpty = False
            print(f"New file `{path}` created")
        except Exception as e:
            print(f"Error creating file: {e}")

    # Deletion logic
    def remove(self, name, recursive=False):
        """
        Removes file or directory by name. Recursive specifies whether to delete directories with contents.
        """
        for file in self.files:
            if file.name == name:
                file.delete()
                self.files.remove(file)
                return
        for dir in self.subdirectories:
            if dir.name == name:
                try:
                    if dir.is_empty or recursive:
                        dir.delete()
                        self.subdirectories.remove(dir)
                    else:
                        print(f"{name} contains files or directories.")
                        print(f"To delete recursively, use `rm {name} -r`")
                    return
                except Exception as e:
                    print(f"Error deleting directory '{self.name}': {e}")
                    return

        print(f"No file or directory called '{name}' was found.")

    def delete(self):
        for file in self.files:
            file.delete()
        for subdir in self.subdirectories:
            subdir.delete()
        if os.path.exists(self.os_path):
            os.rmdir(self.os_path)
            print(f"Directory '{self.os_path}' deleted.")

    # Tree parsing stuff
    def search(self, name):
        for file in self.files:
            if file.name == name:
                print(file.os_path)
                return file
        for dir in self.subdirectories:
            if dir.name == name:
                print(dir.os_path)
                return dir
            dir.search(name)
        print("there is no file or folder named {name} in the current directory")

    def tree_contents(self, depth=""):
        # yea ik that's lazy but idk how to do it in python
        for file in self.dir.files:
            print(f"{depth}{file.name}")
        for directory in self.dir.isubdirectories:
            print(f"{depth}{directory.name}")
            directory.tree_contents(depth + " ")
