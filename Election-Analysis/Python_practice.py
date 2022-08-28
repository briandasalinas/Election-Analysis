voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

for i in range(len(counties)):
    print(counties[i])

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for key, value in counties_dict.items():
    print(key,"county has", value, "registerd voters.")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

