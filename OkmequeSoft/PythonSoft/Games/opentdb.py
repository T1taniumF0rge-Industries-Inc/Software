try:
    print("OpenTDB API - By OpenTDB Corp - Licensed under CC BY-SA 4.0. All copies of this program shall mention Okmeque1 as stated in the LICENSE.MD file in PythonSoft folder and OpenTDB Corp. Thanks to them for making this possible")
    print('Website -> "https://opentdb.com/api_config.php"')
    import requests#starting imports. 
    import random
    import shelve
    import html
    def geturl(amount=1,difficulty="easy",category=9,typee="multiple"):#geturl function calls opentdb.com and returns what it responds in JSON
        returnstring = "https://opentdb.com/api.php"
        returnstring += "?amount=" + str(amount)
        returnstring += "&category=" + str(category)
        returnstring += "&difficulty=" + difficulty
        returnstring += "&type=" + typee
        print(returnstring)
        returnurl = requests.get(returnstring)
        return html.unescape(returnurl.json())
    def displayscore():#displays the score from shelve file or classic file.
        shelvey = input("Use SHELVE MODERN MODE or classic mode? [Y/N] : ").upper()
        if shelvey == "Y":
            with shelve.open(input("Please enter a valid SHELVE file. The format must be 'A:\\SHELVEFILE' with no file extensions after : ")) as readi:
                for x in readi:
                    print(x + " : " + str(readi[x]["points"]))
                return
        else:
            for line in open(input("Please enter the save file file name. The format must be A:\\Directory\\Subdirectory\\file.extention. : ")):
                    if line.split(" -> ")[0] == input("Player name : "):
                        print(line.split(" -> ")[1])
    def resultscreen(points) -> None:#results screen. you only get to see this once you finish the game
        if points == numquestion:
            print("You won!")
            print("Total points : " + str(pts))
            print("WARNING! SHELVE MODE FILE FORMAT IS 'A:\\SHELVEFILE' WITH NO EXTENSIONS. IF YOU NEED A DIFFERENT FILE NAME/EXTENSION, CHOOSE CLASSIC MODE BY PRESSING 'N' AT 'Use SHELVE MDOERN MODE or classic mode'.")
            savefile = input("Save score to file? [Y/N] : ")
            savefile = savefile.upper()
            if savefile == "Y":
                shelvey = input("Use SHELVE MODERN MODE or classic mode? [Y/N] : ").upper()
                display = input("See previous score(s)?[Y/N]? : ").upper()
                if display == "Y":
                    displayscore()
                if shelvey == "Y":
                    name = input("Enter player name : ")
                    with shelve.open(input("Please enter a valid SHELVE file. The format must be 'A:\\SHELVEFILE' with no file extensions after : ")) as writi:#don't ask me how this works.
                        if name in writi:
                            writi[name]["points"] += pts
                        else:
                            writi[name] = {"points":pts}
                            namee = ""
                            highscore = 0
                        for x in writi:
                            if writi[x]["points"] > highscore:
                                highscore = writi[x]["points"]
                                namee = x
                        print("Highscore : " + str(highscore) + " from : " + namee)
                        exit()
                elif shelvey == "N":
                    name = input("Enter player name : ")
                    with open(input("Please enter a valid file name. The format must be A:\\Directory\\Subdirectory\\file.extention. : "),"a") as writing:
                        writing.write(name + " -> " + str(pts) + " points." + "\n")
                        print("Save complete.")
                        exit()
        else:
            print("You lost!")
            print("Total points : " + str(pts))
            print("Hope you do better next time. We will not save the file as we want you to impress your friends.")
            input("Press ENTER to exit...")#cya later!
            exit()
    print("DEFAULT CHOICE is 1 question, easy difficulty, general knowledge and multiple questions with AUTOMODE OFF and FORGIVEMODE ON.")
    numquestion = int(input("Enter number of questions : "))#ahh, where the selection happens. there is no default for your information.
    difselect = input("Enter difficulty[(A)ny, (E)asy, (M)edium, (H)ard] : ")
    difselect = difselect.upper()
    if difselect == "P":#naughty naughty, why are you here?
        while True:
            a = input("Password: ")
            if a == "MSWIN3112":
                break
        b = input("(D)isplayScore,(G)etURL or (R)eultscreen?").upper()
        if b == "D":
            displayscore()
        elif b == "G":
            geturl(3,"easy",18,"multiple")
        else:
            resultscreen(3)
    difmap = {"A":"Any","E":"easy","M":"medium","H":"hard"}#maps that caused me hours of pain...
    difselect = difmap[difselect]
    print("""
    0 : Random
    1 : General knowledge
    2 : Books
    3 : Films
    4 : Music
    5 : Music/Teathrals
    6 : Television  
    7 : Video games
    8 : Board games
    9 : Science and nature
    10 : Computer science
    11 : Mathematics science
    12 : Mythology
    13 : Sports
    14 : Geography
    15 : History
    16 : Politics
    17 : Arts
    18 : Celebrities
    19 : Animals
    20 : Vehicles
    21 : Comics
    22 : Gadget science
    23 : Manga/Anime
    24 : Cartoon/Animations
                                                            """)
    catselect = int(input("Enter category : "))
    if catselect == 0:
        catselect = random.randint(1,23)
    catselect = catselect + 8
    typeselect = input("Enter type of question[(R)andom, (M)ultiple choice, (T)rue or False : ")
    typeselect = typeselect.upper()
    if typeselect == "R" or typeselect == "":
        typeselect = random.choice(["M","T"])
    typemap = {"A":"Any","M":"multiple","T":"boolean"}
    typeselect = typemap[typeselect]
    automode = input("Auto mode. Auto mode allows this program to automatically switch to the next question, however you cannot choose it. [Y/N]? : ").upper()
    automode == automode.upper()
    if automode == "":
        automode = "N"
    forgivemode = input("Forgiveness mode. Forgiveness mode allows you to re-do a question if you failed it IF auto mode is DISABLED. [Y/N]? : ")
    forgivemode.upper()
    if forgivemode == "":
        forgivemode = "Y"
    print("Contacting server, please wait...")#just to test your internet and opentdb website
    test = requests.get("https://opentdb.com")
    print("Generating URL, please wait...")
    questionget = geturl(numquestion,difselect,catselect,typeselect)#where the magic begins...
    game = True
    done = []
    pts = 0
    choosequstion = 0
    while game == True:#the actual game. has lots of modes for different things
        if pts == numquestion:
            print("You have won. Redirecting to win screen menu...")
        print("Questions done : " + str(done))
        print("You MUST complete every question correctly in order to win and there is no timer.")
        if automode == "Y":
            if choosequstion == numquestion:
                input("You have finished. Press ENTER to goto results screen...")
                resultscreen(pts)
            print(html.unescape(str(questionget["results"][choosequstion]["question"]).replace("&quot;","'")))
            if questionget["results"][choosequstion]["type"] == "multiple":
                lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                random.shuffle(l1)
                print("Possible options : " )
                print(*l1,sep="\n")
                answer = int(input("Enter choice. The first option is option 0 and the last option is option 3 -> "))
                if l1[answer] == lcorrect:
                    pts += 1
                    done.append(questionget["results"][choosequstion])
                    input("Correct answer. 1 point added. Press ENTER to continue...")
                    choosequstion += 1
                else:
                    input("Incorrect answer. Press ENTER to continue...")
                    choosequstion += 1
            else:
                answer = input("(T)rue/(F)alse? : ")
                answer = answer.upper()
                tfmap = {"T":"True","F":"False"}
                answer = tfmap[answer]
                if answer == questionget["results"][choosequstion]["correct_answer"]:
                    pts += 1
                    done.append(questionget["results"][choosequstion])
                    choosequstion += 1
                    input("Correct answer. 1 point added. Press ENTER to continue...")
                else:
                    input("Incorrect answer. Press ENTER to continue...")
                    choosequstion += 1
        else:       
            
            choosequstion = int(input("You have selected : " + str(numquestion) + " questions and have to choose. Please choose the question number with the minimum being 1 and the maximum being the number you chose. Enter '-1' and then press ENTER to goto resultscreen -> "))
            if choosequstion == -1:
                resultscreen(pts)
            choosequstion = choosequstion - 1 
            if questionget["results"][choosequstion] in done:
                input("Question already done. Press ENTER to continue...")
            print(str(questionget["results"][choosequstion]["question"]).replace("&quot;","'"))
            if questionget["results"][choosequstion]["type"] == "multiple":
                lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                random.shuffle(l1)
                print("Possible options : " )
                print(*l1,sep="\n")
                answer = int(input("Enter choice. The first option is option 0 and the last option is option 3 -> "))
                if l1[answer] == lcorrect:
                    pts += 1
                    done.append(questionget["results"][choosequstion])
                    input("Correct answer. 1 point added. Press ENTER to continue...")
                else:
                    if forgivemode == "N":
                        done.append(questionget["results"][choosequstion])
                    input("Incorrect answer. Press ENTER to continue...")
            else:
                answer = input("(True)/(F)alse? : ")
                if answer == questionget["results"][choosequstion]["correct_answer"]:
                    pts += 1
                    done.append(questionget["results"][choosequstion])
                    input("Correct answer. 1 point added. Press ENTER to continue...")
                else:
                    if forgivemode == "N":
                        done.append(questionget["results"][choosequstion])
                    input("Incorrect answer. Press ENTER to continue...")
