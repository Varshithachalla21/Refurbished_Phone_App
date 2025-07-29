condition_mapping = {
    "Like New": {
        "X": "New",
        "Y": "3 Stars (Excellent)",
        "Z": "New"
    },
    "Good": {
        "X": "Good",
        "Y": "2 Stars (Good)",
        "Z": "As New"
    },
    "Fair": {
        "X": "Scrap",
        "Y": "1 Star (Usable)",
        "Z": "Good"
    }
}    

def calculate_price(platform, base_price):
    if platform == "X":
        price = base_price / (1 - 0.10)
    elif platform == "Y":
        price = (base_price + 2) / (1 - 0.08)
    elif platform == "Z":
        price = base_price / (1 - 0.12)
    else:
        price = base_price
    return round(price, 2)


def is_profitable(platform, base_price, final_price):
    if platform == "X":
        return final_price * 0.9 >= base_price
    elif platform == "Y":
        return (final_price * 0.92 - 2) >= base_price
    elif platform == "Z":
        return final_price * 0.88 >= base_price
    return False
