cities: list = ["Krishnagar", "Kolkata", "Shyamnagar", "Kalyani", "Sahantipur"]

city: str = ""
print(any(city.startswith("H") for city in cities))

# witnesses: list = [city for city in cities if city.startswith("S")]
#
# if witnesses:
#     print(f'{witnesses[0]} starts with S')
# else:
#     print("No city starts with S")

# with the help of walrus operator
if any((witness := city).startswith("S") for city in cities):
    print(f"{witness} starts with S")
else:
    print("No city name starts with S")
