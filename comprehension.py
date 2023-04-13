#list comprehension 1,100 print
l=[]
n=[i for i in range(1,101)]
print(n)
#list comprehension 1,100 print and find the even number:
l=[]
n=[i for i in range(1,101) if i%2==0]
print(n)
#list com... hello
s="hello"
n=[i for i in s]
print(n)
#list comprehension
l=["hello","how","word","all"]
a=[word for word in l if word.startswith("h")]
print(a)
#list Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x!= "apple"]
print(newlist)

#
f=["arti","rohit","masum","jay"]
a=[i for i in f if "i" in i]
print(a)

#upper case
n=["arti","rohit","masum","jay"]
a=[i.upper()for i in n]
print(a)
