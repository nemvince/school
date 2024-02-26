import folium
import json

with open("maps.json") as f:
    maps = json.load(f)

folmap = folium.Map(location=maps["base_location"], zoom_start=maps["zoom_start"])

selected_locations = []

print("Select locations to add to the map:")
for i, location in enumerate(maps["locations"]):
    print(f"{i + 1}. {location['name']}")
print(
    "Input numbers or ranges in the format of 'start-end,number,start-end' (e.g. 1-3,5), alternatively input * for all locations."
)
ranges = input(">")
if ranges == "*":
    ranges = [str(i) for i in range(1, len(maps["locations"]) + 1)]
else:
    ranges = ranges.split(",")

# check for overlapping ranges and out of bounds numbers
selected_numbers = []
for r in ranges:
    if "-" in r:
        start, end = r.split("-")
        try:
            for i in range(int(start), int(end) + 1):
                if i in selected_numbers:
                    raise ValueError(f"Overlapping range: {r}")
                if i < 1 or i > len(maps["locations"]):
                    raise ValueError(f"Out of bounds number: {i}")
                selected_numbers.append(i)
        except ValueError:
            raise ValueError(f"Invalid range: {r}")
    else:
        i = int(r)
        if i in selected_numbers:
            raise ValueError(f"Duplicate number: {i}")
        if i < 1 or i > len(maps["locations"]):
            raise ValueError(f"Out of bounds number: {i}")
        selected_numbers.append(i)

for r in ranges:
    if "-" in r:
        start, end = r.split("-")
        try:
            for i in range(int(start), int(end) + 1):
                selected_locations.append(maps["locations"][i - 1])
        except ValueError:
            raise ValueError(f"Invalid range: {r}\nAre your ranges overlapping?")
    else:
        selected_locations.append(maps["locations"][int(r) - 1])

print("Selected locations:")
for i, location in enumerate(selected_locations):
    print(f"{i + 1}. {location['name']}")
for location in selected_locations:
    expecting = ["name", "link", "image", "latitude", "longitude"]
    if not list(location.keys()) == expecting:
        raise ValueError(
            f"Invalid location format in maps.json\nYou are missing keys: {[x for x in expecting if x not in location]}\nLocation: {location}"
        )

    coord = [location["latitude"], location["longitude"]]

    icon = folium.CustomIcon(location["image"], icon_size=(50, 50))

    folium.Marker(
        coord,
        icon=icon,
    ).add_to(folmap)

    folium.Marker(
        coord,
        icon=folium.DivIcon(
            html=f'<span style="padding: 2px; background-color: black; font-size: 15px; font-family: monospace"><a href={location["link"]}>{location["name"]}</a></span>'
        ),
    ).add_to(folmap)


folmap.save("map.html")
print(f"Map saved to map.html")
