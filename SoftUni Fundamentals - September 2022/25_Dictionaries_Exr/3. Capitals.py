countries = input().split(", ")
capitals = input().split(", ")
countries_with_theire_capitals = {country:capital for country, capital in zip(countries, capitals)}
for place, city in countries_with_theire_capitals.items():
    print(f"{place} -> {city}")