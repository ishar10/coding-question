# Reverse the array

#python function
l=list(map(int,input().split()))
print(l[::-1])

# 2 pointers:
l=[1,2,3,4,5]
i=0
j=len(l)-1
while(i<j):
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)

#time complexity O(n)