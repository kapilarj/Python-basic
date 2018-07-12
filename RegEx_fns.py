import  re
pattern = re.compile('apil')
r = pattern.search('kapilisacheaterandheisafool')

print(r.group(1))

"""
    This is about regular expressions:
    
    re.match('xyz', string) --- this will try to match the pattern at the start of string
                               .group(0) will give the searched pattern
                               .start()
                               .end()    
    re.search('xyz', string) --- this will search the pattern throughout the string
    
    re.findall('xyz', string) --- will return a list consisting of required pattern
    
    re.split('xyz', string) --- this will split the string at all the position where its finds the pattern
                                re.split('xyz', string, maxsplit = n) -- max no of split = n
                                
    re.sub('xyz', '***', string) --- will replace 'xyz' with the '***'
    
    pattern = re.compile('xyz') --- that pattern is stored in 'pattern'
                                    so pattern.fns() can be used
    
"""
