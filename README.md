# Assignment, Arithmetic, Comparison, and Logical Operators in Python

This repository introduces four groups of Python operators with a runnable
program and step-by-step explanations. The code examples are in
[`operator_examples.py`](./operator_examples.py).

## Requirements

- Python 3
- No third-party packages

## Run the examples

Open a terminal in the repository directory and run:

```bash
python operator_examples.py
```

On some systems, the Python command is `python3`:

```bash
python3 operator_examples.py
```

The program prints each example and its result.

## 1. Assignment operators

Assignment stores a value in a variable. Python evaluates the expression on the
right and stores the result in the name on the left:

```python
product_price = 120
```

After this statement, `product_price` contains `120`. The `=` symbol means
"assign" here; it does not test whether two values are equal. Use `==` to
compare values for equality (see [Comparison operators](#3-comparison-operators)).

### Augmented assignment

An augmented assignment combines an operation and assignment. For example,
`score += 3` means `score = score + 3`.

| Operator | Example | Equivalent operation | Result if `score` starts at `10` |
|---|---|---|---:|
| `=` | `score = 10` | Assign the value directly | `10` |
| `+=` | `score += 3` | `score = score + 3` | `13` |
| `-=` | `score -= 3` | `score = score - 3` | `7` |
| `*=` | `score *= 3` | `score = score * 3` | `30` |
| `/=` | `score /= 4` | `score = score / 4` | `2.5` |
| `//=` | `score //= 4` | `score = score // 4` | `2` |
| `%=` | `score %= 4` | `score = score % 4` | `2` |
| `**=` | `score **= 2` | `score = score ** 2` | `100` |

The program resets `score` before each operation so that every example starts
with a predictable value.

## 2. Arithmetic operators

Arithmetic operators perform calculations. The program demonstrates them with
`17` and `5`:

| Operator | Name | Example | Result |
|---|---|---|---:|
| `+` | Addition | `17 + 5` | `22` |
| `-` | Subtraction | `17 - 5` | `12` |
| `*` | Multiplication | `17 * 5` | `85` |
| `/` | Division | `17 / 5` | `3.4` |
| `//` | Floor division | `17 // 5` | `3` |
| `%` | Modulo (remainder) | `17 % 5` | `2` |
| `**` | Exponentiation | `4 ** 3` | `64` |

`/` returns the quotient, including its fractional part. `//` rounds the
quotient down to the nearest whole number; for these positive numbers,
`17 // 5` is `3`. `%` returns the remainder: dividing `17` by `5` leaves `2`.
`**` raises the left value to the power on its right.

## 3. Comparison operators

Comparison operators compare two values and return a Boolean value: `True` or
`False`. The program compares a customer age of `20` with a minimum age of
`18`:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `20 == 18` | `False` |
| `!=` | Not equal to | `20 != 18` | `True` |
| `>` | Greater than | `20 > 18` | `True` |
| `<` | Less than | `20 < 18` | `False` |
| `>=` | Greater than or equal to | `20 >= 18` | `True` |
| `<=` | Less than or equal to | `20 <= 18` | `False` |

Do not confuse `=` (assign a value) with `==` (compare two values).

## 4. Logical operators

Logical operators combine or reverse conditions. They are often used with
comparison expressions and Boolean values:

| Operator | Meaning | Result for Boolean operands |
|---|---|---|
| `and` | AND | `True` only when both operands are `True` |
| `or` | OR | `True` when at least one operand is `True` |
| `not` | NOT | Reverses the value: `not True` is `False` |

The program uses these conditions:

```python
has_ticket = True
is_adult = True
is_on_guest_list = False
```

- `has_ticket and is_adult` is `True` because both conditions are true.
- `is_on_guest_list or has_ticket` is `True` because at least one condition is
  true.
- `not is_on_guest_list` is `True` because `not` reverses `False`.

### Truth table

| `A` | `B` | `A and B` | `A or B` |
|---|---|---|---|
| `False` | `False` | `False` | `False` |
| `False` | `True` | `False` | `True` |
| `True` | `False` | `False` | `True` |
| `True` | `True` | `True` | `True` |

## Expected output

Running `python operator_examples.py` prints:

```text
=== Assignment operators ===
product_price = 120 -> 120
score += 3 -> 13
score -= 3 -> 7
score *= 3 -> 30
score /= 4 -> 2.5
score //= 4 -> 2
score %= 4 -> 2
score **= 2 -> 9

=== Arithmetic operators ===
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
4 ** 3 = 64

=== Comparison operators ===
20 == 18 -> False
20 != 18 -> True
20 > 18  -> True
20 < 18  -> False
20 >= 18 -> True
20 <= 18 -> False

=== Logical operators ===
Has a ticket AND is an adult: True
Is on the guest list OR has a ticket: True
Is NOT on the guest list: True
```
