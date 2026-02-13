x=input()
if x.islower():
    print("lowercase")
else:
    print("uppercase")
if x.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")