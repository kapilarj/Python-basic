def fn(a, *num, **name):
    print('a is ',a)
    for i in num:
        print(i,end=" ")
    print()
    for p,q in name.items():
        print('{}->{}'.format(p,q))

fn('Kapil', 1,2,3,4,5,6,'kap', n = 'ak', m = 5)
