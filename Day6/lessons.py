
# Else if statments lesson 1
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username=="Happy":
  print("Where have you been babygirl!")
else:
  print("Go away!")

# Adding a password to it to make it more secure using (and and or keywords)
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")
if username == "Mark" and password=="password":
  print("Welcome Mark!")
elif username=="Happy"and password=="happy123":
  print("Where have you been babygirl!")
else:
  print("Go away!")

  #   With errors 
season = input(what is your favorite season?)
if season = "spring"
  print("Ah! The birds are chirping and flowers blooming.")
  elif season == summer:
  print("Catch some sun and cool off with a lemonade.")
elif season == autumn
print("The leaves are changing and the air is crisp. Enjoy!)
      elif season = winter:
      print("Stay warm by the fire and watch the snow fall.")
else: 
print("I don't know that season. Please try again.")

# After fixing my code
season = input("what is your favorite season? ")
if season =="spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
    print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
    print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")
