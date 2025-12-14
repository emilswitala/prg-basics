countries = [
{"name":"Poland", "population":38000000},
{"name": "Ukraine", "population": 39000000},
{"name": "Slovakia", "population": 5400000},
{"name": "Germany", "population": 83600000},
{"name": "Czech Republic", "population": 10900000}
]

print("COUNTRY".ljust(15), "POPULATION")
for country in countries:
    print(country["name"].ljust(15), country["population"])