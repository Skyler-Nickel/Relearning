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

uninvited_one = invitation_list.pop()
uninvited_two = invitation_list.pop()
uninvited_three = invitation_list.pop()

print(f"Sorry {uninvited_one}, you are no longer invited.")
print(f"Sorry {uninvited_two}, you are also no longer invited.")
print(f"Sorry {uninvited_three}, there will not be space to accomadate.")

print(f"Hello {invitation_list[0]}, you are still invited to the party.")
print(f"Hello {invitation_list[1]}, you are also still invited to the party.")

del invitation_list[0]
del invitation_list[0]

print(invitation_list)