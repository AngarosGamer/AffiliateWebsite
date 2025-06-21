"""The Affiliate Model file."""
from datetime import datetime
from time import strftime, gmtime

import bcrypt


class Affiliate:
    """Represents an Affiliate Object."""

    def __init__(
        self,
        id_affiliate: int | None = None,
        email: str = "",
        referral_code: str = "",
    ) -> None:
        """Build Affiliate class item."""
        self.id_affiliate = id_affiliate
        self.email = email
        self.referral_code = referral_code

    # Getter for id_affiliate
    def get_id_affiliate(self) -> int:
        """
        Getter for id_affiliate.

        :return: The Affiliate string ID.
        """
        return self.id_affiliate

    # Setter for id_affiliate
    def set_id_affiliate(self, value: int) -> None:
        """
        Setter for id_affiliate.

        :param value: The id_affiliate to set.
        :return: None.
        """
        self.id_affiliate = value

    # Getter for email
    def get_email(self) -> str:
        """
        Getter for email.

        :return: The Affiliate's email string.
        """
        return self.email

    # Setter for email
    def set_email(self, value: str) -> None:
        """
        Setter for email.

        :param value: The new email to set.
        """
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format.")
        self.email = value

    # Getter for referral_code
    def get_referral_code(self) -> str:
        """
        Getter for referral_code.

        :return: The Affiliate's referral_code.
        """
        return self.referral_code

    # Setter for referral_code
    def set_referral_code(self, referral_code: str) -> None:
        """
        Setter for referral_code.

        :param referral_code: The new referral_code to set.
        """
        self.referral_code = referral_code


    def to_dict(self) -> dict[str:str]:
        """Convert Affiliate object to dictionary representation."""
        return {
            "id_affiliate": self.get_id_affiliate(),
            "email": self.get_email(),
            "referral_code": self.get_referral_code(),
        }