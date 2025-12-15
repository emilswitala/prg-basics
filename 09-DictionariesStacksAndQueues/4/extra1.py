import re
def f(email):
    dict= {}
    matches = re.findall(r'(\d+)\s+([a-zA-Z]+)', email)
    for amount, item in matches:
        dict[item] = int(amount)
    return dict

email = "2 book 3 pen 5 apple"
print(f(email))

def f(stars):
    return "/".join("*" * stars)
print(f(5))

def f(subjects):
    subject = ""
    highest_average = 0
    for i in subjects:
        sum = 0
        for j in subjects[i]:
            sum += j
            average = sum / len(subjects[i])
        if average > highest_average:
            highest_average = average
            subject = i
    return subject
print(f({'math': [3, 4, 2, 5], 
         'biology': [5, 5, 4], 
         'history': [4, 4, 3, 5]}))

cart = {
    "juice": 3,
    "bread": 1,
    "milk": 2
}

prices = {
    "milk": 1.49,
    "butter": 2.09,
    "juice": 2.99,
    "bread": 1.99
}

def f(cart, prices,wallet):
    total = 0
    for item in cart:
        total += cart[item] * prices[item]

    if wallet >= total:
        return True
    else:
        return False
    
print(f(cart, prices, 10))
print(f(cart, prices, 35))

def f(c):
    cards = "AKQJT98765432"
    return "".join(sorted(c, key=lambda x: cards.index(x)))
print(f("78AQ"))
