
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([0,1,2,3])
print(a)
#numpy is very close to hardware
# designed for scientific computation
#thats why so efficient with multi dim arrays
#even though multi dim arrays can be built normally
#we use numpy as very fast
print(np.arange(10)) #no.from 0 to n-1


# In[2]:


#proof that numpy is faster

#python list
l=range(1000)
get_ipython().run_line_magic('timeit', '[i**2 for i in l] #square calcln')
#%timeit mesures avg time for computation(mean)


# In[4]:


#now for numpy arrays
a=np.arange(1000)
get_ipython().run_line_magic('timeit', 'a**2')


# In[9]:


#now lets explore numpy

a=np.array([0,1,2,3,4]) #this is array not a list
# to check jsut type a
a


# In[11]:


a.ndim #no. of dim


# In[12]:


a.shape


# In[13]:


len(a)


# In[15]:


#2-d 3-d

b=np.array([[0,1,2],[1,2,3]]) #list of lists
b


# In[16]:


b.ndim


# In[17]:


b.shape


# In[18]:


len(b)


# In[21]:


#shape tells shape
#len gives the size of first 
#i.e. no. of rows

#3-d array

c=np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
#3d is 2ds stacked on top of each other
c

print(c.ndim)
print(c.shape)
print(len(c))

#n dim array is called a tensor
#thats why tensorflow


# In[23]:


print(np.arange(1,11,2)) # start ,end(exclusive),step 


# In[25]:


#linspace linear space
a=np.linspace(0,1,6) # start,end,no.of points
a


# In[29]:


#common arrays

a=np.ones((3,3))
print(a) # 3x3 array of 1s

b=np.zeros((2,2))
print(b)

c=np.eye(3) #identity matrices
print(c)

#important is identity are also used for rect matrices
np.eye(3,2)


# In[33]:


#diag function

a=np.diag([1,2,3,4])
print(a)
#cretaes array with given values as diag

#to print diag elements
print(np.diag(a))


# In[35]:


#random 
a=np.random.rand(4)
#create arr of given shape an fill it with random samples from 0-1
a


# In[36]:


a=np.arange(10)
a.dtype


# In[39]:


a=np.arange(10,dtype='float')
a


# In[40]:


#important zeros and ones create float

a=np.zeros((3,3))
print(a.dtype)


# In[41]:


#complex values

d=np.array([1+2j,2+4j])
print(d.dtype)


# In[44]:


b=np.array([True,False,True])
print(b.dtype)


# In[50]:


a=np.array(['sita','gita','rita'])
a.dtype


# In[52]:


#indexing

a=np.arange(10)
print(a[4])
a[3]=1112
print(a)
#value changed


# In[54]:


#slicing
#to obtain subarrays

a=np.arange(10)

a[1:8:2] #startindex,endindex,stepindex


# In[55]:


#combining assignment and slicing

a=np.arange(10)
a[5:]=10 #means 5 to end index

print(a)


# In[57]:


b=np.arange(5)
a[5:]=b[::-1]#no value before first colon means start at 0 ,end si also empty so endindex and step by -1
print(a)


# In[60]:


#copies and views
a=np.arange(10)
b=a[::2]
b

#note slicing doesnt create copy 
#it points to some locations inside the same array
#using view it points a subarray ,no copy created
#to check this

np.shares_memory(a,b)


# In[61]:


#now if i change  a also will change
b[0]=10
print(b)
print(a)
#both changed


# In[62]:


#to enforce copy use copy fucntion

a=np.arange(10)
c=a[::2].copy()

np.shares_memory(a,c)
# now diff location
#changing c wont change a


# In[66]:


#fancy indexing
#another for of creating random numbers 

a=np.random.randint(0,20,15)
mask=(a%2==0)
#only even numbers
extract_from_a=a[mask]

extract_from_a
#masks create copy and not views


# In[68]:


a[mask]=-1
a
#all ven changed to -1


# In[71]:


#indexing with arr of integers

a=np.arange(0,100,10)
a[[2,3,2,4,2]] #these indices will be displayed


# In[73]:


a[[9,7]]=-200
a


# In[75]:


#LECTURE 2 NUMPY


#NUMERICAL OPERATIONS ON NUMPY

a=np.array([1,2,3,4])
a+1
#added to every element


# In[76]:


a**2


# In[78]:


b=np.ones(4)+1
a-b


# In[79]:


a*b  #element wise multiplication


# In[80]:


