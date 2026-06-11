
# Bookstore — OOP Lab

A Python OOP exercise that models two items carried by a bookstore: an online **Book** and a **Coffee**. Built with class properties, setters, and instance methods following a test-driven workflow.

---

## Project Structure

```
bookstore/
├── lib/
│   ├── __init__.py
│   ├── book.py          # Book class
│   ├── coffee.py        # Coffee class
│   └── testing/
│       ├── book_test.py
│       ├── coffee_test.py
│       └── conftest.py
├── debug.py             # Interactive debugging entry point
├── Pipfile
└── pytest.ini
```

---

## Setup

```console
$ pipenv install
$ pipenv shell
```

---

## The Classes

### Book (`lib/book.py`)

Represents an online book that a user can read.

**Attributes**

| Attribute    | Type  | Description                        |
|--------------|-------|------------------------------------|
| `title`      | `str` | Title of the book (required)       |
| `page_count` | `int` | Number of pages (required, validated) |

**Methods**

| Method        | Description                                          |
|---------------|------------------------------------------------------|
| `turn_page()` | Prints `Flipping the page...wow, you read fast!`     |

**Validation**

Setting `page_count` to a non-integer prints `page_count must be an integer` and leaves the value unchanged.

**Example**

```python
from lib.book import Book

book = Book("And Then There Were None", 272)
print(book.title)       # And Then There Were None
print(book.page_count)  # 272
book.turn_page()        # Flipping the page...wow, you read fast!

book.page_count = "lots"  # page_count must be an integer
```

---

### Coffee (`lib/coffee.py`)

Represents a coffee drink sold by the bookstore.

**Attributes**

| Attribute | Type    | Description                                      |
|-----------|---------|--------------------------------------------------|
| `size`    | `str`   | One of `Small`, `Medium`, or `Large` (validated) |
| `price`   | `float` | Price in dollars (increases by 1 when tipped)    |

**Methods**

| Method  | Description                                                                 |
|---------|-----------------------------------------------------------------------------|
| `tip()` | Prints `This coffee is great, here's a tip!` and increases `price` by `1` |

**Validation**

Setting `size` to anything other than `Small`, `Medium`, or `Large` prints `size must be Small, Medium, or Large` and leaves the value unchanged.

**Example**

```python
from lib.coffee import Coffee

latte = Coffee(size="Large", price=3.50)
print(latte.size)   # Large
print(latte.price)  # 3.5
latte.tip()         # This coffee is great, here's a tip!
print(latte.price)  # 4.5

latte.size = "Venti"  # size must be Small, Medium, or Large
```

---

## Running the Tests

Run all tests:

```console
$ pipenv run pytest lib/testing/
```

Run a single class:

```console
$ pipenv run pytest lib/testing/book_test.py
$ pipenv run pytest lib/testing/coffee_test.py
```

Stop on first failure (useful during development):

```console
$ pipenv run pytest -x lib/testing/
```

Expected output: **7 tests passing**.

---

## Interactive Debugging

`debug.py` loads both classes and drops into an `ipdb` session:

```console
$ pipenv run python debug.py
```

---

## Branch & Workflow

| Branch                       | Purpose                          |
|------------------------------|----------------------------------|
| `main`                       | Stable, passing code             |
| `feature/book-coffee-classes`| Implementation branch (merged)   |
