import os
import glob
import json
import getpass
import random
import Player
import bcrypt

from pick import pick
from colorama import init as colorama_init, Fore as C, Style
from tabulate import tabulate
from rich.console import Console
from rich.markdown import Markdown
from Player import QuizType


colorama_init(True)


def purge_all_users() -> bool:
    """
     Removes all files in the `users/` directory.
     :return: Whether the operation was executed(can be user cancelled)
     """

    files = glob.glob('./users/*')
    option, index = pick(["Yes", "No"], "Permanently remove all user data files? (Purges `./users/*` folder contents)",
                         indicator='🤔', default_index=1)
    if index == 0:
        for f in files:
            try:
                print(f"{C.RED}Removing {C.CYAN}{f}{C.RED} permanently.")
                os.remove(f)
            except Exception as e:
                print(f"{C.RED}Error while purging 	{C.BLUE}`users/`{C.RED} folder!")
                print(e)
                return False
    else:
        print("Cancelled operation.")
        return False


def get_user_save_data_path(username: str) -> str:
    """
    Get user file location
    :param username: player's username
    :return: file path as str
    """
    return f"users/{username}.json"


def check_if_user_data_present(user_name: str) -> bool:
    """
     Checks whether a user's save data file exists and is not empty.
      :param: user_name The user's name to look for
    :return: Whether the save data file was present in the `users/` directory.
     """
    # If the file exists
    if os.path.isfile(get_user_save_data_path(user_name)):
        with open(get_user_save_data_path(user_name), 'r') as f:
            # If it is not empty or whitespace/newline
            if len(f.read().strip()) != 0:
                f.close()
                return True
            f.close()
    return False


def changePassword(player: Player, new_password: str):
    player.changePassword(new_password)


# --------------------------------
def doThing(player: Player):
    title = 'Please choose an option from the menu (use arrow keys to navigate): '
    options = [purge_all_users.__name__, check_if_user_data_present.__name__, changePassword.__name__,
               whitelist_user.__name__, backup_leaderboard.__name__, resetLeaderboard.__name__,
               un_whitelist_user.__name__, delete_account.__name__, change_admin_password.__name__]

    option, index = pick(options, title, indicator='👉', default_index=1)

    match options[index]:
        case purge_all_users.__name__:
            purge_all_users()
        case check_if_user_data_present.__name__:
            username = input("Please enter the user's name to check for >> ")
            if check_if_user_data_present(username):
                print(f"{C.GREEN}User data file {C.BLUE}{get_user_save_data_path(username)}{C.GREEN} exists!")
            else:
                print(
                    f"{C.RED}User data file {C.BLUE}{get_user_save_data_path(username)}{C.RED} does {C.MAGENTA}NOT{C.RED} exist.")
        case whitelist_user.__name__:
            username = input("User to whitelist: ")
            whitelist_user(username)
        case changePassword.__name__:
            new_password = getpass.getpass("Enter your new password: ")
            changePassword(player, new_password)
            print(f"{C.BLUE}Password changed, logging out...")
            exit(0)
        case resetLeaderboard.__name__:
            print("Reset leaderboard.")
            resetLeaderboard()
        case backup_leaderboard.__name__:
            print("Leaderboard backed up.")
            backup_leaderboard()
        case un_whitelist_user.__name__:
            un_whitelist_user(input("User to unwhitelist: "))
        case delete_account.__name__:
            delete_account(input("Account to delete: "))
        case change_admin_password.__name__:
            change_admin_password(input("New password: "))
        case _:
            print(f"No command was executed, {C.RED}something may be wrong with the menu code.{Style.RESET_ALL}")
            exit(1)


def whitelist_user(new_user):
    with open("whitelist.json", "r") as w:
        data = json.load(w)
    w.close()
    data.append(new_user)
    with open("whitelist.json", "w") as w:
        json.dump(data, w)
    print("Whitelisted " + new_user)


