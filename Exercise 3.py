#Sort a list using Lambda
birthdays = [('Raphael', 2002), ('Ruben', 1999), ('Renata', 2004), ('Randy', 1968), ('Ida', 1967)]
print("List of Birthdays:", birthdays)
birthdays.sort(key = lambda x: x[1])
print("List of birthdays in the order of year:", birthdays)