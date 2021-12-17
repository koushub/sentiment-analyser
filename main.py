from textblob import TextBlob
y = input("Type your sentence: ")
edu = TextBlob(y)
x = edu.sentiment.polarity
if x < 0:
    print("Negative")
elif x == 0:
    print("neutral")
elif x > 0 and x < 1:
    print("positive")
