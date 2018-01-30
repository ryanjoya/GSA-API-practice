

```python
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
```

    <Response [200]>
    {"City": "Pearland", "State": "TX", "Zip": "77584", "Fiscal Year": 2017}
    


```python
poop = json.loads(response.content)["result"]["records"][0]["Dec"]
```


```python
print(poop)
```

    134
    


```python
print(poop)
```

    {'City': 'Riverhead / Ronkonkoma / Melville', 'Dec': '134', 'Feb': '134', 'Zip': '501', 'Aug': '134', 'Sep': '134', 'Apr': '134', 'Jun': '134', 'State': 'NY', 'Jul': '134', 'Meals': '64', 'County': 'Suffolk County, NY', 'May': '134', 'DestinationID': '271', 'Mar': '134', 'Jan': '134', 'LocationDefined': 'Suffolk', 'Nov': '134', '_id': 1, 'Oct': '134', 'FiscalYear': '2018'}
    


```python
import pandas as pd
```


```python
test = pd.read_excel("test.xlsx")
```


```python
test.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Zip</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TX</td>
      <td>77584</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NJ</td>
      <td>7470</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
test.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>State</th>
      <th>Zip</th>
      <th>Meal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TX</td>
      <td>77584</td>
      <td>134</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NJ</td>
      <td>7470</td>
      <td>134</td>
    </tr>
  </tbody>
</table>
</div>




```python
test.to_csv("test2.csv", index=False)
```
