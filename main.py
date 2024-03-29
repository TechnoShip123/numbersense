# Link to practice test: http://bryantheath.com/files/2018/03/Q061.pdf
import random
import questions
import time
import json
from pathlib import Path
from Player import Player, QuizType
from colorama import init as colorama_init, Fore as C, ansi
from pick import pick
import utils
import learnmode as lm
from getpass import getpass
import os
from practicemode import practiceMode, choose_type

# utils.changeAdminPassword("Admin")
from rich.console import Console
from rich.markdown import Markdown

Console().print(Markdown(f"# Numbersense.{C.BLUE}py"))
colorama_init(True)


def write_leaderboard(quiz_type: QuizType, player1: Player, total, time_lapsed):
    num_c = float(player1.get_nem_stuff())
    if num_c / float(total) == 1.0:
        datae = displayLeaderboard(quiz_type, time=time_lapsed, numQuestions=total, player=player1)
    else:
        datae = displayLeaderboard(quiz_type)
    with open('myfile.json', 'w') as leaderboard_file:
        json.dump(datae, leaderboard_file)
    leaderboard_file.close()


def time_convert(sec):
    sec = round(sec, 2)
    ms = sec % 1 * 100
    sec = round(sec)
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {:02d}:{:02d}:{:02d}:{:02d}".format(int(hours), int(mins), sec, int(round(ms))))
    return mins * 60 + sec + .01 * ms


global player1


# Create necessary directories
Path("users/").mkdir(parents=True, exist_ok=True)