def un_whitelist_user(new_user):
    with open("whitelist.json", "r") as w:
        data = json.load(w)
    w.close()
    t = 0
    c = 0
    for i in data:
        if new_user == i:
            data.remove(new_user)
        else:
            c += 1
        t += 1
    if t == c:
        print("User is not whitelisted.")
        exit()
    with open("whitelist.json", "w") as w:
        json.dump(data, w)
    print("Un-whitelisted " + new_user)


def backup_leaderboard():
    with open("myfile.json", "r") as lb:
        lbd = json.load(lb)
    lb.close()
    with open("myfileBackup.json", "w") as lbb:
        json.dump(lbd, lbb)
    lbb.close()


def resetLeaderboard():
    with open("myfileBackup.json", "r") as lbb:
        lbd = json.load(lbb)
    lbb.close()
    with open("myfile.json", "w") as lb:
        json.dump(lbd, lb)
    lb.close()


def read_leaderboard(quiz_mode=None, alternate_question_type=None, num_questions=0):
    if num_questions == 3:
        num_questions = "threeq"
    elif num_questions == 10:
        num_questions = "tenq"
    elif num_questions == 20:
        num_questions = "twentyq"
    elif num_questions is None:
        pass
    else:
        num_questions = "threeq"

    with open("myfile.json", "r+") as lb_file:
        lb_data = json.load(lb_file)
        if quiz_mode == Player.QuizType.EASY:
            quiz_mode = "Easy Mode"
        if quiz_mode == Player.QuizType.NORMAL:
            quiz_mode = "Normal Mode"
        if quiz_mode == Player.QuizType.HARD:
            quiz_mode = "Hard Mode"
        if quiz_mode == None:
            quiz_mode = alternate_question_type

        print(tabulate(
            ([mode for mode in lb_data[f"{quiz_mode}, {num_questions}"].values()]),
            headers=["Time", "Username"],
            tablefmt='orgtbl'
        ))
    lb_file.close()


def delete_account(username):
    username = str(username)
    if check_if_user_data_present(username):
        os.remove(f"./users/{username}.json")


