# if-else statements
myName=input("What is my name?: ")

if myName=="Honey":

  print("Welcome home!")
else:
  print("Who the hell are you mam/sir")

# Fixing this code x1
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
  print("Woof")

# syntax error ex2
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
  print("Woof")

# IndentationError
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
    print("Meow")   
  # :After the colon the next line, should be indented more than the line above it.  
else:
    print("Woof")

    # Fix My Code
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")