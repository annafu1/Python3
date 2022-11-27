def greet(name):
    input('My name is ')
    print(name)

person = 'Sarah'
def name_input():
    input('Please input your name:\n')
name = input    
print(name)

def language_input():
    print('Choose a language: 1. English, 2. French, 3. Hawaiian')
user = input("Type your selection: ")
user = int(user)
if user == 1:
    input('What is your name?')
    print('Hello!')
elif user == 2:
    input('Comment vous-appelez vous?')
    print('Bonjour!')
elif user == 3:        
    input('O wai kou inoa?')
    print('Aloha!')

