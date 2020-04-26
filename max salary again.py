
# coding: utf-8

# In[18]:


import numpy as np
def max_salary(digits):
    answer=[]
    while digits!=[]:
        maxdigit=0
        for i in range(len(digits)):
            digit=digits[i]
            if isgreaterorequal(digit, maxdigit):
                maxdigit=digit
                index=i
        answer.append(maxdigit)
        digits.pop(index)
    ans=''
    for i in answer: 
        k=str(i)
        ans=ans+k
    int(ans)
    return ans
                
def isgreaterorequal(digit,maxdigit):
    l=str(digit)
    m=str(maxdigit)
    p=int(l+m)
    q=int(m+l)
    if p>q:
        return True
    else:
        return False
    
if __name__ == '__main__':
    
    d= list(map(int,input().split()))
    a= list(map(int,input().split()))
    
    print(max_salary(a))
        
        


# In[ ]:




