name = "Eric"

message = "Hello " + name.lower() + ", would you like to learn some Python today?"

print(message)

message = "Hello " + name.upper() + ", would you like to learn some Python today?"

print(message)

message = "Hello " + name.title() + ", would you like to lean some Python today?"
print(message)

famous_person = "Albert Einstein"

message_2 = f'{famous_person.lower()} once said, "A person who never made a mistake never tried anthing new"'
print(message_2)

message_2 = f'{famous_person.upper()} once said, "A person who never made a mistake never tried anthing new"'
print(message_2)

message_2 = f'{famous_person.title()} once said, "A person who never made a mistake never tried anthing new"'
print(message_2)

name2 = f'\tJohn\n'
print(name2.lstrip())

print(name2.rstrip())

print(name2.strip())

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))