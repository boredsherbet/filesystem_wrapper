from browser import Browser
import os


def main():
    print("Welcome to filesystem_wrapper")
    print("building filesystem tree")
    try:
        browser = Browser()
    except Exception as e:
        print(f"an error occurred initializing the filesystem: {e}")
        return
    while True:
        try:
            user_input = input(
                f"(filesystem_wrapper) {browser.current_dir.os_path}>>>"
            ).split()
            if not user_input:
                continue
            # split command and args
            command = user_input[0]
            args = user_input[1:] if len(user_input) > 1 else None
            # processing commands...
            if command == "tree":
                browser.tree()
            elif command == "pwd":
                print(browser.current_dir.os_path)
            elif command == "ls":
                if args and args[0] == "-l":
                    browser.list(long=True)
                    # adds details such as os_path and size
                else:
                    browser.list()
            elif command == "cd" and args:
                browser.change_directory(args[0])
            elif command == "rm" and args:
                if len(args) > 1 and args[1] == "-l":
                    browser.delete(args[0], recursive=True)
                    # adds details such as os_path and size
                else:
                    browser.delete(args[0])
            elif command == "find" and args:
                browser.find(args[0])
            elif command == "touch" and args:
                for filename in args:
                    browser.new_file(filename)
            elif command == "mkdir" and args:
                for dirname in args:
                    browser.new_dir(dirname)
            elif command == "exit":
                break
            else:
                print("Please use a valid command")
        except Exception as e:
            print(f"An error occurred: {e}")

    # exit message
    print(f"Returning you to {os.getcwd()}")
    print("Thank you for using filesystem_wrapper.")


if __name__ == "__main__":
    main()
