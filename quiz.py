#Imports easygui
import easygui

#Defines the values of all the variables needed later in the code
answerNum = 0
score=0
numOfQuestions=0
name = easygui.enterbox("Welcome to the NZ Trivia Quiz!!! What is your name?")
age=0
score = 0

#This block of code makes a definition called age_check and
#checks if the age is valid 
def age_check():

     #This defines age as a global variable (needed because age was
     #defined outside of this function
     global age

     #Asks the user for their age
     try:
          age = int(easygui.enterbox("Please enter your age"))
     
     #If there is a value error, it ask the user for their age again
     except ValueError:
          age = int(easygui.enterbox("Please enter your age"))

#This block of code makes a definition called name_check
#which checks if the user enters a valid name
def name_check():

     #This defines name as a global variable (needed because name was
     #defined outside of this function
     global name

     #This block of code runs if the user does not enter anything
     #or if the user presses cancel
     while name == "" or name == None:
          name = easygui.enterbox("That is not a name! Please enter a name!")

#This block of code defines a function called play_check and checks
#if the user wants to play or not if they are outside the age range
def play_check():
          
     start = easygui.buttonbox("Would you like to take this quiz? Yes or No?"\
                               ,choices = ["Yes", "No"])
     #This block of code closes the program if the user
     #does not want to play
     if start == "No":
          exit()

