
# Note in order for this to work you need to generate a access key from ipstack.com
# coding: utf-8

# In[1]:


# Importing Required Modules
import requests
from geopy.distance import geodesic


# In[2]:
my_ip="157.36.181.223"
friend_ip="157.36.181.223"


# In[3]:

url='http://api.ipstack.com/'+my_ip+'?access_key=6fda225495b676758c991b1ac353a081'
response = requests.get(url)
response=response.json()
print("MY IP INFO: ",response)
my_long_lat= (response['latitude'],response['longitude'])


url='http://api.ipstack.com/'+friend_ip+'?access_key=6fda225495b676758c991b1ac353a081'
response = requests.get(url)
response=response.json()
print("FRIEND IP INFO:",response)
friend_long_lat= (response['latitude'],response['longitude'])


# In[4]:
distance = geodesic(my_long_lat, friend_long_lat).miles
print("DISTANCE BETWEEN MY IP AND FRIEND IP",distance)








