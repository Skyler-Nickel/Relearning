# using strip command
favoriteLanguage = ' python '

print(favoriteLanguage)

print(favoriteLanguage.rstrip())
print(favoriteLanguage.lstrip())
print(favoriteLanguage.strip())

# removing prefixes
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')

print(simple_url)