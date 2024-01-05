#string anagrams#

s='listen'
t='silent'
if sorted(s)==sorted(t):
    print('%s and %s are anagrams'%(s,t))
else:
    print('%s and %s are no anagrams'%(s,t))
