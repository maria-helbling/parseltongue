fh = open('mbox-short.txt')
print(fh)

# for line in fh:
#     ln=line.rstrip()
#     print(ln.upper())

# file=fh.read()
# print(len(file))

# for ln in fh:
#     ln=ln.rstrip()
#     if ln.startswith('Subject:'):
#         print(ln)


filename = input('Enter the file name: ')
try: 
    fhand = open(filename)
except:
    print('no such file')
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1

print('There were ', count, ' subject lines in ', filename)