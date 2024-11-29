class FileNode:
    def __init__(self, name, size):
        self.name = name
        self.size = size  # in KB


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
        self.root = DirectoryNode("Root")
        self.dfs_order = []
        self.bfs_order = []

    def dfs_search_file(self, directory, file_name, path=""):
        # search in current directory's files
        for file in directory.files:
            if file.name == file_name:
                return f"{path}/{directory.name}/{file_name}"

        # search in subdirectories
        for subdir in directory.subdirectories:
            result = self.dfs_search_file(subdir, file_name, f"{path}/{directory.name}")
            if result:
                return result

        return None

    def bfs_search_file(self, start_directory, file_name):
        queue = [(start_directory, start_directory.name)]

        while queue:
            current_dir, current_path = queue.pop(0)

            # search in current directory's files
            for file in current_dir.files:
                if file.name == file_name:
                    return f"{current_path}/{file_name}"

            # add subdirectories to queue
            for subdir in current_dir.subdirectories:
                queue.append((subdir, f"{current_path}/{subdir.name}"))

        return None

    def dfs_calculate_size(self, directory):
        total_size = sum(file.size for file in directory.files)

        for subdir in directory.subdirectories:
            total_size += self.dfs_calculate_size(subdir)

        return total_size

    def bfs_calculate_size(self, start_directory):
        total_size = 0
        queue = [start_directory]

        while queue:
            current_dir = queue.pop(0)
            total_size += sum(file.size for file in current_dir.files)
            queue.extend(current_dir.subdirectories)

        return total_size

    def list_contents(self, directory, indent=0):
        print("  " * indent + f"└── {directory.name}/")

        for file in directory.files:
            print("  " * (indent + 1) + f"├── {file.name} ({file.size}KB)")

        for subdir in directory.subdirectories:
            self.list_contents(subdir, indent + 1)

    def record_traversal_order(self, directory, method="dfs"):
        if method == "dfs":
            self.dfs_order.append(directory.name)
            for subdir in directory.subdirectories:
                self.record_traversal_order(subdir, "dfs")
        else:  # bfs
            self.bfs_order = []  # clear previous BFS order
            queue = [directory]
            while queue:
                current_dir = queue.pop(0)
                self.bfs_order.append(current_dir.name)
                queue.extend(current_dir.subdirectories)


if __name__ == "__main__":
    # start file system instance
    file_system = FileSystem()

    # create example file structure, there's probably a cleaner way to do this

    # level 1 directories
    documents = DirectoryNode("Documents")
    pictures = DirectoryNode("Pictures")
    music = DirectoryNode("Music")

    # level 2 directories under Documents
    work = DirectoryNode("Work")
    personal = DirectoryNode("Personal")
    projects = DirectoryNode("Projects")

    # level 2 directories under Pictures
    vacation = DirectoryNode("Vacation")
    family = DirectoryNode("Family")

    # level 2 directories under Music
    rock = DirectoryNode("Rock")
    jazz = DirectoryNode("Jazz")

    # level 3 directories
    project1 = DirectoryNode("Project1")
    project2 = DirectoryNode("Project2")
    italy = DirectoryNode("Italy")
    france = DirectoryNode("France")

    # create files
    doc1 = FileNode("resume.pdf", 50)
    doc2 = FileNode("report.docx", 30)
    doc3 = FileNode("notes.txt", 10)
    pic1 = FileNode("beach.jpg", 200)
    pic2 = FileNode("mountains.jpg", 150)
    pic3 = FileNode("family_reunion.jpg", 180)
    song1 = FileNode("song1.mp3", 500)
    song2 = FileNode("song2.mp3", 450)
    song3 = FileNode("jazz_compilation.mp3", 800)

    # level 1 directories to root
    file_system.root.add_subdirectory(documents)
    file_system.root.add_subdirectory(pictures)
    file_system.root.add_subdirectory(music)

    # level 2 directories
    documents.add_subdirectory(work)
    documents.add_subdirectory(personal)
    documents.add_subdirectory(projects)

    pictures.add_subdirectory(vacation)
    pictures.add_subdirectory(family)

    music.add_subdirectory(rock)
    music.add_subdirectory(jazz)

    # level 3 directories
    projects.add_subdirectory(project1)
    projects.add_subdirectory(project2)
    vacation.add_subdirectory(italy)
    vacation.add_subdirectory(france)

    # add files to those directories
    work.add_file(doc1)
    personal.add_file(doc2)
    project1.add_file(doc3)
    italy.add_file(pic1)
    france.add_file(pic2)
    family.add_file(pic3)
    rock.add_file(song1)
    rock.add_file(song2)
    jazz.add_file(song3)

    # list contents
    print("Complex Directory Structure:")
    file_system.list_contents(file_system.root)

    # search for files
    print("\nSearching for files:")
    print("Path to beach.jpg:", file_system.dfs_search_file(file_system.root, "beach.jpg"))
    print("Path to song2.mp3:", file_system.dfs_search_file(file_system.root, "song2.mp3"))

    # calculate total size of different directories using both methods
    print("\nCalculating sizes:")
    print("Total size of Documents:", file_system.dfs_calculate_size(documents), "KB")
    print("Total size of Pictures:", file_system.dfs_calculate_size(pictures), "KB")
    print("Total size of Music:", file_system.dfs_calculate_size(music), "KB")

    # Record and display traversal orders for the sake of showing differences idk
    # clear prev records
    file_system.dfs_order = []
    file_system.bfs_order = []

    print("\nTraversal Orders:")
    file_system.record_traversal_order(file_system.root, "dfs")
    file_system.record_traversal_order(file_system.root, "bfs")

    print("DFS Order (goes deep into each branch first):")
    print(" -> ".join(file_system.dfs_order))
    print("\nBFS Order (explores each level completely before going deeper):")
    print(" -> ".join(file_system.bfs_order))