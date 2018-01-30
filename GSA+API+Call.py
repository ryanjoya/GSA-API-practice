
# coding: utf-8

# In[5]:


import json
import requests

url = "https://inventory.data.gov/api/action/datastore_search?resource_id=8ea44bc4-22ba-4386-b84c-1494ab28964b"
parameters = {}

parameters["City"] = "Pearland"
parameters["State"] = "TX"
parameters["Zip"] = "77584"
parameters["Fiscal Year"] = 2017
parameters = json.dumps(parameters)

response = requests.post(url,data=parameters)

print(response)

print(parameters)


# In[27]:


poop = json.loads(response.content)["result"]["records"][0]["Dec"]


# In[28]:


print(poop)


# In[15]:


print(poop)


# In[21]:


import pandas as pd


# In[25]:


test = pd.read_excel("test.xlsx")


# In[26]:


test.head()


# In[29]:


def get_meal_value(row):
    url = "https://inventory.data.gov/api/action/datastore_search?resource_id=8ea44bc4-22ba-4386-b84c-1494ab28964b"
    parameters = {}
    parameters["State"] = row["State"]
    parameters["Zip"] = row["Zip"]
    parameters["Fiscal Year"] = 2017
    parameters = json.dumps(parameters)
    
    try:
        response = requests.post(url,data=parameters)
        poop = json.loads(response.content)["result"]["records"][0]["Dec"]
        return poop
    except:
        return 0

test["Meal"] = test.apply(get_meal_value, axis=1)


# In[30]:


test.head()


# In[31]:


test.to_csv("test2.csv", index=False)

