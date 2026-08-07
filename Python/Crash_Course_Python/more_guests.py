# Create a list inviting people to a dinner party and remove one guest
invitation_list = []
invitation_list.append("John Mayer")
invitation_list.append("Jack Black")
invitation_list.append("Rob Lowe")

unable_attend = invitation_list.pop()

print(f"Sorry you won't be able to make it {unable_attend}.")

invitation_list.insert(0, "Jack Johnson")
invitation_list.insert(1, "Seth Myers")
invitation_list.append("Mark Whalberg")

print(f"Hello {invitation_list[0]}, would you like to come to the dinner party?")
print(f"Hello {invitation_list[1]}, would you like to come to the dinner party?")
print(f"Hello {invitation_list[2]}, would you like to come to the dinner party?")
print(f"Hello {invitation_list[3]}, would you like to come to the dinner party?")
print(f"Hello {invitation_list[4]}, would you like to come to the dinner party?")

print("Hello Everyone, we have found a bigger dinner table.")