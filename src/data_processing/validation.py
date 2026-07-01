"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""
    clean_isbn = str(isbn).replace("-","").strip()

    if not clean_isbn.isdigit():
        return False

    isbn_sum = 0
    for digit in range(len(clean_isbn) - 1):
        if digit % 2:
            isbn_sum += int(clean_isbn[digit])
        else:
            isbn_sum += int(clean_isbn[digit]) * 3

    if len(clean_isbn) != 13 or int((10 - (isbn_sum % 10)) % 10) != int(clean_isbn[12]):
        return False
    return True
