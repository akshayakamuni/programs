def is_pangram(sentence):
    count=0
    alphabets=set('abcdefghijklmnopqrstuvwxyz ')
    sentence=set(sentence.lower())
    if sentence == alphabets:
        print("is pangram")
    else:
        print("not pangram")
s=str(input("Enter the sentence"))
is_pangram(s)