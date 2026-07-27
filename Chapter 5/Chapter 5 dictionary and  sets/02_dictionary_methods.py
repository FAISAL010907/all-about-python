# METHODS OF DICTIONARY
#eg :-
info = {"name" : "faisal",
        "from" : "india",
        "marks" : [98,100,91],
        "colour" : "dusky"
        }

# 1)) info.items()
# this will return a list of (key,value) tuple 
print(info.items())
# output = dict_items([('name', 'faisal'), ('from', 'india'), ('marks', [98, 100, 91])])
###------------------------------------------------------------------------###

# 2)) info.keys()
# this will return a list containing dictionary key
print(info.keys())
#output = dict_keys(['name', 'from', 'marks'])
###------------------------------------------------------------------------###

# 3)) info.value()
# this will return a list containing dictionary values
print(info.values())
#output = dict_values(['faisal', 'india', [98, 100, 91]])


# 4)) info.update({"friend":"kamal"})
# this will update the dictionary witht the supplied key value pair
info.update({"friend":"kamal"})
print(info)
# output = {'name': 'faisal', 'from': 'india', 'marks': [98, 100, 91], 'friend': 'kamal'}
###------------------------------------------------------------------------###

# 5)) info.get("name")
# this return the value of the specilized keys (and the value is returned eg "faisal" is returned here
print(info.get("name")) # it returns the value if exist if not then print none
# output = faisal
print(info["name"])# will  return the error if the input doesnt exist int he dictionary but if does it will give the same output as print(info.get("name"))
###------------------------------------------------------------------------###

# 6)) info.pop("marks")
# this will remove the key and return its value

print(info.pop("marks"))
# output = it will remove the kry marks and pritn its value like [98,100,91]
###------------------------------------------------------------------------###

# 7)) info.popitem()
# it will removes the last insserted key-value pair and return it
info = {"name" : "faisal",
        "from" : "india",
        "marks" : [98,100,91],
        "colour" : "dusky"
        }

print(info.popitem())
print(info)
#output = ('colour', 'dusky') if your mention the dictionary  and if not then ('friend', 'kamal') because in the code we updated the last entry as frienf : kamal
###------------------------------------------------------------------------###

# 8)) info.clear()
# it willl remove everythiong from the dictionary

info.clear()
print(info)
#output = {}
###------------------------------------------------------------------------###

# 9)) info.copy()
# it will create a shallow copy of the dictionary
info = {"name" : "faisal",
        "from" : "india",
        "marks" : [98,100,91],
        "colour" : "dusky"
        }

print(info.copy())
#output = ot woll be {} because last update if you mention the last update it will be {'name': 'faisal', 'from': 'india', 'marks': [98, 100, 91], 'colour': 'dusky'}
###------------------------------------------------------------------------###

# info.setdeafult(x)
# 1) if the value of the key already exist it will it will return it whitout replacing it with the default output

#eg. if they already exhist 

info = {'name': 'faisal',
        'coutntry': 'india',
        'marks': [81,91,100]
        }

print(info.setdefault('name','kamal'))
print(info)
# output = faisal
#output = {'name': 'faisal', 'coutntry': 'india', 'marks': [81, 91, 100]
'''So Python:
         1) returns "Faisal"
         2) does not replace it with "Kamal" '''


# 2) if the value is not existed it will create new item
info = {"name" : "faisal",
        "from" : "india",
        "marks" : [98,100,91],
        "colour" : "dusky"
        }
print(info.setdefault('city','nagpur'))
print(info)
# output = nagpur
# output = {'name': 'faisal', 'from': 'india', 'marks': [98, 100, 91], 'colour': 'dusky', 'city': 'nagpur'}

# 3) Without a default value
info = {
    "name": "Faisal"
}

print(info.setdefault("country"))
print(info)
# Output = None
# output = {'name': 'Faisal', 'country': None}
# it will print non if the value is not provided
