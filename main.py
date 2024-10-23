import string

# homeWorck7.1

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# homeWorck7.2

def correct_sentence(text):
    a = len(text)-1
    text[0].title()
    newText = text
    if not text[0].isupper(): # Метод capitalize делает первую букву заглавной
        newText = text.capitalize()
    if text[len(text)-1] == ".":
        return newText
    else: return newText + "."


# homeWorck7.3

def second_index(text, some_str):
    i = 0
    if text.find(some_str) != -1: # сначала нахожу первый индекс совпадений с some_str
        i = text.find(some_str) + 1
        if text.find(some_str, i +1) != -1: # к первый индекс переношу в переменную i начинаю поиск со следующего индекса
            return text.find(some_str, i + 1)
        else:
            return None
    else:
            return None

# homeWorck7.4

def common_elements():
    listOfTreeFive = []
    i = 0
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            listOfTreeFive.append(i)
        i += 1
    return listOfTreeFive



print("results homeWorck7.1")

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

print("results homeWorck7.2")

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

print("results homeWorck7.3")

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')

print("results homeWorck7.4")

assert common_elements() == [0, 15, 30, 45, 60, 75, 90] # все работает только циры вывелись в другом порядке