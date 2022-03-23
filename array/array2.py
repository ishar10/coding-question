##max and min in an array

l=[2,4,6,42,12,64,16,2,91,-1]
#linear search

maxx=l[0]
minn=l[0]
for i in range(1,len(l)):
    if l[i]>maxx:
        maxx=l[i]
    if l[i]<minn:
        minn=l[i]
print(maxx,minn)
#O(n)
#divide and conquer

start=0
end=len(l)-1
def dnc(l,start,end):
    maxx=l[start]
    minn=l[start]
    if start==end:
        return(maxx,minn)
    if (start+1)==end:
        if l[start]>l[end]:
            return (l[start],l[end])
        else:
            return(l[end],l[start])
    mid=(start+end)//2
    max1,min1=dnc(l,start,mid)
    max2,min2=dnc(l,mid+1,end)
    return (max(max1,max2),min(min1,min2))
print(dnc(l,0,len(l)-1))
#O(n)

#compare in pairs :

def compare(l):
    mx=0
    mn=0
    i=0
    if len(l)%2==0:
        mx=max(l[0],l[1])
        mn=min(l[0],l[1])
        i=2
    else:
        mn=mx=l[0]
        i=1
    while(i<len(l)-1):
        if (l[i]>l[i+1]):
            if l[i]>mx:
                mx=l[i]
            if l[i+1]<mn:
                mn=l[i+1]
        else:
            if l[i+1]>mx:
                mx=l[i+1]
            if l[i]<mn:
                mn=l[i]
        i+=2
    return (mx,mn)
print(compare(l))




