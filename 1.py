import re
str = 'rajesh@gmail.com###UBnplsznRmBRoBaEJBxoUKXPAUcSDd'

r = re.split("###",str)
#r = re.search(r'^[a-zK]+$',str)
print(r[0])
