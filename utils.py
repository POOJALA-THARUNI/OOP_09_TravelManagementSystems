# utils.py
"""
Helper functions (ID generation, validation).
"""

import random

def generate_id(prefix):
    """
    Generate ID like: CUST123, BOOK456
    💡 Hint:
    - Use prefix + random number
    """
    return f"{prefix}{random.randint(100,999)}"
