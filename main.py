import colorama
from colorama import Fore, Back
colorama.init(autoreset=True) #We don't want it keeping the color.
import shlex #?
import os

print(f"{Fore.YELLOW}Shell starting..")

# Put anything prestart here..

l2k = [] #Used in removal processes.

commands = {
    "help": f"""{Fore.GREEN}HELP INFORMATION:{Fore.WHITE}
Capitalization does not matter.
{Fore.CYAN}"Q"{Fore.WHITE}, {Fore.CYAN}"EXIT"{Fore.WHITE}, or {Fore.CYAN}"QUIT"{Fore.WHITE} to exit.
{Fore.CYAN}"ECHO"{Fore.WHITE} will return what you entered into it. [Text]
{Fore.CYAN}"READ"{Fore.WHITE}, {Fore.CYAN}"CAT" {Fore.WHITE} will attempt to read and print the contents of a file. [File/Path]
{Fore.CYAN}"NEW"{Fore.WHITE} will create a new, blank file at the desired location and with the desired name. [File/Path]
{Fore.CYAN}"APPEND"{Fore.WHITE}, {Fore.CYAN}"APP"{Fore.WHITE} will attempt to append a line to a file. [File/Path, Text, (OPTIONAL) Line Index]
{Fore.CYAN}"REMLINE"{Fore.WHITE}, {Fore.CYAN}"REML" {Fore.WHITE} will attempt to remove the specified line from a file. [File/Path, Line Index]
{Fore.YELLOW}"CLEARFILE"{Fore.WHITE}, {Fore.YELLOW}"CFILE" {Fore.WHITE} will attempt to clear the file you specify. [File/Path]
{Fore.RED}"REMFILE"{Fore.WHITE}, {Fore.RED}"RFILE" {Fore.WHITE} Will attempt to remove the file/directory entirely. {Fore.RED}Use these two sparingly.{Fore.WHITE} [File/Path]
{Fore.CYAN}"COPY" {Fore.WHITE} Will take one file's contents and put them in another. {Fore.RED}Will override new file's contents. {Fore.WHITE}[File/Path to copy from, File/Path to copy to]
{Fore.CYAN}"RENAME"{Fore.WHITE}, {Fore.CYAN}"REN" {Fore.WHITE}Will just rename a file. [File/Path, New Name]
{Fore.CYAN}"LIST"{Fore.WHITE}, {Fore.CYAN}"LS" {Fore.WHITE}Will list the folders and files in a directory. If given a file, it will list the contents of the directory it's in. [Path]""",
    "q": "exit",
    "quit": "exit",
    "exit": "exit",
    "echo": "echo",
    "read": "read",
    "cat": "read",
    "new": "new",
    "append": "ap",
    "app": "ap",
    "remline": "remline",
    "reml": "remline",
    "clearfile": "cf",
    "cfile": "cf",
    "remfile": "ref",
    "rfile": "ref",
    "copy": "copy",
    "test": f"Please refer to {Fore.CYAN}'Help'{Fore.WHITE} if you want the list of commands. Your testing is.. {Fore.LIGHTGREEN_EX}Successful!",
    "rename": "ren",
    "ren": "ren",
    "list": "ls",
    "ls": "ls",
}

