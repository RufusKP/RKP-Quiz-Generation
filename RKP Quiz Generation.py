# Initiated 05/30/2020 1201 PST
# Completed 06/03/2020 2230 PST

# This program is a part of my continuing endeavor to learn Python.  This specific project was inspired from an exercise
# in Al Sweigart's book  "Automate the Boring Stuff with Python: Practical Programming for Total Beginners".  This
# program creates a multiple choice text (.txt) file.  Each quiz file has a corresponding answer key file.  The quiz
# and answer files are stored in two separate folders.  Every quiz is completely unique (thanks to the random module).
# Both the order of questions and their answer choices are randomized.  This specific quiz generator program is for
# the geography of the United States.

# PLEASE NOTE: You will have to add your desired working directory to the variable "testfolder" for this program to
# work properly.



# We import the "random" module for randomizing question order ans answer choice order.  The "os" module to create file
# paths so that we can save the results of this program on the hard drive.  The datetime module is to ensure that all
# quiz folders are unique.  This uniqueness comes from the fact that each folder is named with the exact date and
# time it was created, accurate up to the microsecond (10^-6).
import random

import os

import datetime


# This dictionary contains all 50 states in the USA with their respective capitals.  The state names are stored as
# "keys" and the capitals are stored as "values".
answer_key = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock',
             'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover',
             'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
             'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
             'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis',
             'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
             'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City',
             'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York':'Albany',
             'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
             'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
             'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin',
             'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
             'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# This variable stores the exact time this program was run as a string.  This will be used in the naming of the folder
# where the quiz and answer folders will be stored.
current_date = str(datetime.datetime.today())


# Here the user can specify how many unique quizzes they would like to generate.  The default number is 3.
testquantity = 3


# This variable stores the pathway to the current working directory (CWD) as a string.
# *** PLEASE NOTE ***
# You will have to put in the pathway you desire for this program to work.  By default a dummy path is below.  This
# program will not work with the unchanged dummy path.  Please also make the necessary changes to the syntax of the
# pathway prior to running the program.
testfolder = str("/Users/DUMMYPATH/Documents/pythontest/PythonTest " + current_date)


# This variable stores the pathway to the "Quizzes" folder where all the quizzes will be stored.
quizzes_folder = str(testfolder + "/Quizzes")

# This variable stores the pathway to the "AnswerKeys" folder where all the answer files will be stored.
answers_folder = str(testfolder + "/AnswerKeys")


# This function is the heart of the program.  It creates quiz and answerkey files for the required number to be
# generated.  In order to ensure that these quiz and answerkey files are stored in the correct folders, the CWD is
# changed as needed throughout the function.
def testcreation():
    for testnumber in range(testquantity):
        os.chdir(quizzes_folder)
        testfile = open("Test %s.txt" %(testnumber+1), 'w')
        os.chdir(answers_folder)
        answers = open("Test %s Answers.txt" %(testnumber+1), 'w')
        os.chdir(quizzes_folder)
        testfile.write(
" _______  _______  _______  _______  ______    _______  _______  __   __  __   __\n"
"|       ||       ||       ||       ||    _ |  |   _   ||       ||  | |  ||  | |  |\n"
"|    ___||    ___||   _   ||    ___||   | ||  |  |_|  ||    _  ||  |_|  ||  |_|  |\n"
"|   | __ |   |___ |  | |  ||   | __ |   |_||_ |       ||   |_| ||       ||       |\n"
"|   ||  ||    ___||  |_|  ||   ||  ||    __  ||       ||    ___||       ||_     _|\n"
"|   |_| ||   |___ |       ||   |_| ||   |  | ||   _   ||   |    |   _   |  |   |\n"
"|_______||_______||_______||_______||___|  |_||__| |__||___|    |__| |__|  |___|  \n\n")
        testfile.write("Name: \n\nInstructions: For this quiz, please choose the capital for each state of the USA.\n")
        states = list(answer_key.keys())
        capitals = list(answer_key.values())
        random.shuffle(states)
        n = 0
        os.chdir(answers_folder)
        answers.write("Here are the answers:\n\n")
        os.chdir(quizzes_folder)
        for qnumber in range(len(answer_key)):
            testfile.write("\n\n" + str(qnumber+1) + ". What is the capital of " + states[n] + "?\n")
            correctanswer = answer_key[states[n]]
            capitals.remove(correctanswer)
            randomwrongchoices = random.sample(capitals, 3)
            randomchoices = randomwrongchoices + [correctanswer]
            random.shuffle(randomchoices)
            for i in range(4):
                testfile.write("%s. %s\n" % ('ABCD'[i], randomchoices[i]))
            capitals.append(correctanswer)
            os.chdir(answers_folder)
            answers.write("%s. %s\n\n" %(str(qnumber+1) ,'ABCD'[randomchoices.index(correctanswer)]))
            os.chdir(quizzes_folder)
            n += 1
        testfile.write("\n\nGreat Job!  You completed the quiz!\n")
        testfile.close()
        answers.close()


# This function checks the existence of the folder where the quiz and answerkey files will be stored.  If the folder
# does not exist, the function creates that folder.  If the folder does exist, the program runs the testcreation()
# function.  In both cases, once the parent folder has been created, the enclosed "Quiz" and "AnswerKey" folders
# are created.
def initiate():
    if os.path.isfile(testfolder):
        os.makedirs(quizzes_folder)
        os.makedirs(answers_folder)
        testcreation()
    elif not os.path.isfile(testfolder):
        os.makedirs(testfolder)
        os.chdir(testfolder)
        os.makedirs(quizzes_folder)
        os.makedirs(answers_folder)
        testcreation()


# If the program has reached the end successfully, this function will provide an output that says so.
def programsuccessful():
    print("\nThe program has run successfully!\n")


# This calls the function and starts the program.
initiate()


# If this function is called and an output appears, the program has run successfully.
programsuccessful()
