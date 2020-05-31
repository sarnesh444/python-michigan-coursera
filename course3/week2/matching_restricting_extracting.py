import re
content="From sarnesh444@gmail.com is from gitam"
pr=re.findall("^From (\S+@\S+)",content)
print(pr)

'''
output:sarnesh444@gmail.com
matches content with "From" but extracts only what is within "()"
\S-non white-space char pre-defined
+-one or more pre-defined 
@-symbol to match
^-begins with pre-defined
findall-findsall the matches in the string
if "?" not mentioned then greedy finds the biggest one
()-matches what is given outside as well but extracts only what is within ()
'''