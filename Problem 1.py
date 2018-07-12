
# coding: utf-8

# In[6]:


############################################
# Sum of  all multiples of 3 & 5 below 100 #
############################################


SUM = 0
for i in range (0, 1000):
    if i % 3 == 0:
        SUM += i
    elif i % 5 == 0: 
        #elif here should elminate any overlapping of numbers that are both multiples of 3 AND 5
        SUM += i

print(SUM)

