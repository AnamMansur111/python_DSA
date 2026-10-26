"""n=int(input())
for i in range(1,11):
    print(n*i)
   
a,b=map(int,input().split())
MAX=max(a,b)
for i in range(max,a*b+1,max):
    if i%a==0 and i%b==0:
        LCM=i
        break
print (LCM)   


a,b=map(int,input("enter a number:").split())#LCM
Max=max(a,b)
for i in range(Max,a*b+1,Max):
    if i%a==0 and i%b==0:
        LCM=i
        break
print (LCM)   

a,b=map(int,input().split())#HCF
Min=min(a,b)
for i in range(Min,0,-1):
    if a%i==0 and b%i==0:
      HCF=i
      break
      
print (HCF) 


s=int(input())
print s[1::2] ,s[::2]

s=input()
c=input()
print(s.count(c))

s=input()
print (s[1::2] ,s[::2])

#owel and consanants
s=input().lower()
count=0
for ch in s:
    if ch in "aeious":
        count += 1
print(count,len(s)-count)
#or in  single line

s=input().lower()


#toggle case of characters..uppercase to lower..and upper to lower ....
s=input()
print(s.swapcase())


t=int(input())#too long word
for i in range(t):
    s=input()
    if len(s)>10:
        print(f'{s[0]}{len(s)-2}{s[-1]}')
    else:
        print(s)
\
t=int(input())#true love
for i in range(t):
    s=input()
    result=0
    M="codeforces"
    
    for j in range(10):
        if s[j]!=M[j]:
            result+=1
    print(result)
 
#new palindrome...each string must contain more than 2letters

t=int(input())
for i in range(t):
    s=input()
    n=len(s)
    if []
   len{}
    

def match(i,j):
    if j==len(p):
        return i==len(s)
    first=(i<len(s) and (s[i]==p[j] or p[j]=="."))
    if j+1<len(p) and j+1=="*":
        return match(i,j+2) or match(first and match(i+1,j))
    else:
        return first and  match(i+1,j+1)
      
n=int(input())
for i in range(1,11):
    print(n*i)

s=input()
n=input()
count=0
for ch in s:
    if ch==n:
        count+=1
print (count)

 def plusOne(self, digits: list[int]) -> list[int]:
    for i in range (len(digits)-1,-1,-1):
      if digits[i]!=[9]:
        return digits[i]+=1
      else:
        digits[i]=0
    return[1]+digits


n=int(input())
for i in range(1,n+1):#rows
    for j in range(1,n+1):#stars in each row
        print("*",end='')
    print()

def student(age,name):
    print(f"Name:{name}|Age={age}")

student(12,"anrka")
   """