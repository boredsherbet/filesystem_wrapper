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
        args = user_input[1:] if len(user_input) > 1 else None
        if command == "tree":
            pass
        elif command == "pwd":
            pass
        elif command == "exit":
            break
        elif command == "ls":
            pass
        elif command == "cd" and args is not None:
            pass
        elif command == "rm" and args is not None:
            pass
        elif command == "find" and args is not None:
            pass
        elif command == "touch" and args is not None:
            pass
        elif command == "mkdir" and args is not None:
            pass
        else:
            print("Please use a valid command")
    print(f"Returning you to {os.getcwd()}")
    print("Thank you for using filesystem_wrapper.")


if __name__ == "__main__":
    main()
