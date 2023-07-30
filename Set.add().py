n = int(input())
unique_countries = set()
for i in range(n):
    country = input()
    unique_countries.add(country)
print(len(unique_countries))