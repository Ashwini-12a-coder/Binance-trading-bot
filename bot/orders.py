import logging

class OrderService:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):

        request = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == "LIMIT":
            request["price"] = price
            request["timeInForce"] = "GTC"

        logging.info(f"ORDER REQUEST: {request}")

        try:
            response = self.client.place_order(**request)

            logging.info(f"ORDER RESPONSE: {response}")

            return request, response

        except Exception as e:
            logging.error(f"ORDER ERROR: {str(e)}")
            raise