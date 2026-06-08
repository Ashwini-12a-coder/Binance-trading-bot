import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

# Load .env file
load_dotenv()

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Binance Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:
        # Input validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        # Load API credentials from .env
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError(
                "API_KEY or API_SECRET not found in .env file"
            )

        # Create client
        client = BinanceFuturesClient(
            api_key=api_key,
            api_secret=api_secret
        )

        service = OrderService(client)

        # Place order
        request, response = service.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        # Required Output
        print("\n===== ORDER REQUEST SUMMARY =====")
        print(request)

        print("\n===== ORDER RESPONSE DETAILS =====")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

        print("\n✅ SUCCESS: Order placed successfully")

    except Exception as e:
        logger.error(str(e))
        print(f"\n❌ FAILED: {e}")


if __name__ == "__main__":
    main()