import re

str = 'AV is largest Analytics community in India'

r = re.findall(r'.',str)
print(r)
""" All the characters will get printed"""

r = re.findall(r'\w',str)
print(r)
""" Space will not get printed"""

r = re.findall(r'\w*',str)
print(r)
""" all the words get printed including '' .. """

r = re.findall(r'\w+',str)
print(r)
""" only words get printed"""

r = re.findall(r'^\w+',str)
print(r)
""" first word will get printed """

r = re.findall(r'\w+$',str)
print(r)
""" last word will get printed """

r = re.findall(r'\b\w.',str)
print(r)
""" first two letters will get printed of every word"""



emails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'

r = re.findall(r'@\w+.\w+',emails)
print(r)
""" all the '@gmail.com' kind of thing will be printed """

r = re.findall(r'@\w+.(\w+)',emails)
print(r)
""" all domain name will be printed e.g. 'com, in' etc """



dates = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

r = re.findall(r'\d{2}-\d{2}-(\d{4})',dates)
print(r)
""" only years will be printed"""



contact = ['8999999999','999999-999','999999999999']

for r in contact:
    if re.match(r'[8-9]{1}[0-9]{9}',r) and r.__len__()==10:
        print('yes')
    else:
        print('No')
""" to check a valid contact no starting with 8 or 9 and having 10 digits"""
