import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Sepal_length_cm':2, 'Sepal_width_cm':9, 'Petal_length_cm':6, 'Petal_width_cm':10})

print(r.json())