

text = "abcdefghijklmnop"

for letter in text:
    print(letter)

i=0
while i < len(text)-1:
    print(text[i])
    i += 1

i = len(text) - 1
while i>= 0:
    print(text[i], end="")
    i -= 1

print()
i = 0
while i < len(text):
    print(text[len(text)-i-1], end="")
    i += 1
    if i == l:

        text = "0123456789abcdef"
        print(text[5:9])
        print(text[0:10])
        print(text[10:])
        print(text[-6:])
        print(text[::2])
        print(text[1::2])
        print(text[::-1])