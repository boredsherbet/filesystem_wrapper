from nodes import Browser
import os


def main():
    print("Welcome to filesystem_wrapper")
    print("building filesystem tree")
    browser = Browser()
    while True:
        user_input = input(
            f"(filesystem_wrapper) {browser.current_dir.os_path}>>>"
        ).split()
        command = user_input[0]
        if command == "tree":
            pass
        elif command == "ls":
            pass
        elif command == "pwd":
            pass
        elif command == "cd":
            pass
        elif command == "exit":
            break
        elif command == "rm":
            pass
        elif command == "find":
            pass
        elif command == "touch":
            pass
        elif command == "mkdir":
            pass
    print(f"Returning you to {os.getcwd()}")
    print("Thank you for using filesystem_wrapper.")


if __name__ == "__main__":
    main()
