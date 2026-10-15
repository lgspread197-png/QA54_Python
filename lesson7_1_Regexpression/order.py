import re


def is_valid_id(order_id):
    return bool(re.search("^ORD-...$",order_id))
print(is_valid_id("ORD-123"))
print(is_valid_id("ORD-12"))
print(is_valid_id("OOO-123"))
