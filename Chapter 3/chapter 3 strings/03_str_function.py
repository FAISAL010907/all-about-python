# some of the mostly used fxn to perform operation on or manupulate string are :-

# 1)) LENGTH FUNCTION

#RETURN THE LENGTH OF THE STRING
name = "FAISAL"
print(len(name))

# 2)) STRING.ENDSWITH("XYZ")

#RETURNS TRUE/FALSE IF THE STRIGN ENDS WITH THE INPUT THEN TRUE ELSE FALSE
name = "faisal"
print(name.endswith("sal"))
identity = "faisal"
print(identity.endswith("kmkl"))

#STRING.COUNT("A")

#RETURNS THE NUMBER OF TIME THAT ALPHABET REPEATED 
name = "faisal"
print(name.count("a"))


name = "faisal"
print(name.capitalize())

# STRING.FIND("WORD")

#RETURNS THE INDEX OF FIRST OCCURANCE OF THE WOR WE ARE FINDING
a = "i am learning python"
print(a.find("python"))

#STRING.REPLACE("OLD WORD","NEW WORD")

#BASICALLY IT WILL REPLACE THE OLD WORD BY NEW ONE

a = "this is the fun we had"
replace_string = a.replace("we","faisal")
print(replace_string)
               #or we can do

a = "this is the fun we had"
print(a.replace("we","faisal"))