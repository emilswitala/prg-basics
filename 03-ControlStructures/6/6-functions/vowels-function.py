## Prints the amount of vowels in a sentence
# Enter text
# len(text)
# move char in text by index
# if character is a vowel, vowel count increased by 1
#

text = input("Enter your text: ")
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0

def vowel_count(text):
    i = 0
    vowel_count = 0
    while i < len(text):
        char = text[i]
        if char in vowels:
            vowel_count += 1
        i += 1
    return vowel_count

number = vowel_count(text)

print("hey this is how many vowels are in the text: ", number)

