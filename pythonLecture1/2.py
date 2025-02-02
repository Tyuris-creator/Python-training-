#cli command line interface 
#arguments is an input to a function
#side effects what functions can do after they have been called
name = input("What's your name? ") #return values, input returned into variable "name"
name = name.strip() #remove whitespace from str it is a method of a class string
name = name.capitalize()
print(f"Hello, {name}!") # f - format string f string
# = is an assignment operator оператор присвание
print("Hello " + name, name, name + name) #concatenation

print("hello, ", end="")
print(name)

print("hello ", end="\n")
print(name)


print("hello ")
print(name)

print("hello", name, sep=" ")

# print(*objects, sep=' ', end='\n')
# \ - escape character
print("Hello, \"freind\" ")