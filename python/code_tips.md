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