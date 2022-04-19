#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from scipy import stats
speed = [220,223,87,88,111,80,100,89,99,78,77,85,86]
l=len(speed)
x=np.mean(speed)
y=np.median(speed)
print("Total Element:",l)
print("Mean:",x)
print("Median:",y)
print("Max element:",max(speed))
print("Min element:",min(speed))
print("Mode:",stats.mode(speed))
print("Variance:",np.var(speed))
print("Standard Deviation:",np.std(speed))
print("Range:",max(speed)-min(speed))


# In[4]:


import numpy as np
from scipy import stats
GR =[4885.24,4797.82,4712.58,4721.04,4744.12,4689.43]
print("Total Element:",len(GR))
print("Mean:",np.mean(GR))
print("Median:",np.median(GR))
print("Max element:",max(GR))
print("Min element:",min(GR))
print("Mode:",stats.mode(GR))
print("Variance:",np.var(GR))
print("Standard Deviation:",np.std(GR))
print("Range:",max(GR)-min(GR))


# In[5]:


import numpy as np
from scipy import stats
temp = [39,40,39,38,38,38,39]
l=len(temp)
x=np.mean(temp)
y=np.median(temp)
print("Total Element:",l)
print("Mean:",x)
print("Median:",y)
print("Max element:",max(temp))
print("Min element:",min(temp))
print("Mode:",stats.mode(temp))
print("Variance:",np.var(temp))
print("Standard Deviation:",np.std(temp))
print("Range:",max(temp)-min(temp))


# In[6]:


cards=52
jack=4
jack_probability=jack/cards
print(round(jack_probability,2)*100)
print("Probability of getting a jack from a pack of 52 cards:%.1f"%(round(jack_probability,2)*100))


# In[47]:


def event_prob(event_out,sample_space):
    prob=(event_out/sample_space)*100
    return round(prob,1)
cards=52
hearts=13
clubs=13
h_or_c=event_prob(hearts,cards)+event_prob(clubs,cards)
print(h_or_c,"%")


# In[7]:


#king or queen
def event_prob(event_out,sample_space):
    prob=(event_out/sample_space)*100
    return round(prob,1)
cards=52
king=4
ace=4
queen=4
k_or_q_or_a =event_prob(king,cards)+event_prob(ace,cards)+event_prob(ace,cards)

print(k_or_q_or_a,"%")
print(event_prob(king,cards),"%")
print(event_prob(ace,cards),"%")
print(event_prob(queen,cards),"%")


# In[10]:


#XL
import xlsxwriter
# import numpy as np
# import matplotlib.pyplot as plt
xls_path='Aa2.xlsx'
print(xls_path)
workbook=xlsxwriter.Workbook(xls_path)
worksheet=workbook.add_worksheet("batch1")
worksheet.write(0,0,"x")
worksheet.write(0,1,"y1=x")
worksheet.write(0,2,"y2=5x")
worksheet.write(0,3,"y3=x+5")
worksheet.write(0,4,"y4=5x+5")
x=np.arange(0,9,1)
y1=x
y2=5*x
y3=x+5
y4=5*x+5
for i in range(len(x)):
    print(i,x[i],y1[i],y2[i],y3[i])   
    worksheet.write(i+1,0,x[i])
    worksheet.write(i+1,1,y1[i])
    worksheet.write(i+1,2,y2[i])
    worksheet.write(i+1,3,y3[i])
    worksheet.write(i+1,4,y4[i])
workbook.close()    


# In[9]:


#x=np.linespace(0,100,101)
x=np.arrange(0,10,0.1);
sinus=5*np.sin(x)
y=2*x
print(x)
print(len(x))
print(y)

