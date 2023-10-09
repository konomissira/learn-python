from collections import defaultdict

people = defaultdict(int)
people.update({"John" : 45, "Lea": 39, "Jane" : 28})

print(people["Lea"])
print(people["james"])