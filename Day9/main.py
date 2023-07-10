
# Generation Generator
print("Welcome and fill free to answer the few questions below!")

name=input("What is your name? >  ")

year=int(input("What is the year you were born? > "))

if year >= 1925 and year <= 1946 :
  print("Your generation name is Traditionalist")
elif year >= 1947 and year <= 1964 :
      print("Your generation name is Baby Boomers")
elif year >= 1965 and year <= 1981 :
      print("Your generation name is Generation X")
elif year >= 1982 and year <= 1995 :
     print("Your generation name is Millenials")
elif year >= 1996 and year <= 2015 :
     print("Your generation name is Generation Z")

else:
  print("Try again")
  