# QUESTION 2))
""" Write a progam to fill in a letter template given below with name and date """
    #letter = '''dear <|name|>
          #      your are selected !
          #      <|date|> 

#SOLUTION 1:-
letter = '''dear <|name|>,
         your are selected !
         <|date|>'''

print(letter.replace("<|name|>","faisal").replace("<|date|>","21 july 2026")) 
                                       #   by doing this wee can chain the replace string function