def give_info():
    options1 = ["Leaderboard", "Programmers", "Updates"]
    options11 = ["3 Questions", "10 Questions", "20 Questions"]
    options12 = ["Easy Mode", "Normal Mode"]
    options13 = ["Recent Updates", "Future Plans"]
    mmm, index1 = pick(options1, "What would you like info on?", indicator='👉', default_index=0)
    if index1 == 0:
        print("  					Info about leaderboard.", end="")
        print("""
        The leaderboard keeps track of the top three fastest times for getting every question correct. To qualify, you must not answer any questions wrong, and do so as quickly as possible. The categories are 3, 10 and 20 questions easy or hard.
        """)

        view_leaderboard_choice: str = input("View leaderboard? (Y/n) >> ").lower()
        if view_leaderboard_choice == "y" or view_leaderboard_choice == "":
            mode11, index11 = pick(options11, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            mode12, index12 = pick(options12, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            match index11:
                case 0:
                    numQe = 3
                    pr = "Three Questions"
                case 1:
                    numQe = 10
                    pr = "Ten Questions"
                case 2:
                    numQe = 20
                    pr = "Twenty Questions"
            print("\t\t\t" + pr + ", " + mode12)
            read_leaderboard(num_questions=int(numQe), alternate_question_type=mode12)
        else:
            print("Exiting.")
            return

    if index1 == 1:
        print("  				Programmers Info")
        print("""
        This program was written by Unmesh Tokale and Sopan Jalkote, two high school students currently attending Round Rock
        High School in the 10th grade.
        """)
    if 2 == index1:
        # TODO: Move app flow to loops for each scene
        mmm, index13 = pick(options13, "What would you like info on? ", indicator='👉', default_index=0)
        if index13 == 0:
            print("  				Recent updates")
            print("""
            Recent updates have been focused on user-friendliness, including ensuring that non-numeric inputs do not raise errors. Learn Mode and basic features have also been implemented.
            """)
        if index13 == 1:
            with open('TODO.md', 'r') as todo_file:
                todo_markdown = todo_file.read()

                Console().print(Markdown(todo_markdown))
            todo_file.close()
    input("\nPress enter to return to the main menu\n")


def better_num_input(question_reprint: str = ""):
    while True:
        try:
            thing = input(question_reprint + "\n👉 ")
            if thing == "":
                eP = input("Exit program? Y/n ")
                if eP == "y" or eP == "":
                    print("Exited program")
                    exit()
                else:
                    print("Exit cancelled.")
                    continue
            int(thing)
            break
        except ValueError:
            print("Invalid input. ", end="")
    return thing


"""def betterNumInput(question_reprint: str = ""):
    did_int_parse_correctly = False
    while not did_int_parse_correctly:
        try:
            thing = input(question_reprint)
            int(thing)
            did_int_parse_correctly = True
        except ValueError:
            did_int_parse_correctly = False
            thing = input("Invalid input. " + question_reprint + "\n👉 ")
    return thing
"""


def better_frac_input(question_reprint, decimal=False):
    thing = input(question_reprint + "\n👉")
    state = True
    first = True
    num_dig = 0
    num_dot = 0
    num_slash = 0
    num_dash = 0
    empty_list = []
    if thing == "":
        exit_choice = input("Exit program? Y/n ")
        if exit_choice == "y" or exit_choice == "":
            print("Exited program")
            exit()
        else:
            print("Exit cancelled.")
            thing = input(question_reprint + "\n👉")
    for i in thing:
        if first and i == "/":
            state = False

        if (not (i.isnumeric())) and (i != "/" or decimal) and i != "." and i != "-":
            state = False
        if i == ".":
            num_dot += 1
        if i == "/":
            num_slash += 1
        if i == "-":
            num_dash += 1
        first = False
        empty_list.append(i)
        num_dig += 1
    if (empty_list[0] == "." or empty_list[0] == "/" or empty_list[0] == "-") and num_dig == 1:
        state = False
    if num_dot > 1 or num_slash > 1 or num_dash > 1:
        state = False
    while not state:

        first = True
        thing = input("Invalid input. " + question_reprint + "\n👉 ")
        if thing == "":
            exit_choice = input("Exit program? Y/n ")
            if exit_choice == "y" or exit_choice == "":
                print("Exited program")
                exit()
            else:
                print("Exit cancelled.")
                continue
        state = True
        num_dig = 0
        num_dot = 0
        num_dash = 0
        num_slash = 0
        empty_list = []
        for i in thing:
            if first and (i == "/"):
                state = False
                print(1)
            if (not (i.isnumeric())) and (i != "/" or decimal) and i != ".":
                state = False
            if i == ".":
                num_dot += 1
            if i == "/":
                num_slash += 1
            if i == "-":
                num_dash += 1
            first = False
            num_dig += 1
            empty_list.append(i)
        if (empty_list[0] == "." or empty_list[0] == "/" or empty_list[0] == "-") and num_dig == 1:
            state = False
            print(2)

        if num_dot > 1 or num_slash > 1 or num_dash > 1:
            state = False
            print(3)
    return thing


def encrypt_password(password: str, return_as_str: bool = False):
    """Encrypts the given password (Should be str) and returns the result as either encoded or decoded."""
    bytes = password.encode('utf-8')  # encodes password str to an array of bytes
    hashed_pwd = bcrypt.hashpw(bytes, bcrypt.gensalt())  # Newly hashed & salted password
    if return_as_str:
        return hashed_pwd.decode('utf-8')
    return hashed_pwd


def check_password(user_pwd, retrieved_pwd) -> bool:
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    user_pwd = user_pwd.encode("utf-8")
    if not type(retrieved_pwd) == bytes:
        retrieved_pwd = retrieved_pwd.encode("utf-8")
    return bcrypt.checkpw(user_pwd, retrieved_pwd)


def change_admin_password(new_pwd):
    new_pwd = encrypt_password(new_pwd, return_as_str=True)
    with open("adminpwd.json", "w+") as pF:
        json.dump(new_pwd, pF)
    print("Password changed successfully.")
    pF.close()


def gen_random_mode():
    modes = [QuizType.EASY, QuizType.NORMAL, QuizType.HARD]
    num_questions = [3, 10, 20]
    return random.choice(modes), random.choice(num_questions)
