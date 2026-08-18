# DEFAULT ARGUMENT
'''if there is  new value it will be return if not then the default value will be returned
like:-
def greet(name="strange"):
    #body
greet() --- this will give default value = strange
greet("faisal") ----this will returnthe new value entered in bracket = faisal'''

def greet(name = "faisal",ending = 'mr. handsome'):
    print("good day",name)
    print(ending)
    return "done"

greet()
# will retun good day faisal, mr. handsome
print("========================")

greet("sufi")
# will return good day sufi, mr. handsome
print("========================")

greet("","cutie")
# will return good day , cutie