person = {
    "name": "Rafiul",
    "age": 25,
    "city": "Dhaka"
}

print(person)
print(person["city"])

person.pop("age")
print(person)

person["country"] = "Bangladesh"
print(person)

print(person.get("gender", "Not specified"))
