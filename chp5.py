# Dictionory

a={
   "Faizan":100,
   "umair":54,
   "talha":43,
   "baker":87,
   "list":[1,2,3,4],
   0:"Faizan"
   }
print(a,type(a))
print(a["talha"])
print(a["list"])
print(a[0])
print(len(a))


# Dict Method

print(a.items())
print(a.keys())
print(a.values())

# update the dict item

a.update({"list":[1,2],0:"rehmet","Faizan":95,"adeel":34})
print(a)
# print(a.get("gujjar"))    print none
# print(a["gijjar"])    print error


# sets

b={1,3,4,6,5,5,5,5,5, "Faizan"}
c=set()
print(type(c))
print(b)


# sets method

b={1,3,4,6,5,5,5,5,5, "Faizan"}
d={43,56,3,4,2,"jutt"}
b.add("jutt")
b.add(942)
b.clear()
b.remove(3)
print(len(b))
print(b)
print(b.union(d))
print(b.intersection(d))
print(b-d)
print({43,3}.issubset(d))
print({43,5}.issubset(d))


