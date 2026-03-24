set1 = {1,2,3,4}
set2 = {1,3,5}
print(set1 & set2)
print(set1 - set2)

customers = [
    {"name": "John", "city": "Kathmandu"},
    {"name": "Ram", "city": "Pokhara"},
    {"name": "Hari", "city": "Kathmandu"},
    {"name": "Sita", "city": "Lalitpur"}
]
city = {customer["city"] for customer in customers}
print(city)