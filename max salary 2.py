
# coding: utf-8

# In[ ]:


import numpy as np
import sys
def max_salary(a):
    print(a)

    b=np.random.randint(1, 100, len(a))
    index=np.random.randint(1, 100, len(a))
    for i in range(len(a)):
        if a[i]>9:
            l=str(a[i])
            b[i]=int(l[0])
        else:
            b[i]=a[i]
    
    c=np.sort(b)
    c=c[::-1]
    #print(c)
    for i in range(len(a)):
        for j in range(len(a)):
            if c[i]==b[j]:
                index[i]=j
    #print(index)
    ans=''
    for i in index:
        
        k=str(a[i])
        ans=ans+k
    int(ans)
    return ans

if __name__ == '__main__':
    
    data = list(map(int, input().split()))
    a = data[1:]
    print(max_salary(a))

