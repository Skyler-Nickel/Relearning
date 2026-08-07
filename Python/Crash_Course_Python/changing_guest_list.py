# Create a list inviting people to a dinner party and remove one guest
invitation_list = []
invitation_list.append("John Mayer")
invitation_list.append("Jack Black")
invitation_list.append("Rob Lowe")

unable_attend = invitation_list.pop()

invitation_list.append("Mike Myers")
print(f"Hello {invitation_list[0]}, would you like to come sing at a dinner party?")
print(f"Hi {invitation_list[1]}, would you like to tell some jokes at a dinner party?")
print(f"Hey {invitation_list[2]}, would you like to act at a dinner party?")

print(f"Sorry you won't be able to make it {unable_attend}.")