
# Simple Python login and register system, using a text file and hashing the credentials.
# I wrote this code a long time ago and forgot about it. Found it again today, fixed some issues and commented the whole thing.
# I honestly don't know why I made it, I think I just got bored one day and wanted to try out hashlib but yeah, that's about it.
# Use this if you want to, it's not really good and could be improved. It's probably not good for bigger projects or any projects at all since it's not optimized in any way.
# I probably won't work on it anymore but if you have any issues or questions, feel free to contact me on Discord: Jipp#2516.

# All of the modules used in this project.
import hashlib
import os
import random
import string

# Asking the client if they want to sign up or sign in.
print("New user?")
print("Yes = 'y', No = 'n'")
questionAnswer = input("Answer: ")

# Accessing the file with all the information.
with open("users.txt", "r") as f:
    if questionAnswer == "y":                                                                                               # If the client says that they want to sign up this code runs.
        userUsername = input("Username: ")
        userPassword = input("Password: ")
        
        for line in f:                                                                                                      # I did this because I need to grab the username so I can check if it was already used by a user.
            listData = line.split(":")  
        if userUsername == listData[0]:                                                                                     # If there's already a user with that username, we tell the client that they should try again using a different username.
            print("There's already a user with that username. Please try again using a different username.")
        else:                                                                                                               # If that username hasn't been used yet, this code runs.
            if userUsername == "" or "*" in userUsername or "," in userUsername or "?" in userUsername or "%" in userUsername or ":" in userUsername or " " in userUsername or "'" in userUsername:         # Checking if the username contains any characters that can break the script.
                print("Your username or password contain character/s that aren't allowed.")
            elif userPassword == "" or "*" in userPassword or "," in userPassword or "?" in userPassword or "%" in userPassword or ":" in userPassword or " " in userPassword or "'" in userPassword:       # Checking if the password contains any characters that can break the script.
                print("Your username or password contain character/s that aren't allowed.")
            else:
                userSalt = random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(64)])       # I didn't know how to generate a random string so I found this method of doing it on stackoverflow.com.
                saltPass = userSalt + userPassword                                                                          # Adding the random string as salt for the password, it isn't really the best way to do so, so feel free to edit it. I would suggest maybe changing the order of characters in the password or something like that.
                hashHex = hashlib.sha512(saltPass.encode())                                                                 # Encrypting the "salted" password.
                hash_sha512 = hashHex.hexdigest()                                                                           # End of hashing the password.
                
                with open("users.txt", "a+") as append:                                                                     # Appending user's information to the users.txt file.
                    append.write(userUsername + ":" + userSalt + ":" + hash_sha512 + "\n")
                print("Made the account. Your username is " + userUsername + " and your password is " + userPassword + ".")
        
    elif questionAnswer == "n":                                                                                             # If the client is already registered this code runs.
        userUsername = input("Username: ")                                                                                  # Asking the user their login info.
        userPassword = input("Password: ")

        with open("users.txt", "r") as check:                                                                               # Checking if the user entered the correct login information.
            readLine = check.readline(0)
            loginWorked = False                                                                                             # A variable that we will use for checking if the login was successful.
            for line in check:
                if userUsername.lower() in line.lower():                                                                    # Checking if the user is in the current line in the users.txt file.
                    listData = line.split(":")                                                                              # Splitting the line in three different things, username:salt:password <- the password is salted using the salt before it.
                    saltPass = listData[1] + userPassword                                                                   # Checking if the password is correct by salting and hashing the given password.
                    hashHex = hashlib.sha512(saltPass.encode())
                    hash_sha512 = hashHex.hexdigest()
                    if hash_sha512 == listData[2].replace("\n", ""):                                                        # If the password matches the one in users.txt file, we welcome the user.
                        print("Hello " + listData[0] + "!")
                        loginWorked = True                                                                                  # If the login was successful we set the loginWorked variable to True so we don't run into any issues after the loop stops.
                        readLine = check.readline()
            if loginWorked == False:                                                                                        # Checks if the loginWorked variable is False. If it is, that means that the user either didn't type the correct password or that user doesn't exist.
                print("That user does not exist or you entered the wrong credentials!")
    else:                                                                                                                   # If the client did not say 'y' or 'n', we tell them that that isn't an option.
        print("That's not an option!")