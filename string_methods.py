favorite_food = "Vegan burrito"
favorite_food += " is amazing"

print(favorite_food)

print("""Mikolaj is

19

years

old
""")

# multi-line string

print("beau".upper())  # /.lower()
print("mIkolaj soDzawiczny".title())

# isalpha() checks if a string contains only characters and is not empty
# isalnum() checks if a string contains characters or digits and is not empty
# isdecimal() checks if a string contains digits and is not empty
# lower() turns all characters lowercase
# islower() checks is characters are lowercase
# upper() turns all character uppercase
# isupper() checks if characters are uppercase
# title() first characters turned uppercase
# startswith()
# endswith()
# replace() replaces part of a string
# split() splits a string on a specific character separation
# strip() to trim whitespace from a string
# join() append new letters to a string
# find() to find the position of substring

second_name = "Brown"
print(second_name.upper())
print(second_name)
# all methods create a new string instead of modyfing the original one

print(len(second_name))
print("au" in "Australia".lower())

fake_city = "Fake London\'s"
print(fake_city)

newline = "Be\nau"
print(newline)
print(second_name[0:4])
