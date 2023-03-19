def orderPizza(size, style='regular', topping=None):
    PRICE_OF_TOPPING = 1.50

    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.00
    else:
        price = 18.00

    if style == 'deepdish':
        price = price + 2.00

    line = 'You have ordered a ' + size + ' ' + style + ' pizza with '
    if topping is None:
        print(line + 'no topping')
    else:
        print(line + topping)
        price = price + PRICE_OF_TOPPING

    print('The price is $', price)
    print()

orderPizza('large')
orderPizza('large', style='regular')
orderPizza('medium', style='deepdish', topping='mushrooms')
orderPizza('small', topping='mushroom')
