
#!/usr/bin/env python
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return greet(other_name)  

print call_func(greet)
