def process_price(price, currencies):
    for currency in currencies:
        if currency in price:
            price = price.replace(currency, '')
            break
    price = price.replace(',', '.')
    price = float(price)
    return price