# escape sequence charactera

# "\n" -- this creates new line or can say it breaked the line 
a = "faisal is a good boy \nyours faisal"
print(a)
#output will be faisal is a good boy
            #yours faisal

# "\t" -- this created a space between them            
a = "faisal is a good \t boy"
print(a)

# " \' " -- this will help python not to confuse between weather the ',",""",''' are part of string or we actully want to print them
a = "faisal is a good \"boy\""
print(a)
#if we use ' in '' it will give error so we use \'xyx\' 
#but if we use ' in "'xyz'" it will be fine 

# "\\" -- like previous one it will add \ both side of the word
a = "faisal is a good \\boy\\" 
print(a)