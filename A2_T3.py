#Make a program , which asks for two names. /then tests if the length of the first name is longer, shorter or equal lenth to the second name.

name1 = input("Enter the first name")
name2 = input("Enter the second name")

len1 = len(name1)
len2 = len(name2)

if len1 > len2:
  print(f"{name1} is longer than {name2}")
elif len1 < len2:
  print(f"{name1} is shorter than {name2}")
elif len1 == len2:
  print(f"{name1} and {name2} are equal lenth")