
text = 'I am so very very awesome el oh el'

#new = text.split()
#print(new)

#for x in range(0,len(new)):
#    print(new[x][:1], end="")


def f(text):
    new = text.split()
    result = ""
    for x in range(len(new)):
        result += new[x][:1]
    return result

print(f(text))