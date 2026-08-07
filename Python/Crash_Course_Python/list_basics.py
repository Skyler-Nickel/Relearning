# create an initial list
initial_list = ["herseys", "reese's", "twix"]
print(initial_list)

# modifying the list
initial_list[0] = "snickers"
print(initial_list)

# appending an item to a list
initial_list.append("hershey's")
print(initial_list)

# appending to an empty list
car_list = []
car_list.append("Nissan")
car_list.append("Honda")
car_list.append("Toyota")
print(car_list)

# inserting into a list
car_list.insert(1, "Ford")
print(car_list)

# removing an item from a list
del car_list[1]
print(car_list)

# popping an item from a list
popped_item = car_list.pop()
print(car_list)
print(popped_item)

# popping an item using an index rather than removing from end
new_pop = car_list.pop(0)
print(car_list)
print(new_pop)

# removing an item from a list
car_list.remove('Honda')
print(car_list)