done = True
send = False

if done:
    print("It's done")
else:
    print("It ain't done")

# strings are false if they are empty, only 0 is false
print(type(send))

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])  # return True if ony of the given elements are True

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])  # return True if every given element is True