except ModuleNotFoundError:#boring exception handling.
    print("STOP : 0199\nYou do not have the module REQUESTS. Please download that by going to [PYTHON_FOLDER]\\Scripts and doing PIP INSTALL REQUESTS. Make sure that you have an internet connection")
    input("Press ENTER to exit...")
    exit()    
except ImportError:
    print("STOP : 0199\nYou do not have the module REQUESTS. Please download that by going to [PYTHON_FOLDER]\\Scripts and doing PIP INSTALL REQUESTS. Make sure that you have an internet connection")
    input("Press ENTER to exit...")
    exit()
except ValueError:
    print("STOP : 0211\nBad value was inputted. Please enter the CORRECT type of value required.")
    input("Press ENTER to exit...")
    exit()
except requests.exceptions.ConnectionError:
    print("STOP : 1E/08\nConnection failed. Please check your connection or contact the server administrator for more info.")
    input("Press ENTER to exit...")
    exit()
except KeyboardInterrupt:
    print("STOP : 0270\nUser has chosen to exit. Exiting...")
    exit()
except EOFError:
    print("STOP : 0250\nUser has chosen to exit. Exiting...")
    exit()
except KeyError:
    print("STOP : 0190\nBad access key and/or bad value was inputted. When an input asks (T)rue or (F)alse, enter 'T' or 'F' or it will throw error 0190")
    input("Press ENTER to exit...")
    exit()
except IndexError:
    print("STOP : 0910\nBad value/access number specified.")
    input("Press ENTER to exit...")
    exit()
except PermissionError:
    print("STOP : 0210\nAccess violation has happened in your file.")
    input("Press ENTER to exit...")
    exit()
except FileNotFoundError:
    print("STOP : 6510B\nThe file you specified does not exist. Please create it and try again")
    input("Press ENTER to exit...")
    exit()
except SystemExit:#Because I figured it out : stupid exit() function
    exit()
except BaseException:
    print("STOP : 770A\nGeneral exception. Retry the operation")
    input("Press ENTER to exit...")