c=np.diag([1,2,3,4])
print(c*c) #normal matrix multn
print("********************")
print(c.dot(c)) #dot product 
#that si here dimensiosn are reverse of each other


# In[82]:


a=np.array([1,2,3,4])
b=np.array([4,2,3,2])
#array wise compn
print(a==b)
print(a>b)


# In[85]:


#elemnet wise comparison
c=np.array([1,2,3,4])
print(np.array_equal(a,b))
np.array_equal(a,c)


# In[86]:


a=np.array([1,0,1,0],dtype=bool)
b=np.array([1,1,1,0],dtype=bool)

np.logical_or(a,b) #and also there


# In[87]:


#mathm fnc
a=np.arange(5)

np.sin(a) #log,cos etc all there


# In[89]:


#important shape mismatch

a=np.arange(4)
a+np.array(1,2)


# In[90]:


#reductions 

x=np.array([1,2,3,4])
np.sum(a)


# In[91]:


x=np.array([[1,1],[2,2]])
x


# In[92]:


x.sum(axis=0)#column wise sum


# In[93]:


x.sum(axis=1) #row wise sum


# In[95]:


x=np.array([1,3,2])
x.min() #max also


# In[96]:


print(x.argmin()) # gives index of min element
print(x.argmax())


# In[97]:


np.all([True,True])


# In[98]:


np.any([True,False])


# In[99]:


#any can be used for array comparsions
a=np.zeros((50,50))
np.any(a!=0)


# In[100]:


np.all(a==a)


# In[101]:


#very important
#so easy
a=np.array([1,2,3,2])
b=np.array([2,2,3,2])
c=np.array([6,4,4,5])

((a<=b)& (b<=c)).all()


# In[103]:


x=np.array([1,2,3,1])
print(x.mean())
print(np.median(x))
print(np.std(x))

#can also do for matrices alog axises suing axis values


# In[104]:


data=np.loadtxt('populations.txt')
data


# In[105]:


year,hares,lynxes,carrots=data.T #colums to variables
print(year)


# In[106]:


populations=data[:,1:] #all rows but colum from 1 onwards
populations  


# In[107]:


populations.std(axis=0) #column wise


# In[108]:


#whcih species has max population each year 
np.argmax(populations,axis=1) 


# In[112]:


#broadcasting
#very important

#to add or subtract two arrays we generally do element wise 
#operation that is element wise operation

#but for numpy array we can do for non similar sizes
a=np.tile(np.arange(0,40,10),(3,1))
#here arange creates a 1d array 
#tile replicates this into 3 times into rows and 1 times to column
print(a)

print('\n\n')
a=a.T
print(a) #transpose of a


# In[113]:


b=np.array([0,1,2])
b


# In[114]:


a+b


# In[142]:


a=np.arange(0,40,10)
b=np.array([0,1,2])
#this also doesnt work


# In[143]:


b=b[:,np.newaxis]
b.shape #convert any one to matrix either a or b


# In[144]:


a+b


# In[146]:


#array shape manipulation
a=np.array([[1,2,3],[4,5,6]]) #2d array
#flattens or converts array into 1d
a.ravel() #a doesnt change


# In[148]:


a.T #a doesnt change


# In[149]:


a.T.ravel()


# In[151]:


b=a.ravel()
b


# In[152]:


b=b.reshape((2,3))
b


# In[159]:


b[0,0]=100
a
#a also changes
# ravel always works on memory so change ill be reflected in both
#reshape can sometimes return copy depending on case
#example

a=np.zeros((3,2))
b=a.T.reshape((3,2))
b[0]=50
a
#if directly use a and not a.T change will be reflected


# In[160]:


#adding a dimension

z=np.array([1,2,3])
z[:,np.newaxis]

#reshaping
a=np.arange(4*3*2).reshape(4,3,2)
a
#think of 3d arrray as 4 arrays of size 3*2


# In[161]:


#resizing

a=np.arange(4)
a.resize((8,))
a
#concatenates with zero for remanining values


# In[162]:


#problem with resizing

b=a
a.resize((4,))
#because referenced cant be resized


# In[163]:


#sorting 

a=np.array([[5,4,6],[2,3,2]])
b=np.sort(a,axis=1)
b #rowwise


# In[164]:


#sorting original array a
#inplace sorting algo
a.sort(axis=0)
a


# In[166]:


#fancy indexing
a=np.array([4,3,1,2])
j=np.argsort(a)
#tells the index accd to old array in the sorted array
j


# In[167]:


a[j] #gives sorted array values

