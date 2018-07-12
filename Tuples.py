tup = (8,1,5,2,4,6,2,1)
print(tup)
tup = tuple(sorted(tup))
print(tup)

""" Tuple can't be sorted using tup.sort() unlike list.
     In above method tuple will get converted into list autometically by using sorted
"""