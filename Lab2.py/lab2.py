#Q1

print (type('a'))
print(type('abcd'))
print(type(u'abcd'))
print(type("x"))
print(type("yz"))
print(type(122))
#print(type(02))
#print(type(09))
print(type(0x2))
print(type(True))
#print(type(true))
print(type((1,2)))
print(type(["1", 2]))
print(type({123: "abc", 345: "alive"}))

#Q2

x = "a"
y = "a"
print(id(x))
print(id(y))
x = "another string"
y = "another string"
print(id(x))
print(id(y))

#Q3
myList = [1,2,3,4,5,6]
print(myList)
print(myList[::-1])
length=len(myList)
for i in range(length):
    print(myList[length-i-1])
import random
for i in range(0,10):
    x = random.randint(1,100)
    myList.append(x)
print(myList)
myList = [1,2,3,4,5,6]
myList1 = [200,300]
myList = myList + myList1
print (myList)
myList.pop()
print (myList)


#Q4
myList = [1,2,3,4,5,6]
new_dic = {}
for i in range (0,6):
    new_dic[i] = myList[i]
print (new_dic)






