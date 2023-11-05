# Importing the required library for ISBN validation
import isbnlib

# Validating whether the given ISBN number is valid or not using an existing library
def ValidateISBN(isbn: str) -> bool:
    try:
        if isbnlib.notisbn(isbn, level='strict'):
            # ISBN is not valid according to the 'strict' level validation
            return False
        else:
            # ISBN is valid
            return True
    except Exception as e:
        # Exception occurred during validation
        return False
