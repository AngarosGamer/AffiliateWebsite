"""Stores constant config settings for Flask Server."""

CSV_LINKS_PATH= "database/affiliate-links.csv"
CSV_CODES_PATH= "database/affiliate-codes.csv"
PASSWORD_MIN_LENGTH: int | None = 8
REGEX_PATTERNS: dict[str, str] = {
    "email_addresses": r"^[\w\.=-]+@[\w\.-]+\.[\w]{2,3}$",
}


