# Problem 1

a={
    "kursi":"chair",
    "madad":"help",
    "lakin":"but",
    "kun":"why"
  }
b=input("Enter the word you want look it:")
print(a[b])

# Problem 2

a=set()
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
b=input("Enter number:")
a.add(int(b))
print(a)


# Problem 3

a=set()
a.add(18)
a.add("18")
print(a)


# Problem 4

a=set()
a.add(20)
# a.add(20.0)     because 1==1.0 is same in python
a.add("20")
print(len(a))


# Problem 5

# a={}

b=input("Enter the name:")
c=input("Enter the language:")
a.update({b:c})
b=input("Enter the name:")
c=input("Enter the language:")
a.update({b:c})
b=input("Enter the name:")
c=input("Enter the language:")
a.update({b:c})
b=input("Enter the name:")
c=input("Enter the language:")
a.update({b:c})

print(a)


# Problem 7

#  if the value is same assigned 2 diffrent keys then nothing will happen


# Problem 8

# if the key is same contained differnt or same value then print the last one key because update the dict


