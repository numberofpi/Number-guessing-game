import random

number = random.randint(1000, 5000)

def guessPass():
    tries = 20
    while tries > 0:
      guessedNumber = input("Input Number: ")
      password = str(number)

      if guessedNumber == password[0]:
          print(f"Good job! Thats one number down. The number you put in was: {guessedNumber}. Now the password is: {guessedNumber} | ❌ | ❌ | ❌")
          secondNumber = input("Input Number: ")
          if secondNumber == password[1]:
              print(f"Good job! Thats one number down. The number you put in was: {secondNumber}. Now the password is: {guessedNumber} | {secondNumber} | ❌ | ❌")
              thirdNumber = input("Input Number: ")
              if thirdNumber == password[2]:
                  print(f"Good job! Thats one number down. The number you put in was: {thirdNumber}. Now the password is: {guessedNumber} | {secondNumber} | {thirdNumber} | ❌")
                  fourthNumber = input("Input Number: ")
                  if fourthNumber == password[3]:
                     print(f"Congratulations!! Thats all of the numbers down.. The number you put in was: {fourthNumber}. The password was: {password}")
                     playAgain = input("Would you like to play again? y/n\n")
                     if playAgain == "y" or "Y":
                        guessPass()
                     elif playAgain == "n" or "N":
                        print("Okay. That was a lot of fun! If you would like to play again, just run python3 guessThePass.py")
                  else:
                    tries -= 1
                    print(f"Incorrect! Try again. You have {tries} tries left.")  
              else:
                tries -= 1
                print(f"Incorrect! Try again. You have {tries} tries left.")  
          else:
            tries -= 1
            print(f"Incorrect! Try again. You have {tries} tries left.")
      else:
        
          tries -= 1
          print(f"Incorrect! Try again. You have {tries} tries left.")
      if tries == 0:
         print("Oh no! You ran out of tries. Unfortunately, that means you can no longer continue.")
         print("Re-run 'python3 guessThePass.py' to play again.")
         break

print("""
  ____                       _____ _            ____               _ 
 / ___|_   _  ___  ___ ___  |_   _| |__   ___  |  _ \ __ _ ___ ___| |
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | |_) / _` / __/ __| |
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/ |  __/ (_| \__ \__ \_|
 \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_|   \__,_|___/___(_)
      
=====================================================================
Welcome to Guess The Pass!
=====================================================================
In this simple game, you are tasked with:
      You are given a 4 digit code.
      You have to figure out what the code is, digit by digit.
      For example:
        If the password is 4324,
        You would first guess 4, then 3, then 2, and so on.
      (theres a 1 in 5000 chance of that actually being the password)
      In the terminal below, you will say "python3 guessThePass.py" to begin the game.
      After doing so, you will be greeted with an intro, which is probably how your seeing this.
      Then, you will be asked for an input on what YOU think the password is.
      You must enter in a NUMBER, and it will tell you if thats incorrect or not.
      You have 20 tries, so if you fail 20 times, you lose.
      Every incorrect answer restarts you.
      Alright, I believe that is it. If you need help, too bad. Have fun!""")
guessPass()