def main(totalQuestions: int, player1: Player):
    counter = 1
    player1.num_correct = 0
    if totalQuestions == 0:
        return 0
    while counter <= totalQuestions:
        if player1.current_mode == QuizType.NORMAL:
            print(f"{counter}) ", end="")
            questionType = random.randint(1, 31)
            # Print the question number
            match questionType:
                case 1:
                    if questions.divide_by(random.randint(1, 25)):
                        player1.num_correct += 1
                case 2:
                    if questions.multiply_by():
                        player1.num_correct += 1
                case 3:
                    if questions.multiply_fractions():
                        player1.num_correct += 1
                case 4:
                    if questions.centered_around_third():
                        player1.num_correct += 1
                case 5:
                    if questions.square_number():
                        player1.num_correct += 1
                case 6:
                    if questions.cube_number():
                        player1.num_correct += 1
                case 7:
                    if questions.square_root_number():
                        player1.num_correct += 1
                case 8:
                    if questions.cube_root_number():
                        player1.num_correct += 1
                case 9:
                    if questions.difference_of_reverses(random.randint(3, 4)):
                        player1.num_correct += 1
                case 10:
                    if questions.gcf_lcm_question():
                        player1.num_correct += 1
                case 11:
                    if questions.add_squares(random.randint(1, 2)):
                        player1.num_correct += 1
                case 12:
                    if questions.remainder():
                        player1.num_correct += 1
                case 13:
                    if questions.compare_fractions():
                        player1.num_correct += 1
                case 14:
                    if questions.difference_of_squares():
                        player1.num_correct += 1
                case 15:
                    if questions.close_to_hundred():
                        player1.num_correct += 1
                case 16:
                    if questions.x_and_y_cubed():
                        player1.num_correct += 1
                case 17:
                    if questions.divide_fractions():
                        player1.num_correct += 1
                case 18:
                    if questions.stats():
                        player1.num_correct += 1
                case 19:
                    if questions.integral_divisors_question():
                        player1.num_correct += 1
                case 20:
                    if questions.logarithm_question():
                        player1.num_correct += 1
                case 21:
                    if questions.sep_digits():
                        player1.num_correct += 1
                case 22:
                    if questions.xtoy1():
                        player1.num_correct += 1
                case 23:
                    if questions.add_common_products():
                        player1.num_correct += 1
                case 24:
                    if questions.subsets_question():
                        player1.num_correct += 1
                case 25:
                    if questions.multiply_over_37():
                        player1.num_correct += 1
                case 26:
                    if questions.order_of_operations_question():
                        player1.num_correct += 1
                case 27:
                    if questions.decimal_to_fractions():
                        player1.num_correct += 1
                case 28:
                    if questions.frac_to_dec():
                        player1.num_correct += 1
                case 29:
                    if questions.add_opposite_fractions():
                        player1.num_correct += 1
                case 30:
                    if questions.convert_to_base_10_question():
                        player1.num_correct += 1
                case 31:
                    if questions.convert_from_base_10_question():
                        player1.num_correct += 1
            counter += 1
                    

        elif player1.current_mode == quizMode.EASY:
            QuestionType = random.randint(1, 7)
            print(f"{counter}) ", end="")
            match QuestionType:
                case 1:
                    if questions.divide_by(random.randint(1, 10)):
                        player1.num_correct += 1
                case 2:
                    if questions.multiply_by():
                        player1.num_correct += 1
                case 3:
                    if questions.multiply_fractions():
                        player1.num_correct += 1
                case 4:
                    if questions.square_number(easy=True):
                        player1.num_correct += 1
                case 5:
                    if questions.add_squares(1):
                        player1.num_correct += 1
                case 6:
                    if questions.gcf_lcm_question():
                        player1.num_correct += 1
                case 7:
                    if questions.frac_to_dec():
                        player1.num_correct += 1
            counter += 1
        elif player1.current_mode == quizMode.HARD:
            QuestionType = random.randint(1, 11)
            print(f"{counter}) ", end="")
            match QuestionType:
                case 1:
                    if questions.cube_number():
                        player1.num_correct += 1
                case 2:
                    if questions.cube_root_number():
                        player1.num_correct += 1
                case 3:
                    if questions.add_squares(2):
                        player1.num_correct += 1
                case 4:
                    if questions.difference_of_squares():
                        player1.num_correct += 1
                case 5:
                    if questions.close_to_hundred():
                        player1.num_correct += 1
                case 6:
                    if questions.x_and_y_cubed():
                        player1.num_correct += 1
                case 7:
                    if questions.logarithm_question():
                        player1.num_correct += 1
                case 8:
                    if questions.xtoy1():
                        player1.num_correct += 1
                case 9:
                    if questions.add_common_products():
                        player1.num_correct += 1
                case 10:
                    if questions.decimal_to_fractions():
                        player1.num_correct += 1
                case 11:
                    if questions.convert_to_base_10_question():
                        player1.num_correct += 1
            counter += 1
        elif player1.current_mode == quizMode.QUICK:
            QuestionType = random.randint(1, 6)
            print(f"{counter}) ", end="")
            match QuestionType:
                case 1:
                    if questions.divide_by(random.randint(1, 10)):
                        player1.num_correct += 1
                case 2:
                    if questions.multiply_by():
                        player1.num_correct += 1
                case 3:
                    if questions.square_number(easy=True):
                        player1.num_correct += 1
                case 4:
                    if questions.add_squares(1):
                        player1.num_correct += 1
                case 5:
                    if questions.frac_to_dec():
                        player1.num_correct += 1
                case 6:
                    if questions.cube_number():
                        player1.num_correct += 1
            counter += 1
        else:
            print("Error #0: Not found")
            exit()
    print(f"Questions answered correctly: {player1.num_correct}/{totalQuestions}")
    return totalQuestions


