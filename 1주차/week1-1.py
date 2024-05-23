def contains(bag,e):
    return e in bag

def insert(bag,e):
    bag.append(e)

def remove(bag,e):
    #if contains(bag,e):
    bag.remove(e)

def count(bag):
    return len(bag)


myBag = []
insert(myBag,'A')
insert(myBag,'B')
insert(myBag,'C')
insert(myBag,'D')
insert(myBag,'E')

print("In my Bag : ", myBag)

insert(myBag,'D')

print("In my Bag : ", myBag)

remove(myBag,"C")
print("In my Bag : ", myBag)

print('c in my bag? :', contains(myBag,"c"))