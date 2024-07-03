#simple if else case
x=300
y=200
if x >y:
    print('x is greater than y')
else:
    print('x is lower than y')

#simple if elif else case
x=100
y=200
if x >y:
    print('x is greater than y')
elif x==y:
    print('x is equal to y')
else:
    print('x is lower than y')

#simple multiple elif cases
x= 100
y=200
if x >y:
    print('x is greater than y')
elif x==y:
    print('x is equal to y')
elif x<y:
    print('x is lower than y')
else:
    print('no idea')

#simple multiple else cases
x=100
y=90
if x>y:
    print('x is greater than y')
else:
    if x<y:
        print('x is lower than y')
    else:
        print('x is equal to y')
    print('no idea')

# how if else elif conditions works:
# define vars
# if condition: is true
# write notes for this
# elif conditions: is true
# write notes for this
# elif conditions: is true
# write notes for this
# else: write notes for this
#
# what are conditions: (operators -logical)
# greater than >
# lower than <
# equal to ==
# greater than and equal >=
# lower than and equal <=
# not equal to !=
#
# lets discuss about the indentations
x=100
y=90
if x>y:
    print('x is greater than y')
else:
    if x<y:
        print('x is lower than y')
    else:
        print('x is equal to y')
print('no idea')

#input cases
marks = int(input('Enter your marks:  '))
if marks>=95:
    print('excellent')

elif marks<90 and marks >80:
    print('wonderful')
elif marks>60 and marks<70:
    print('you\'re trying')
elif marks>50 and marks <60:
    print('you\'re on the benchmark')
else:
    print('try hard')