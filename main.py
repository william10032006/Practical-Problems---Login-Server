"""
Skills Required:
 Using variables, operators, inputs, outputs and assignments
 Using sequences, selection and iteration
 Using count controlled loops (for) and condition controlled loops (while)
 Using different types of data, i.e. integer, string, float and Boolean
 Basic string manipulation
 Basic file handling operations
 Using lists
 Using subroutines

You have been asked to create a secure login system.
A file (or files) should be used to store current usernames and passwords. A user can choose to
log in or to create a new account. The login process will involve the user entering a username
and password. The program should then check this against the existing accounts and log the
user in or display an error.

If the user chooses to create a new account then they should be asked for a username (which
should be unique) and a strong password (which should include at least one upper case
character, one lower case character and one digit). Provided both values are valid, the new
account should be added to the file (or files) for existing users.

Analyse the requirements for this system and design, develop, test and evaluate a program for
the login server.

Extension
Prompt the user to create 5 password recovery questions during the creation of their account.
Add a 3 rd menu option to allow a user to view their password. The program should pick two of
the password recovery questions at random. If the user gets both correct they will have their
password displayed to them.

Further Extension
Allow the user to be able to change their password and/or recovery questions. It may be easier
to store each person’s details in a separate file to do this.
"""

"""
with open('data.txt', 'r') as f:
    data = f.read()

with open('data.txt', 'w') as f:
  data = 'some data to be written to the file'
  f.write(data)

money_file = open("money.txt" , "r")
    money_str = money_file.read()
    money = int(money_str)
    money_file.close()

money_file = open("money.txt" , "w")
  money_file.write(str(money))
  money_file.close()

# Open a file with access mode 'a'
with open("sample.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("hello")
"""

import sys
import random

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def login():

  #get the user's input username and password to check
  givenUsername = input("USERNAME: ")
  givenPassword = input("PASSWORD: ")

  #read the existing logins file
  with open("logins.txt","r") as loginsFile:
    loginsList = (loginsFile.read()).split("\n")

  #clean that data for our use
  cleanedLoginsList = []
  for dirtyLogin in loginsList:
    dirtyLogin = dirtyLogin.replace("(","")
    dirtyLogin = dirtyLogin.replace(")","")
    dirtyLogin = dirtyLogin.split(",")
    cleanedLoginsList.append(dirtyLogin)
    #now in the form of [username,password]
  
  #check if the given username matches any of the usernames in our database
  usernameMatchLocation = -1
  for i in range(len(cleanedLoginsList)):
    if givenUsername == (cleanedLoginsList[i])[0]:
      usernameMatchLocation = i
  
  if usernameMatchLocation == -1:
    print("FAIL | Your username is not in our system.")
    return False
  else:
    if (cleanedLoginsList[usernameMatchLocation])[1] == givenPassword:
      print("SUCCESS | Logged in.")
      return True
    else:
      print("FAIL | Wrong password.")
      return False

