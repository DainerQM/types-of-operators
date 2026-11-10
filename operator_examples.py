"""Runnable examples of assignment, arithmetic, comparison, and logical operators."""


def main():
    print("=== Assignment operators ===")

    # The = operator assigns the value on the right to the variable on the left.
    product_price = 120
    print("product_price = 120 ->", product_price)

    # Augmented assignment operators update a variable using its current value.
    score = 10
    score += 3
    print("score += 3 ->", score)

    score = 10
    score -= 3
    print("score -= 3 ->", score)

    score = 10
    score *= 3
    print("score *= 3 ->", score)

    score = 10
    score /= 4
    print("score /= 4 ->", score)

    score = 10
    score //= 4
    print("score //= 4 ->", score)

    score = 10
    score %= 4
    print("score %= 4 ->", score)

    score = 3
    score **= 2
    print("score **= 2 ->", score)

    print("\n=== Arithmetic operators ===")

    first_number = 17
    second_number = 5
    print("17 + 5 =", first_number + second_number)
    print("17 - 5 =", first_number - second_number)
    print("17 * 5 =", first_number * second_number)
    print("17 / 5 =", first_number / second_number)
    print("17 // 5 =", first_number // second_number)
    print("17 % 5 =", first_number % second_number)
    print("4 ** 3 =", 4**3)

    print("\n=== Comparison operators ===")

    customer_age = 20
    minimum_age = 18
    print("20 == 18 ->", customer_age == minimum_age)
    print("20 != 18 ->", customer_age != minimum_age)
    print("20 > 18  ->", customer_age > minimum_age)
    print("20 < 18  ->", customer_age < minimum_age)
    print("20 >= 18 ->", customer_age >= minimum_age)
    print("20 <= 18 ->", customer_age <= minimum_age)

    print("\n=== Logical operators ===")

    has_ticket = True
    is_adult = True
    is_on_guest_list = False
    print("Has a ticket AND is an adult:", has_ticket and is_adult)
    print("Is on the guest list OR has a ticket:", is_on_guest_list or has_ticket)
    print("Is NOT on the guest list:", not is_on_guest_list)


if __name__ == "__main__":
    main()
