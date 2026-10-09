def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Yeh function total price par discount calculate karke final price return karta hai.
    """
    discount_amount: float = (price * discount_percent) / 100.0
    final_price: float = price - discount_amount
    return round(final_price, 2)


if __name__ == "__main__":
    original: float = 1000.0
    discount: float = 15.0
    print(f"Final Price: ₹{calculate_discount(original, discount)}")
