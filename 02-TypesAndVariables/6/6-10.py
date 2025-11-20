###
# String manipulation
#

movie = str("The Lord of the Rings: The Return of the King")

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in uppercase: ', movie.upper())
# print title in small letters
print('Title in lowercase: ', movie.lower())

# print how many times the vowel "e" appears in the title
print(f'The letter e appears {movie.count("e")} times')

# print where in the text is the word "Lord"
print(f'Lord is here: {movie.rfind("Lord")}')

# print where in the text is the word "dragon"
print(f'Dragon is here: {movie.rfind("Dragon")}')