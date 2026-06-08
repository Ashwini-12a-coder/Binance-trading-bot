def validate_symbol(symbol):
    if not symbol:
        raise ValueError(
            "Symbol is required (example: BTCUSDT)"
        )

    if not symbol.upper().endswith("USDT"):
        raise ValueError(
            "Invalid symbol. Must be USDT pair like BTCUSDT"
        )


def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError(
            "Side must be BUY or SELL"
        )


def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError(
            "Order type must be MARKET or LIMIT"
        )


def validate_quantity(qty):
    try:
        qty = float(qty)

        if qty <= 0:
            raise ValueError

    except:
        raise ValueError(
            "Quantity must be a positive number"
        )


def validate_price(order_type, price):
    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        try:
            price = float(price)

            if price <= 0:
                raise ValueError

        except:
            raise ValueError(
                "Price must be a positive number"
            )