def displayLeaderboard(mode: QuizType, time=None, numQuestions=None, player=None):
    # start of where error could occur
    if time is not None:
        time = time
    if numQuestions is not None:
        num_of_questions = int(numQuestions)
    else:
        num_of_questions = None
    pnumQ = None
    with open("myfile.json", "r+") as data_file:
        other_data = json.load(data_file)

    # end
    data_file.close()
    if time is None:
        return other_data
    if numQuestions is None:
        return other_data

    # 20 questions
    # TODO: we shouldn't need this since we implemented __str__() method for the enum
    match mode:
        case QuizType.NORMAL:
            mode = "Normal Mode"
        case QuizType.EASY:
            mode = "Easy Mode"
        case QuizType.HARD:
            mode = "Hard Mode"
        case QuizType.QUICK:
            mode = "Quick Mode"

    if num_of_questions != 3 and num_of_questions != 10 and num_of_questions != 20:
        return other_data

    match num_of_questions:
        case 3:
            num_of_questions = "threeq"
            pnumQ = "Three Questions"
        case 10:
            num_of_questions = "tenq"
            pnumQ = "Ten Questions"
        case 20:
            num_of_questions = "twentyq"
            pnumQ = "Twenty Questions"

    if time < float(other_data[f"{mode}, {num_of_questions}"]["First"][0]):
        print(f"Congratulations! You made First Place in {pnumQ}, {mode}")
        other_data[f"{mode}, {num_of_questions}"]["Third"][0], other_data[f"{mode}, {num_of_questions}"]["Third"][1] = other_data[f"{mode}, {num_of_questions}"]["Second"][0], \
                                                                                   other_data[f"{mode}, {num_of_questions}"]["Second"][1]
        other_data[f"{mode}, {num_of_questions}"]["Second"][0], other_data[f"{mode}, {num_of_questions}"]["Second"][1] = other_data[f"{mode}, {num_of_questions}"]["First"][
                                                                                         0], \
                                                                                     other_data[f"{mode}, {num_of_questions}"]["First"][1]
        other_data[f"{mode}, {num_of_questions}"]["First"][0], other_data[f"{mode}, {num_of_questions}"]["First"][1] = time, str(player1)

    elif time < float(other_data[f"{mode}, {num_of_questions}"]["Second"][0]):
        print(f"Congratulations! You made Second Place in {pnumQ}, {mode}")
        other_data[f"{mode}, {num_of_questions}"]["Third"][0], other_data[f"{mode}, {num_of_questions}"]["Third"][1] = other_data[f"{mode}, {num_of_questions}"]["Second"][0], \
                                                                                   other_data[f"{mode}, {num_of_questions}"]["Second"][1]
        other_data[f"{mode}, {num_of_questions}"]["Second"][0], other_data[f"{mode}, {num_of_questions}"]["Second"][1] = time, str(player1)

    elif time < float(other_data[f"{mode}, {num_of_questions}"]["Third"][0]):
        print(f"Congratulations! You made Third Place in {pnumQ}, {mode}")
        other_data[f"{mode}, {num_of_questions}"]["Third"][0], other_data[f"{mode}, {num_of_questions}"]["Third"][1] = time, str(player1)

    return other_data


