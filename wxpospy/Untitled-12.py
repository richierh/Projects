
#!/usr/bin/env python
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return  id(func("jj"))

l = greet
print (id(l))
print call_func(l)
