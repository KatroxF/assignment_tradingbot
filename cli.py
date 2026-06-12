import argparse
from bot.orders import place_market_order

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_limit_price
)

from bot.logging_config import logger


parser = argparse.ArgumentParser()

parser.add_argument(
    "--symbol",
    required=True
)

parser.add_argument(
    "--side",
    required=True
)

parser.add_argument(
    "--type",
    required=True
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()


try:

    validate_side(args.side)

    validate_order_type(
        args.type
    )

    validate_quantity(
        args.quantity
    )

    validate_limit_price(
        args.type,
        args.price
    )

    logger.info(
        f"Request: {args}"
    )

    if args.type == "MARKET":

        response = (
            place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )
        )

    else:

        response = (
            place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )
        )

    logger.info(
        f"Response: {response}"
    )

    print("\n===== SUCCESS =====")

    print(
        f"Order ID: "
        f"{response.get('orderId')}"
    )

    print(
        f"Status: "
        f"{response.get('status')}"
    )

    print(
        f"Executed Qty: "
        f"{response.get('executedQty')}"
    )

except Exception as e:

    logger.error(str(e))

    print(
        f"\nERROR: {e}"
    )