#Defines the mainloop               
def mainloop():
     
     #This block of code defines name as a global variable
     #Which means if it was defined at the beginning it can
     #now be used inside a function
     global name

     #This list contains the possible questions for quiz A
     a_questions = ["What is the capital of New Zealand?",\
                    "What city is known as 'The garden city?",\
                    "Where did L&P originally come from?",\
                    "In what month is mataraki celebrated?",\
                    "What colour is Kakariki?"]

     #This list contains the possible answers to the questions in Quiz A
     a_possi_ans = ["A) Auckland",\
                    "B) Wellington",\
                    "C) Christchurch",\
                    "D) Hamilton",\
                    "A) Wellington",\
                    "B) Christchurch",\
                    "C) Paeroa",\
                    "D) Auckland",\
                    "A) Putaruru",\
                    "B) Waihi",\
                    "C) Paeroa",\
                    "D) Auckland",\
                    "A) April",\
                    "B) May",\
                    "C) June",\
                    "D) July",\
                    "A) Green",\
                    "B) Blue",\
                    "C) Black",\
                    "D) Grey"]

     #This list contains all the correct answers to the Quiz A questions
     a_correct_answers = ["B) Wellington","B) Christchurch",\
                          "C) Paeroa", "C) June", "A) Green"]

     #This list contains all the possible questions for Quiz B
     b_questions = ["What is the name of the stretch of water\
 that seperates the North and South Island?",\
                 "Which New Zealand city houses the beehive?",\
                 "Which town has a giant carrot as a landmark?",\
                 "Where is 90 mile beach?",\
                 "When was the Treaty of Waitangi signed?"]

     #This list contains the possible answers to the questions in Quiz B
     b_possi_ans = ["A) Wellington Strait",\
                    "B) Tasman Channel",\
                    "C) Cook Strait",\
                    "D) Kaikoura Strait",\
                    "A) Wellington",\
                    "B) Christchurch",\
                    "C) Paeroa",\
                    "D) Auckland",\
                    "A) Taihape",\
                    "B) Waihi",\
                    "C) Paeroa",\
                    "D) Ohakune",\
                    "A) Top of the North Island",\
                    "B) Bottom of the South Island",\
                    "C) Bottom of the North Island",\
                    "D) Top of the South Island",\
                    "A) 1815",\
                    "B) 1840",\
                    "C) 1855",\
                    "D) 1875"]

     #This list contains the correct answers to all the Quiz B questions
     b_correct_answers = ["C) Cook Strait", "A) Wellington", "D) Ohakune",\
                          "A) Top of the North Island", "B) 1840"]

     #These lists below contain the 2 different types of quizzes
     #To be used later in the program so there is no redundant code
     possi_questions = [a_questions, b_questions]
     possi_ans = [a_possi_ans,b_possi_ans]
     correct_ans = [a_correct_answers,b_correct_answers]
     
     #This block of code defines a function called question_a
     #which runs when the user is eligible to sit quiz A
     def questions():

          #This block of code defines name as a global variable
          #Which means if it was defined at the beginning it can
          #now be used inside a function
          global name
          
          cont="y"

          #This block of code defines quiz as a function and this
          #function runs and chooses which quiz the user does according
          #to their age
          def quiz():

               #This block of code defines all these variables as
               #global variables (which means they can be used inside a
               #function if they were defined at the beginning
               global score
               global name
               global age
               global answerNum
               global numOfQuestions

               #This block of code runs if the user is younger
               #or equal to 7 years of age. It makes quiztype equal to
               #0 which means they will sit the first quiz as a is the
               #the first element of each list
               if age <= 7:
                    quiztype = 0

               #This block of code runs when the user is not
               #younger or equal to 7 years of age. It makes
               #the variable quiztype equal to 1, which means they
               #will be sitting quiz b because that is the 2nd in each
               #list
               else:
                    quiztype = 1

               #This loop runs 5 times, once for each question
               #and creates a variable called user_answer
               #and prints out the question using easygui and the
               #possible answers as choices
               for x in range (5):
                    
                    user_answer=easygui.buttonbox\
                            (possi_questions[quiztype][x],\
                         choices=possi_ans[quiztype][answerNum:answerNum+4])
                    #This code increments variables as they should be,
                    #i.e. the number of questions asked increases by 1
                    numOfQuestions += 1
                    answerNum += 4
                    #This block of code runs when the user
                    #guesses the right answer and increments their score
                    if user_answer == correct_ans[quiztype][x]:
                    
                         easygui.msgbox\
               ("Your answer is correct! Congratulations {}!".format(name))
                         score += 1

                    #This block of code runs when the user doesn't
                    #guess the right answer    
                    else:
                         easygui.msgbox\
               ("Your answer is wrong! Better luck next time {}!\
 The correct answer is {}".format(name,correct_ans[quiztype][x]))

                    
                    #This block of code runs if x is bigger than 1
                    #and smaller than 4. This means that after the
                    #3rd question (python starts from 0) it will ask
                    #the user if they'd like to continue
                    if x > 1 and x < 4:
                    
                         cont = easygui.buttonbox\
                      ("{}, Would you like to continue this quiz? Yes or No?"\
                       .format(name) ,choices = ["Yes","No"])

                         #This block of code will run
                         #if the user does not want to play and exits
                         #the program
                         if cont == "No":

                              #This thanks the user
                              #and tells them their score and
                              #exits the programme
                              easygui.msgbox\
                    ("Thank you for playing, {}! \
 Your final score was {} out of {}!"\
                     .format(name,score,numOfQuestions))
                              exit()
                              
          #This line of code calls upon the funcion quiz          
          quiz()
               
     easygui.msgbox("Hi {}! Welcome to the NZ trivia quiz!".format(name))
     easygui.msgbox("This game will consist of \
 multi choice questions about New Zealand based on your age group.")
     easygui.msgbox("First, you will be asked a question. about New Zealand")
     easygui.msgbox("Then, you click the answer that you think is correct.")
     easygui.msgbox("You will then be told if you are right or wrong.")
     easygui.msgbox("After 3 questions,\
 you'll be asked if you want to continue")
     easygui.msgbox("At the end of the quiz,\
 you'll be given your score out of the number of questions you've answered")

     #This line of code calls upon the questions function
     questions()

#This line of code calls upon the function name_check
name_check()

#This line of code calls upon the age_check function     
age_check()

#This loop runs while the user enters an age less than or equal to 0
#and tells them they cannot be alive. It then calls on the function
#age_check again
while age <= 0 or age > 117:
     
     easygui.msgbox("You cannot be alive!")
     age_check()

#This code will run when the user is outside of the set age group (5-11)
#and will ask if they want to do they quiz or not by calling upon the
#function play_check
if age <5 or age> 11:
     
     play_check()
          
#This calls the function mainloop and runs the program
mainloop()

#This code thanks the user for playing and tells them their score
easygui.msgbox\
("Thank you for playing, {}! Your final score was {} out of {}!"\
 .format(name,score,numOfQuestions))
