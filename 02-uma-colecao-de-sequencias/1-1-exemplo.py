metro_areas = [
    ('tokio', 'JP', 36.933, (35.68727, 139.691667)),
    ('Delhi NCR', 'IN', 36.933, (35.68727, 139.691667)),
    ('Mexico City', 'MX', 36.933, (35.68727, 139.691667)),
    ('New York-Newark', 'US', 36.933, (35.68727, 139.691667)),
    ('São Paulo', 'BR', 36.933, (35.68727, 139.691667))
]

print(f"{'':15} | {'lat.':^9} | {'long.':^9}")
fmt = "{:15} | {:9.4f} | {:9.4f}"

for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
