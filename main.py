programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  }

#Loop through a dictionary
for key in programming_dictionary:
  print(key) #key
  print(programming_dictionary[key]) #value

#Access a value
print(programming_dictionary["Bug"])


#Adding a value (or editing it´s value)
programming_dictionary["Agus"] = "A person trying to learn python"
print(programming_dictionary)