print(f"{Fore.GREEN}Shell started!")
while True:
    user = str(input(f"{Fore.LIGHTBLUE_EX}$ {Fore.WHITE}"))
    sl = shlex.split(user)
    if user.lower() != "":
        if sl[0].lower() in commands:
            userl = user.lower()
            retval = commands[sl[0].lower()]
            match retval:
                case "exit":
                    print(f"{Fore.LIGHTRED_EX}Exiting!")
                    break
                case "echo":
                    if len(sl) != 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Echo' Expected 1 argument but got {len(sl) - 1} arguments.")
                        continue
                    else:
                        print(f"{Fore.LIGHTCYAN_EX}{sl[1]}")
                        continue
                case "read":
                    if len(sl) != 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Read/Cat' Expected 1 argument but got {len(sl) - 1} arguments.")
                        continue
                    else:
                        try:
                            with open(sl[1], "r") as file:
                                lines = file.readlines()
                                if len(lines) == 0:
                                    print(f"{Back.LIGHTYELLOW_EX}{Fore.BLACK}Info:{Back.RESET}{Fore.YELLOW} File was empty.")
                                    continue
                                else:
                                    numspaces = 7 #Modify this at will.
                                    for lnum, line in enumerate(lines, 1):
                                        print(f"{Fore.LIGHTYELLOW_EX}{lnum}{Fore.YELLOW}{' ' * (numspaces - len(str(lnum)))}{line.strip()}")
                                    continue
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "new":
                    if len(sl) != 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'New' Expected 1 argument but got {len(sl) - 1} arguments.")
                        continue
                    else:
                        try:
                            with open(sl[1], "w") as file:
                                print(f"{Fore.GREEN}Successfully created '{sl[1]}.'")
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "ap":
                    if len(sl) != 3 and len(sl) != 4:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Append' Expected 2-3 arguments but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        if len(sl) == 3:
                            try:
                                with open(sl[1], "a") as file:
                                    if sl[2].endswith("\n"):
                                        file.write(sl[2])
                                        print(f"{Fore.GREEN}Successfully appended '{sl[2][:-2]}' to {sl[1]}!")
                                    elif sl[2].endswith("@!:"):
                                        file.write(sl[2][:-3])
                                        print(f"{Fore.GREEN}Successfully appended '{sl[2][:-3]}' to {sl[1]}!")
                                    else:
                                        file.write(sl[2] + "\n")
                                        print(f"{Fore.GREEN}Successfully appended '{sl[2]}' to {sl[1]}!")                     
                            except FileNotFoundError:
                                print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                                continue
                            except Exception as ermsg:
                                print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                                continue
                        elif len(sl) == 4:
                            try:
                                with open(sl[1], "r") as file:
                                    l2k = file.readlines()
                            except Exception as ermsg:
                                print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                                l2k = []
                                continue
                            l2k.insert(int(sl[3])-1, f"{sl[2]}\n")
                            try:
                                with open(sl[1], "w") as file:
                                    for i in range(len(l2k)):
                                        file.write(l2k[i])
                                    print(f"{Fore.GREEN}Successfully inserted '{sl[2]}' into {sl[1]}!")
                                    l2k = []
                            except Exception as ermsg:
                                print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                                l2k = []
                                continue
                case "remline":
                    if len(sl) != 3:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Remline' Expected 2 arguments but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        try:
                            with open(sl[1], "r") as file:
                                for i, line in enumerate(file):
                                    if i != int(sl[2]) - 1:
                                        l2k.append(line.strip())
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                        try:
                            with open(sl[1], "w") as file:
                                for i in range(len(l2k)):
                                    if i != len(l2k)-1:
                                        file.write(l2k[i] + "\n")
                                    else:
                                        file.write(l2k[i])
                                l2k = []
                            print(f"{Fore.YELLOW}Successfully removed line number {sl[2]}.")
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            l2k = []
                            continue
                case "cf":
                    if len(sl) != 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Clearfile' Expected 2 arguments but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        try:
                            with open(sl[1], "w") as file:
                                file.write("")
                                print(f"{Fore.YELLOW}Successfully cleared file '{sl[0]}'.")
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "ref":
                    if len(sl) != 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Removefile' Expected 2 arguments but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        try:
                            os.remove(sl[1])
                            print(f"{Fore.RED}File or directory '{sl[1]}' removed.")
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "copy":
                    if len(sl) != 3:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Copy' Expected 3 argument(s) but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        try:
                            with open(sl[1], "r") as file:
                                l2k = file.readlines()
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                        try:
                            with open(sl[2], "w") as file:
                                for i in range(len(l2k)):
                                    file.write(l2k[i])
                                print(f"{Fore.GREEN}Successfully copied from '{sl[1]}' to '{sl[2]}'!")
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "rname":
                    if len(sl) != 3:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'Rename' Expected 2 argument(s) but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        try:
                            with open(sl[1], "r") as file:
                                l2k = file.readlines()
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                        try:
                            with open(os.path.dirname(sl[1])+"\\"+os.path.basename(sl[2]), "w") as file:
                                for i in range(len(l2k)):
                                    file.write(l2k[i])
                                try:
                                    os.remove(sl[1])
                                except OSError as ermsg:
                                    print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Failed to delete the original file. Could be no perms or it's in use.")
                                    print(f"{Fore.RED}(This command clones and then deletes the original file to rename it.)")
                                print(f"{Fore.GREEN}Successfully renamed from '{sl[1]}' to '{sl[2]}'!")
                        except FileNotFoundError:
                            print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                            continue
                        except Exception as ermsg:
                            print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                            continue
                case "ls":
                    if len(sl) > 2:
                        print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Command 'List' Expected 0-1 arguments but got {len(sl) - 1} argument(s).")
                        continue
                    else:
                        print(f"Files in {Fore.LIGHTGREEN_EX}Green.")
                        print(f"Directories in {Fore.LIGHTYELLOW_EX}Yellow.")
                        if len(sl) != 1:
                            try:
                                if os.path.isfile(sl[1]):
                                    p2l = os.path.dirname(sl[1])
                                elif os.path.isdir(sl[1]):
                                    p2l = sl[1]
                                for item in os.listdir(p2l):
                                    if os.path.isfile(os.path.join(p2l, item)):
                                        print(f"{Fore.LIGHTGREEN_EX}{item}")
                                    elif os.path.isdir(os.path.join(p2l, item)):
                                        print(f"{Fore.LIGHTYELLOW_EX}{item}")
                                continue
                            except FileNotFoundError:
                                print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                                continue
                            except Exception as ermsg:
                                print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                                continue
                        else:
                            try:
                                p2l = os.path.dirname(__file__)
                                for item in os.listdir(p2l):
                                    if os.path.isfile(os.path.join(p2l, item)):
                                        print(f"{Fore.LIGHTGREEN_EX}{item}")
                                    elif os.path.isdir(os.path.join(p2l, item)):
                                        print(f"{Fore.LIGHTYELLOW_EX}{item}")
                                continue
                            except FileNotFoundError:
                                print(f"{Back.RED}{Fore.WHITE}ERROR:{Back.RESET}{Fore.RED} Invalid file name or path!")
                                continue
                            except Exception as ermsg:
                                print(f"{Back.CYAN}{Fore.WHITE}Not doing the thing.{Back.RESET}{Fore.YELLOW} Sorry not sorry. ({ermsg})")
                                continue
                case _:
                    print(retval) #If theres no special return value associated, just print the return value.
        else:
            print(f"{Fore.RED}Invalid command! See 'Help' for a list of commands and general help.")
            continue
    elif user.lower() == "":
        continue