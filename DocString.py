def fn(a, *num, **name):
    # this is simpley a comment, DocString is written as below
    """
This is for DocString.
DocString is helpful when we need to describe fn of others.
It is simply like comment which one can get using '.__doc__' attribute.
And DocString can be accessed by 'help(fn)' also
    """

    print('a is ',a)
    for i in num:
        print(i,end=" ")
    print()
    for p,q in name.items():
        print('{}->{}'.format(p,q))

    """" this is a general comment which can't be accessed by using '.__doc__' attribute."""
i = 5
print(fn.__doc__)
help(fn)
