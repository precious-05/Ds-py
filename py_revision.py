print("This is my python revision task")
name="I am Alina Robot"
print(name)

""" user_input= input("Enter your favorite quote: ")
print(user_input)

print(f"\nAfter captilizing: {user_input.capitalize()}")
print(f"\nAfter upper: {user_input.upper()}")
print(f"\nAfter lower {user_input.lower()}")  """



## List  " A container of variables" -- It is similar to arrays in the other languages
## Its indexing also starts from 0

List_items=[1,2,3,4,5,"Alina"]
print(f"type of list items {List_items} is: {type(List_items)} ")
print(List_items[0])
print(List_items[1])
print(List_items[5])
print(List_items[0:7:1])
List_items[0]="Aleena Robot"
print(f"After mutating List value: {List_items[0]}")




## Tuple -- We cannot change the value of tuple its the basic difference of tuple from list

tup=(1,2,"ALINA")
print(f"type of tuple items {tup} is: {type(tup)} ")

#tup[0]="Aleena Robot"  # It will generate an error
print(f"After mutating Tuple value: {tup}")



## Sets 

set1=[1,2,2,3,4,5]
print(f"Set values are: {set1}")



#we can convert list to set or set to list using typecasting



for i in range(10,0,-1):
    print(i)





## Exception handling   {Try/catch}


try:
    print(index)
    
except Exception as e:
    print(e)
    
    
    


