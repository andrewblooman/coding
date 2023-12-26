# utils.py

def generate_unique_id(prefix):
    """
    Generate a unique identifier with a given prefix.
    """
    import uuid
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def format_date(date):
    """
    Format a date object as a string in a specific format.
    """
    return date.strftime("%Y-%m-%d")
