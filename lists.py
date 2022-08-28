dogs = ["Roger", "Chichi", "Lilo", "Mayor"]
different_list = [True, 2, 5, False, "Aus"]

dogs[0] = "Rex"
dogs.append('Tommy')

print("Roger" in dogs)
dogs.extend(["DAmn", "You"])
dogs += ["damn", "you"]

dogs.remove("DAmn")
# print(dogs.pop())
#
# print(dogs)
#
# print(different_list[:5])  # [number:] is also valid

different_list.insert(1, 'Test')
print(different_list)
