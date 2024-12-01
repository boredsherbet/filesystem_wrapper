from nodes import DirectoryNode
import os


class Browser:
    def __init__(self):
        try:
            self.current_dir = DirectoryNode(
                os.path.basename(os.getcwd()), None, os.getcwd()
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize browser: {e}")

    def change_directory(self, name):
        """change the current directory"""
        try:
            if name == "..":
                if self.current_dir.parent is None:
                    print("you cannot move above the base directory")
                else:
                    self.current_dir = self.current_dir.parent
                return
            for directory in self.current_dir.subdirectories:
                if directory.name == name:
                    self.current_dir = directory
                    return
            print(f"There is no directory {name} in {self.current_dir.os_path}. ")
        except Exception as e:
            raise RuntimeError(f"Couldn't change directories: {e}")

    def list(self, long=False):
        """list the contents of the current directory"""
        for file in self.current_dir.files:
            if long:
                print(file)
            else:
                print(file.name)
        for directory in self.current_dir.subdirectories:
            if long:
                print(directory)
            else:
                print(directory.name)

    def tree(self):
        """display the directory tree"""
        self.current_dir.tree_contents()

    def search(self, name):
        """searches through the current directory and all of its subdirectories for `name`"""
        result = self.current_dir.search(name)
        if result:
            print(result)
        else:
            print(f"nothing called {name} in {self.current_dir.os_path}")

    def new_file(self, name):
        """creates a new file in the current directory"""
        try:
            self.current_dir.add_file(name)
            print(f"Created file {self.os_path.join(self.current_dir.os_path, name)}")
        except Exception as e:
            print(f"Failed to create file: {e}")

    def new_dir(self, name):
        """creates new directory `name` in current directory"""
        try:
            self.current_dir.add_subdirectory(name)
            print(
                f"Created directory {self.os_path.join(self.current_dir.os_path, name)}"
            )
        except Exception as e:
            print(f"Failed to create directory: {e}")

    def delete(self, name):
        try:
            if self.current_dir.remove(name):
                print(f"Deleted {self.os_path.join(self.current_dir.os_path, name)}")
            else:
                print(
                    f"There was no file or directory {name} in {self.current_dir.os_path}"
                )
        except Exception as e:
            print(f"Failed to delete {name}: {e}")
