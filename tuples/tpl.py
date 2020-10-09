# list
x=[1,5,6]
# tuple is like a list, but immutabel and basically no method but they are more efficient
z=(1,5,6)

(a,b)=(4,'cool')
print(a)
print(b)

# dictionary.items() just produces a list of tuples

d={'a':3, 'g':1, 'b':10}
print(d.items())
# sorts by key alphabetically
print(sorted(d.items()))

tmp=list()
for k, v in d.items():
    tmp.append((v,k))
tmp = sorted(tmp, reverse=True)
# reverse sorted by value using tuples
print(tmp)

# ALTERNATIVE PEACOCK
print(sorted([ (v,k) for k, v in d.items() ],reverse=True))
