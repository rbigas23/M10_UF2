import json

data = {
    "books": [
        {
            "title": "The Catcher in the Rye",
            "cover": "Paperback",
            "year": 1951,
            "pages": 277,
        },
        {
            "title": "To Kill a Mockingbird",
            "cover": "Hardcover",
            "year": 1960,
            "pages": 281,
        },
        {"title": "1984", "cover": "Paperback", "year": 1949, "pages": 328},
        {"title": "The Great Gatsby", "cover": "Hardcover", "year": 1925, "pages": 180},
        {
            "title": "The Lord of the Rings",
            "cover": "Box Set",
            "year": 1954,
            "pages": 1178,
        },
    ]
}
json_str = json.dumps(data)
print(json_str)
with open("ex_23.json", "wt") as f:
    f.write(json_str)