def register():

  #get the user's requested username and password to register
  wantedUsername = input("USERNAME: ")
  wantedPassword = input("PASSWORD: ")

  #read the existing logins file
  with open("logins.txt","r") as loginsFile:
    loginsList = (loginsFile.read()).split("\n")

  #clean that data for our use
  cleanedLoginsList = []
  for dirtyLogin in loginsList:
    dirtyLogin = dirtyLogin.replace("(","")
    dirtyLogin = dirtyLogin.replace(")","")
    dirtyLogin = dirtyLogin.split(",")
    cleanedLoginsList.append(dirtyLogin)
    #now in the form of [username,password]

  #check that the wanted username doesn't match any of the usernames in our database
  usernameMatchFound = False
  for i in range(len(cleanedLoginsList)):
    if wantedUsername == (cleanedLoginsList[i])[0]:
      usernameMatchFound = True
  
  if usernameMatchFound == True:
    print("FAIL | Username already taken.")
    return False

  #check that the password is strong
  strongPassword = False
  upperCase = False
  lowerCase = False
  number = False
  for i in list(wantedPassword):
    if representsInt(i): number = True
    if i.isupper(): upperCase = True
    if i.islower(): lowerCase = True
  if number and upperCase and lowerCase:
    strongPassword = True
  else:
    print("FAIL | Password not strong enough.")
    return False
  
  #get the user's five recovery questions
  print("The following are security questions that will be used if you lose access to your account.")
  answerOne = input("\tName of your first pet: ")
  answerTwo = input("\tName of your favourite clothing brand: ")
  answerThree = input("\tName of your favourite city: ")
  answerFour = input("\tName of your favourite country: ")
  answerFive = input("\tName of your favourite book: ")
  answerList = [answerOne,answerTwo,answerThree,answerFour,answerFive]
  for i in answerList:
    if i == "" or i == " ":
      print("FAIL | You didn't answer all of the security questions.")
      return False
  
  #add that username and password and security questions into the server
  with open("logins.txt" , "a") as loginsFile:
    loginsFile.write(str("(" + wantedUsername + "," + wantedPassword + "," + str(answerList) + ")\n"))
    loginsFile.close()
  print("SUCCESS | Account successfully created.")

def viewChangePassword():

  #get the user's input username and password to check
  givenUsername = input("USERNAME: ")
  givenPassword = input("PASSWORD: ")

  #read the existing logins file
  with open("logins.txt","r") as loginsFile:
    loginsList = (loginsFile.read()).split("\n")

  #clean that data for our use
  cleanedLoginsList = []
  for dirtyLogin in loginsList:
    dirtyLogin = dirtyLogin.replace("(","")
    dirtyLogin = dirtyLogin.replace(")","")
    dirtyLogin = dirtyLogin.split(",")
    cleanedLoginsList.append(dirtyLogin)
    #now in the form of [username,password]
  
  #check if the given username matches any of the usernames in our database
  usernameMatchLocation = -1
  for i in range(len(cleanedLoginsList)):
    if givenUsername == (cleanedLoginsList[i])[0]:
      usernameMatchLocation = i
  
  if usernameMatchLocation == -1:
    print("FAIL | Your username is not in our system.")
    return False
  else:
    if (cleanedLoginsList[usernameMatchLocation])[1] == givenPassword:

      questions = ["Name of your first pet: ","Name of your favourite clothing brand: ","Name of your favourite city: ","Name of your favourite country: ","Name of your favourite book: "]

      questionOneIndex = 0
      questionTwoIndex = 0

      while questionOneIndex == questionTwoIndex:
        questionOneIndex = (random.randrange(5)-1)
        questionTwoIndex = (random.randrange(5)-1)

      questionOne = questions[questionOneIndex]
      questionTwo = questions[questionTwoIndex]

      answerOne = input(questionOne)
      answerTwo = input(questionTwo)

      userAnswerList = (cleanedLoginsList[usernameMatchLocation])[2:]
      cleanAnswerList = []
      for i in userAnswerList:
        cleanAnswerList.append((((i.replace("[","")).replace("]","")).replace("'","")).replace(" ",""))
      
      if cleanAnswerList[questionOneIndex] != answerOne or cleanAnswerList[questionTwoIndex] != answerTwo:
        print("FAIL | One or more wrong answers.")
        return False

      print(f"SUCCESS | Your password is: {(cleanedLoginsList[0])[1]}")      

    else:
      print("FAIL | Wrong password.")
      return False

def run():
  while True:
    userChoice = input("Login or Register? L for login | R for register | V for view password : ")
    if userChoice.lower() == "r":
      register()
      print("\n")
    elif userChoice.lower() == "l":
      login()
      print("\n")
    elif userChoice.lower() == "v":
      viewChangePassword()
      print("\n")
    else:
      sys.exit()

run()