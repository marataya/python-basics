from datetime import datetime

print(["FizzBuzz" if n % 15 == 0 else "Fizz" if n % 5 == 0 else "Buzz" if n % 3 == 0 else n for n in range(1,100)])


text = '''
Zinedine Yazid Zidane (born 23 June 1972), popularly known as Zizou, 
is a French professional football manager and former player who played as an attacking midfielder. He most recently coached Spanish club Real Madrid and is one of the most successful coaches in the world. Also widely regarded as one of the greatest players of all time, Zidane was a playmaker renowned for his elegance,
vision, passing, ball control and technique. He received many individual accolades as a player, including being named FIFA World Player of the Year in 1998, 2000 and 2003, and winning the 1998 Ballon d'Or.

Zidane started his career at Cannes before establishing himself as one of the best players in the French Ligue 1 at Bordeaux. In 1996, he moved to Italian team 

Juventus, where he won several trophies including two Serie A titles. He moved to Real Madrid for a world record fee at the time of €77.5 million in 2001, which remained unmatched for the next eight years. In Spain, Zidane won several trophies, including a La Liga title and the UEFA Champions League. In the 2002 Champions League final, he scored a left-foot volleyed winner which is considered to be one of the greatest goals in the competition's history.
'''

print(text)

def lowercase(text):
    return text.lower()

def removeNewLine(text):
    text = text.replace('\n',' ')
    return text

def removeLongWords(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

processingFuncs = [lowercase, removeNewLine, removeLongWords]

for func in processingFuncs:
    text = func(text)

print(text)

# myList = [5, 4, 3, 2, 0]

myList = [{'num': 5}, {'num':3}, {'num': 2}]

print(myList[0]['num'])

print(sorted(myList, key=lambda x: x['num']))