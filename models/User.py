"""The User Model file."""

import bcrypt
from flask_login import UserMixin


class User(UserMixin):
    """Represents a User Object."""

    def __init__(
        self,
        id_user: int | None = None,
        email: str = "",
        password: str = "",
        affiliate_status: bool = False,
        referral_code: str = "",
    ) -> None:
        """Build User class item."""
        self.id_user = id_user
        self.email = email
        self.password = password
        self.affiliate_status = affiliate_status
        self.referral_code = referral_code

    # Getter for id_user
    def get_id_user(self) -> int:
        """
        Getter for id_user.

        :return: The User string ID.
        """
        return self.id_user

    # Setter for id_user
    def set_id_user(self, value: int) -> None:
        """
        Setter for id_user.

        :param value: The id_user to set.
        :return: None.
        """
        self.id_user = value

    # Getter for email
    def get_email(self) -> str:
        """
        Getter for email.

        :return: The User's email string.
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

    # Getter for password
    def get_password(self) -> str:
        """
        Getter for password.

        :return: The User hashed password.
        """
        return self.password

    # Setter for password
    def set_password(self, passwd: str) -> None:
        """
        Setter for password.

        :param passwd: The new password to set.
        """
        if isinstance(passwd, str):
            passwd = bytes(passwd, "utf-8")
        self.password = str(bcrypt.hashpw(passwd, bcrypt.gensalt()), "utf8")


    # Getter for affiliate_status
    def get_affiliate_status(self) -> bool:
        """
        Getter for affiliate status.

        :return: Is the user an affiliate?
        """
        return self.affiliate_status


    # Setter for affiliate_status
    def set_affiliate_status(self, affiliate_status: bool) -> None:
        """
        Setter for affiliate status.

        :param affiliate_status: The new affiliate status to set.
        """
        self.affiliate_status = affiliate_status


    # Getter for referral_code
    def get_referral_code(self) -> str | None:
        """
        Getter for referral_code.

        :return: The User's affiliate code.
        """
        return self.referral_code


    # Setter for referral_code
    def set_referral_code(self, referral_code: str) -> None:
        """
        Setter for referral_code.

        :param referral_code: The new referral_code to set.
        """
        self.referral_code = str(referral_code)

    # Additional methods
    def check_password(self, passwd_to_check: str) -> bool:
        """
        Boolean function, check if password_to_check matches with user password.

        :param passwd_to_check: The password to check
        :return: Boolean. True if passwords match.
        """
        if isinstance(passwd_to_check, str):
            passwd_to_check = bytes(passwd_to_check, "utf-8")
        passwd = bytes(self.password, "utf8")
        return bcrypt.checkpw(passwd_to_check, passwd)

    def to_dict(self) -> dict[str:str]:
        """Convert User object to dictionary representation."""
        return {
            "id_user": self.get_id_user(),
            "email": self.get_email(),
            "affiliate_status": self.get_affiliate_status(),
            "referral_code": self.get_referral_code(),
        }

    def get_id(self) -> int:
        """
        Necessary flask_login function.

        Gets the user id each time there is a login_required page request.
        :return: The user ID.
        """
        return self.id_user
