"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
Estimate: 10 minutes
Actual:   20 minutes
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "beaver": "#9f8170",
    "blue1": "#0000ff",
    "chocolate": "#d2691e",
    "denim": "#1560bd",
    "dimgray": "#696969",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff"
}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").lower()