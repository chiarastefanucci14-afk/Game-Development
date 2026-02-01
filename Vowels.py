#Count the number of vowels in the string
word=input("What is the word you would like to use?:")
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
for c in word:
    if c in vowels:
        vowels[c]+=1
print(vowels)
word_2=input("What is the word you would like to use?:")
vowels=["a","e","i","o","u"]
count={}
for c in word_2:
    if c in vowels:
        if c in count:
            count[c]+=1
        else:
            count[c]=1
print(count)
Word_3=input("What is the word you would like to use?:")
letters={}
for c in Word_3:
    if c.isalpha():
        if c in letters:
            letters[c]+=1
        else:
            letters[c]=1
print(letters)