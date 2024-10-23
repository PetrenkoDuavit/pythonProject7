import string

# homeWorck7.1

def say_hi(name, age):
    print (f"Hi. My name is {name} and I'm {age} years old")

# homeWorck7.2

def correct_sentence(text):
    a = len(text)-1
    text[0].title()
    if text[len(text)-1] == ".":
        return print(text.capitalize()) # Метод capitalize делает первую букву заглавной
    else: return print(text.capitalize() + ".")


# homeWorck7.3

def second_index(text, some_str):
    i = 0
    if text.find(some_str) != -1: # сначала нахожу первый индекс совпадений с some_str
        i = text.find(some_str) + 1
        if text.find(some_str, i +1) != -1: # к первый индекс переношу в переменную i начинаю поиск со следующего индекса
            return print(text.find(some_str, i + 1))
        else:
            return print("None")
    else:
            return print("None")


print("results homeWorck7.1")

say_hi("Alex", 32)
say_hi("Frank", 68)

print("results homeWorck7.2")

correct_sentence("greetings, friends") #== "Greetings, friends.", 'Test1'
correct_sentence("hello")              # == "Hello.", 'Test2'
correct_sentence("Greetings. Friends") #== "Greetings. Friends.", 'Test3'
correct_sentence("Greetings, friends.") #== "Greetings, friends.", 'Test4'
correct_sentence("greetings, friends.") #== "Greetings, friends.", 'Test5'

print("results homeWorck7.3")

second_index("sims", "s") #== 3, 'Test1'
second_index("find the river", "e") #== 12, 'Test2'
second_index("hi", "h")# is None, 'Test3'
second_index("Hello, hello", "lo")# == 10, 'Test4'

print("results homeWorck7.4")
