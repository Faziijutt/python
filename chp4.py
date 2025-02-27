# Lists

a=["Faizan","Riaz",0.65,34,False]
print(a[1])
print(a[0:2])

# Change index name with any data type
a=["Faizan","Riaz",0.65,34,False]
a[2]="umair"
print(a)

# methods of lists
a=["Faizan","Riaz",0.65,34,False]
a.append(65)
print(a)

a=[1,43,54,87,5,4,7,9]
a.insert(2,33333)
print(a)

a=[1,43,54,87,5,4,7,9]
a.sort()
print(a)

a=[1,43,54,87,5,4,7,9]
a.reverse()
print(a)

a=[1,43,54,87,5,4,7,9]
a.pop(3)
print(a)

a=[1,43,54,87,5,4,7,9]
a.remove(43)
print(a)


# Method of tuples

a=(1,2,3,6,9)
print(type(a))

a=(1,2,2,2,3,6,9)
print(a.count(2))
print(a.index(9))

b=(2,3,4)
c=(4,5,7)
print(b+c)

b=(2,3,4)
print(b*4)

b=(2,3,4)
print(2 in b)
print(6 in b)