"""
CP1401 - Practical
Shop Calculator

function main
    get number_of_items
    while number_of_items < 0
        display "Invalid number of items!"
        get number_of_items
    set total_price to 0
    for each item in range from 1 to number_of_items
        get price_of_item
        add price_of_item to total_price
    if total_price > 100
        set total_price to total_price * 0.9   # apply 10% discount
    display "Total price for number_of_items items is $total_price"
"""


def main():
    """Calculate total price for items with discount if applicable."""
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0
    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        total_price += price_of_item

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


main()