# Make sure this is the main file ------------------------------
if __name__ == "__main__":
    # Get the quiz mode

    quizMode: QuizType = None
    # Whether we should generate basic user data file instantly
    # TODO: This will later be replaced by adding a new row with default info to database
    newAccount: bool = False
    print(ansi.BEL, end='')
    username = input("Username: ")
    player1: Player = Player(username, quizMode)
    # ----------------------------------------------------

    while True:
        title = 'Choose a quiz mode: '
        options = ["😀 Easy", "😐 Normal", "👺 Hard", "⏰ Quick", "🤝 2 Player (v.s.)", "🎲 Random", "⚙️ Settings", "📝 Give Feedback",
                   "🔒 Administrative Menu",
                   "📙 Learn Mode", "🏋️ Practice mode", "🥇 Display High Scores", "🚪🏃 Exit"]
        settingsOptions = ["🔑 Change Password", "❌ Delete Account", "📝 Get additional Info", "⬅ Go Back"]
        lmGroups = ["Basic Operations", "Powers", "Addition and Subtraction", "Data and Algebra"]
        lmGroupsOne = ["Multiplying by 25", "Multiplying by 75", "Multiplying by 101", "Multiplying by 11", "Difference of Reverses",  "Multiplying Two Numbers Centered Around a Third", "Remainders","Adding with Common Products",  "Multiplying Numbers Close to 100", "Adding with digits and 0's", "Multiplying over 37"]
        lmGroupsTwo = ["Squaring Numbers", "Cubing Numbers", "Square Rooting Numbers", "Cube Rooting Numbers", "Adding Square Type One", "Adding Squares Type Two", "Difference of squares", "Logarithms"]
        lmGroupsThree = ["Multiplying Fractions", "Compare Fractions", "Dividing Fractions", "Adding Opposite Fractions"]
        lmGroupsFour = ["GCF and LCM", "Mean, Median, and Range", "Integral Divisors", "Subsets", "Order of Operations",
                        "x to y +/- 1", "x and y cubed Algebra"]
        mode, index = pick(options, title, indicator='👉', default_index=5)

        # 😀 Easy
        if index == 0:
            quizMode = QuizType.EASY
            utils.log_stats(QuizType.EASY)

        # 😐 Normal
        elif index == 1:
            quizMode = QuizType.NORMAL
            utils.log_stats(QuizType.NORMAL)

        # 👺 Hard
        elif index == 2:
            quizMode = QuizType.HARD
            utils.log_stats(QuizType.HARD)
        elif index == 3:
            quizMode = QuizType.QUICK
            utils.log_stats(QuizType.QUICK)
        elif index == 4:
            quizMode = QuizType.TWO_PLAYER_VS

        elif index == 5:
            quizMode, numQuestions = utils.gen_random_mode()

        # ⚙️ Settings
        elif index == 6:

            mode2, index2 = pick(settingsOptions, "Settings", indicator='👉', default_index=1)
            if index2 == 0:
                new_password = input("Enter your new password: ")
                player1.changePassword(new_password)
                print(f"{C.BLUE}Password changed, logging out...")
                exit(0)
            if index2 == 1:
                conf, conf2 = pick(["Yes", "No"], "Are you sure?", indicator='👉', default_index=1)
                if conf2 == 0:
                    utils.delete_account(player1.name)
                    exit()
                if conf2 == 1:
                    print("Account deletion cancelled.")
                    continue
            if index2 == 2:
                utils.give_info()
                continue
            if index2 == 3:
                continue
        # 📝 Give Feedback
        elif index == 7:
            utils.log_feedback(player1.name, input("What feedback would you like to provide?: "))
            input("Thank you for your feedback. \nPress enter to return to the main menu. ")
            continue
        # 🔒 Administrative Menu
        elif index == 8:
            with open("whitelist.json", "r") as bFile:
                data = json.load(bFile)
            bFile.close()
            with open("adminpwd.json", "r+") as pF:
                password1 = json.load(pF)
            pF.close()
            for element in data:
                if username == element:
                    password = getpass()
                    if utils.check_password(password, password1):
                        utils.doThing()
                    else:
                        print(f"{C.RED}Incorrect password. Aborting...")
                    exit()
            print("You do not have sufficient permissions to complete this action.  Do not try this again.")
            input("Press enter to return to the main menu. ")

            continue
        elif index == 9:
            lmmode, lmgindex = pick(lmGroups, "What topic? ", indicator='👉', default_index=0)
            if lmgindex == 0:
                lmg1mode, lmg1index = pick(lmGroupsOne, "What lesson? ", indicator='👉', default_index=0)
                match lmg1index:
                    case 0:
                        lm.learn_multiplyBy25()
                    case 1:
                        lm.learn_multiplyBy75()
                    case 2:
                        lm.learn_multiplyBy101()
                    case 3:
                        lm.learn_multiplyBy11()
                    case 4:
                        lm.learn_diffOfReverses()
                    case 5:
                        lm.learn_centeredAroundThird()
                    case 6:
                        lm.learn_remainder()
                    case 7:
                        lm.learn_addCommon()
                    case 8:
                        lm.learn_closeToHundred()
                    case 9:
                        lm.learn_sepDigits()
                    case 10:
                        lm.learn_multiplyOver37()
            elif lmgindex == 1:
                lmg2mode, lmg2index = pick(lmGroupsTwo, "What lesson? ", indicator='👉', default_index=0)
                if lmg2index == 0:
                    lm.learn_squareNumbers()
                if lmg2index == 1:
                    lm.learn_cubeNumbers()
                if lmg2index == 2:
                    lm.learn_squareRootNumber()
                if lmg2index == 3:
                    lm.learn_cubeRootNumber()
                if lmg2index == 4:
                    lm.learn_addSquares3x()
                if lmg2index == 5:
                    lm.learn_addSquaresSpec()
                if lmg2index == 6:
                    lm.learn_differenceOfSquares()
                if lmg2index == 7:
                    lm.learn_logarithms()
            elif lmgindex == 2:
                lmg3mode, lmg3index = pick(lmGroupsThree, "What lesson? ", indicator='👉', default_index=0)
                if lmg3index == 0:
                    lm.learn_multiplyFractions()
                if lmg3index == 1:
                    lm.learn_compareFractions()
                if lmg3index == 2:
                    lm.learn_divideFractions()
                if lmg3index == 3:
                    lm.learn_add_opposite_fractions()
            elif lmgindex == 3:
                lmg4mode, lmg4index = pick(lmGroupsFour, "What lesson? ", indicator='👉', default_index=0)
                if lmg4index == 0:
                    lm.learn_gcflcm()
                if lmg4index == 1:
                    lm.learn_stats()
                if lmg4index == 2:
                    lm.learn_integralDivisors()
                if lmg4index == 3:
                    lm.learn_subsets()
                if lmg4index == 4:
                    lm.learn_OrderofOperations()
                if lmg4index == 5:
                    lm.learn_xtoy1()
                if lmg4index == 6:
                    lm.learn_xAndYCubed()

            else:
                print("Error #1: Not found")
                exit()
            input("\nPress enter to return to the main menu\n")
            continue
        elif index == 10:
            practiceMode(choose_type())
            input("\nPress enter to return to the main menu.")
            continue
        elif index == 11:
            player1.get_high_scores()
            input("Press enter to go back. ")
            continue
        elif index == 12:
            print("Thank you for playing.")
            if player1.is_guest:
                os.remove(f"./users/{player1}.json")
            break

        else:
            print(" Error #2: Not found")
            exit(1)

        # ----------------------------------------------------
        player1.current_mode = quizMode

        if index == 5:
            print(quizMode, numQuestions)
            print("Remember, leave your answer blank to exit.")
            input("Press Enter to start\n--------------------")
            start_time = time.time()
            total = main(int(numQuestions), player1)
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_lapsed = time_convert(time_lapsed)
            print(f"Score: {player1.calculate_score(total)}")
        # If  mode
        elif quizMode == QuizType.EASY or quizMode == quizMode.NORMAL or quizMode == QuizType.HARD or quizMode == QuizType.QUICK:
            numQuestions = input("How many questions? >> ")
            while not numQuestions.isnumeric():
                numQuestions = input("Invalid input. How many questions? >> ")
            numQuestions = int(numQuestions)
            # player1.current_mode = QuizType.EASY
            print("Remember, leave your answer blank to exit.")
            input("Press Enter to start\n--------------------")
            start_time = time.time()
            total = main(int(numQuestions), player1)
            end_time = time.time()
            time_lapsed = end_time - start_time
            if total > 0:
                time_lapsed = time_convert(time_lapsed)
                print(f"Score: {player1.calculate_score(total)}")

        elif quizMode == QuizType.TWO_PLAYER_VS:
            player1.current_mode = QuizType.TWO_PLAYER_VS
            print(f"{C.RED}Error: Not implemented")
            print(f"{C.RED}2 player mode is not yet implemented. Please try something else.")
            input(f"\n{C.CYAN}Press enter to go back to the main menu{C.CYAN}\n")
            continue

        player1.save_to_scoreboard(quizMode)
        if total > 0:
            write_leaderboard(quizMode, player1, total, time_lapsed)

        
        choice = input("Play again? (Y/n)")
        choice_sentinel = choice.strip().lower() in ("", "y", "ye", "yes")
        while choice_sentinel:
            # player1.current_mode = QuizType.EASY
            print("Remember, leave your answer blank to exit.")
            input("Press Enter to start\n--------------------")
            start_time = time.time()
            if index == 5:
                player1.current_mode, numQuestions = utils.gen_random_mode()
                print(player1.current_mode, numQuestions)
            total = main(int(numQuestions), player1)
            end_time = time.time()
            time_lapsed = end_time - start_time
            if total > 0:
                time_lapsed = time_convert(time_lapsed)
                print(f"Score: {player1.calculate_score(total)}")
            player1.save_to_scoreboard(quizMode)
            if total > 0:
                write_leaderboard(player1.current_mode, player1, total, time_lapsed)
            choice = input("Play again? (Y/n)")
            choice_sentinel = choice.strip().lower() in ("", "y", "ye", "yes")
        userLeaderboardResponse = input("Display leaderboard? [Y/n] >> ").strip().lower()
        if userLeaderboardResponse == "y" or userLeaderboardResponse == "":
            utils.read_leaderboard(quiz_mode=quizMode, num_questions=int(numQuestions))
        input("\nPress enter to go back to the main menu\n")
"""except:
    give_feedback = input("It seems that the program has crashed. Would you like to provide feedback? (Y/n)")
    if give_feedback.lower().strip() == "y" or give_feedback == "":
        utils.log_feedback("Error", input("Feedback: ") + "(Error:)")"""
    
    