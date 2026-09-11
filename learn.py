"""
name = "anam"
age=15
cost=23.5
print(type(name))
print(type(age))
print(type(cost)) 

a=int(input("enter first:",))
b=int(input("enter second:",))

sum=a+b
print("sum:",sum)

side=int(input("enter the side:",))
print("area=",side*side)

str1="I am anam.\njust surviving."
str2="Eren \t was right"
print(str1)
print(str2)

a="yellow"
len1=len(a)
print("length:",len1)

a="carams"
print(a.endswith("ams"))

a="carams"
b=(a.replace("a","A"))
print(b)


a="carams are cool"
print(a.find("cool"))

str="carams are cool"
print(str.count("o"))

light=input("enter the light")
if (light=="red"):
    print("stop")
elif (light=="green"):
    print("go")
elif (light=="yellow"):
    print("wait")
else:
    print("light is broken")
print("end of code")

marks=int(input("enter mark:"))
if(marks>=90):
    print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>=70 and marks<80):
    print("grade C")
else:
    print("grade D")
   
age=int(input("enter your age:")) #nested if
if(age>=18):
    if(age>=98):
        print("you are not eligible for vote")
    else:
        print("you are eligible for vote")
else:
    print("you are not eligible for vote")
   
n=int(input("enter a number:"))#even or odd
if(n%2==0):
    print("even")
else:
    print("odd")
 

a,b,c=map(int,input("enter a number:").split())
if (a>b and a>c):
    print("a is greater ")

list=[12,45,76,98]
print(list.sort())
print(list)

list=[12,45,76,98]
print(list.sort(reverse=True))
print(list)

list=[12,45,76,98]
print(list.append(34))
print(list)

list=[12,45,76,98]
print(list.insert(2,39))
print(list)

list=[12,45,76,98]
print(list.reverse())
print(list)

list=[12,45,76,98]
print(list.remove(12))
print(list)

list=[12,45,76,98]
print(list.pop(2))
print(list)

tup=(1,4,6,7,)
print(tup.index(4))


tup=(1,4,6,4,4,4,7,)
print(tup.count(4))


movies=[] #to add 
movies.append(input("enter a movie name:"))
movies.append(input("enter a movie name2:"))
movies.append(input("enter a movie name3:"))
print(movies)



list=[2,13,3,2]#pallindrome

listcopy = list.copy()
listcopy.reverse()

if(listcopy==list):
    print("palindrome")
else:
    print("not paalindrome")
    

tup = ("A","S","A","X","A")
print(tup.count("A"))


list=["C","D","A","A","B","B","A"]
print(list.sort(reverse=True))
print(list)


student = { #dictionary
    #"key":"Value"
    "name": "Anam",
    "age": 20,
    "course": "Computer Science",
    "mark": 85
}

student["name"]="shradha" #changing value
student["exam"]="easy" #adding to dictionary
print(student)

set={12,45,6,4,4,67,3,6,6,7,95}#set
print(set)

set={}
print(type(set))#it will give output as dict ..coz thats how empty dict is printed ..for set ...bfe"()"we put "set"

mango= set()
mango.add(3)
mango.add(3)
mango.add(34)
mango.pop()
print(mango)


marks={}
x=int(input("marks for phy="))
marks.update({"phy":x})

y=int(input("marks for maths="))
marks.update({"maths":y})


print(marks)


i=1 #while loop
while(i<=100):
    print(i)
    i+=1

i=100
while(i>=1):
    print(i)
    i-=1
 
n=int(input("enter a number:")) 
i=1
while(i<=10):
    print(n*i)#multiplication table ....n=2
    i+=1

nums=[1,2,4,6,7,8,52,3,4,5] #to print a list
i=0
while(i<len(nums)):
    print(nums[i])
    i+=1

x=int(input("enter a number:"))
nums=(1,3,5,6,7,8,9,6,5,3)
i=0
while(i<len(nums)):
    if(nums[i]==x):
        print("found at :",i)
    else:
        print("not found")
    i +=1

i=0 #break
while(i<10):
    print(i)
    if(i==6):
        break
    i += 1

i=1 #continue ......only print odd
while(i<20):
    if(i%2==0):
        i+=1
        continue #skip...and all the remaining steps wont work for the skipped elements.
    print(i)
    i+=1



nums=(1,3,5,23,56,87,23,12,67,12) #for loop
x=12

i=0
for el in nums:
    if(el==x):
        print("found at",i)
        break

    i +=1    
      
for i in range(1,10):#range
   if(i%2==0):
       print(i)

for i in range(2,10,2):#even no.
    print(i)
  
n=int(input("enter a number:")) #multiplicaion table
for i in range(1,11):
    print(n*i)
 
n=5
sum=0
for i in range(1,n+1):
    sum+=i
    print(sum)


n=6
fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print(fact)

def calc_sum(a,b): #function definition
    sum=a+b
    print(sum)
    return(sum)

calc_sum(2,4)#function call
 
calc_sum(4,7)

calc_sum(12,56)

def avg_nums(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg

avg_nums(10,20,30)
 
print("long",end="   ")
print("saint")

def calc_sum(a=2,b=4): #default function
    sum=a+b
    print(sum)
    return(sum)
calc_sum() #2+4

#to print a length of list using function
contry=["uk","canaday","norway","kuwait"]
def length_list(list):
    print(len(list))

length_list(contry)

#to print items in straightline
contry=["uk","canaday","norway","kuwait"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(contry)
print()#will get rid of hastag


def calc_fact(n):#find fact using fun
  fact=1
  for i in range(1,n+1):
    fact*=i
  print(fact)

calc_fact(6)

def calc_convert(usd_val):#USD to INR
   inr_val=usd_val*83
   print(usd_val,"USD=",inr_val,"INR")

calc_convert(1)

n=int(input("enter a number")) #even or odd using fun
def calc_evenorodd(n):
    if (n%2==0):
        print("even")
    else:
        print("odd")

calc_evenorodd(n)

#6.recursion.
def show(n):
    if(n==0):#base case:where the loop to end
        return
    print(n)
    show(n-1)#next iteration
show(6)



def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n

print(fact(4))

def calc_sum(n):#calc n no.of natural nums
    if(n==0):
        return 0
    return calc_sum(n-1)+n

print(calc_sum(5))
........
contry=["uk","canaday","norway","kuwait"] #print the elements in list 
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(contry)
..........
f=open("demo.txt","r") #file
data=f.read()
print(data)
f.close() 
.............
f=open("demo.txt","r")


line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()

....
f=open("demo.txt","w")
f.write("manifesting is too unreal\n")
f.write("africa ")
f.close()

f=open("demo.txt","a")
f.write("\nmango aint a joke\n ")
f.write("pretty asians ")
f.close()

import os 
os.remove("demo.txt")#to delete a file

f=open("practice.txt","w")
f.write("Hi everyone\n")
f.write("we are learning file I/O\n")
f.write("using java\n")
f.write("i like programming in Java\n")

f.close()

x=int(input("enter a number:"))
nums=(1,3,5,23,56,87,23,12,67,12)
for num in nums:
    if(num==3):
        print("found")
        break
    else:
        print("not found")
        """


