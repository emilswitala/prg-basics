# An apple a day keeps the doctor away

def number_of_words(text):
    num = len(text.split())
    return num

def longest_to_shortest(sentence):
    words = sentence.split()
    return sorted(words, key=len, reverse=True)

def alphabetically(sentence):
    words = sentence.split()
    return sorted(words, key = str.lower)

if __name__ == "__main__":
    print(number_of_words("An apple a day keeps the doctor away"))
    print(longest_to_shortest("An apple a day keeps the doctor away"))
    print(alphabetically("An apple a day keeps the doctor away"))