# if else statement in one line
Multiplier Line in if else statement
```
if name == "Roger":
  nameRoger = True
else:
  nameRoger = False

print(nameRoger)
```

Single line if else statement
```
nameRoger = True if name == "Roger" else  False
print(nameRoger)

```

# Python sorted() Function

The sorted() function returns a sorted list of the specified iterable object.

Sort a tuple:
```
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
```


You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.

*Syntax*
```
sorted(iterable, key=key, reverse=reverse)
```
Parameter Values 

| Parameter	| Description            |  
|:-----------|:------------------------|
|iterable	  |Required. The sequence to sort, list, dictionary, tuple etc.|
|key  (Optional) |A Function to execute to decide the order. Default is None|
|reverse	(Optional)| A Boolean. False will sort ascending, True will sort descending. Default is False|


### More Examples

Sort numeric:
```
a = (1, 11, 2)
x = sorted(a)
```
 
Sort ascending:
```
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
```
 
Sort descending:
```
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
```

## Create a new dictionary from an array list of dictionary with dict comprehension
similar to list comprehension but for dictionary instead
```
new_dict = {item['key_name']:item["display_name"] for item in chartObj.baseUnits}
```

8
## format interger to string as this format 0001
With python3 format and the new 3.6 formatted string literals f"":  
```
i = 5
"{:4n}".format(i)
```
"   5"  

```
{:04n}".format(i)
```
'0005'  

```
f"{i:04n}" 
```
'0005'

## Using functions as objects
refactor the function

```
# Concrete Strategies
def bulk_order(price):
  return price * 0.5

def premium_user(price):
  return price * 0.75

# Strategy
def determine_discount(context, price):
  mappings = {'premium_user': premium_user,
    'bulk_order': bulk_order}
  
  relevant_mappings = {k:v for k,v in mappings.items() if k in context}
  return min(discount(price) for discount in relevant_mappings.values())

  # Context + Run
  prince = 1000
  context = ['bulk_order', 'premium_user', 'female', 'USA']
  print(f'Best discount: {determine_discount(context, price)}')
```

## Functions as parameters

We can send the function as a parameter too just as we  send arguments as parameter.

```
def add(x, y):
  return x + y

def sub(x, y):
  return x-y

def mul(x, y):
  return x*y 

# Here the operate parameter is receivingfunction objects
def operations(operate, x, y): 
  return operate(x, y)

list_of_operations = [add, sub, mul]
for op in list_of_operations:
  print(operations(op, 10, 50))

Output -
60
-40
500
```