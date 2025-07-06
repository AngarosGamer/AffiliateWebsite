"""controllers/signup.py."""

import re

from flask import Blueprint, redirect, render_template, request
from flask_login import login_user
from werkzeug import Response

import constants
from models.User import User
from models.User_DAO import UserDAO

signup_controller = Blueprint("signup_controller", __name__)


@signup_controller.route("/signup", methods=["GET"])
def signup_get() -> Response | str:
    """
    Renders the signup page when called with HTTP 'GET' method.

    If the user is already logged in, redirects to dashboard.

    :return: Returns the signup template, or redirect to signup.
    """
    print("Signup GET request received")
    return render_template("signup.html", noexist=False)  # Show signup page


def check_email(email: str) -> bool:
    """Ensure that the email is valid."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@.+\.com$"
    if re.match(email_regex, email):  # noqa: SIM103
        return True
    return False


def check_password(password: str) -> bool:
    """Checks if password meets security criteria."""
    password_regex_complexity = r".*['^£$%&*()}{@#~?><,.|=_+!-].*"  # noqa: S105
    password_regex_uppercase = r".*[A-Z].*"  # noqa: S105
    password_regex_lowercase = r".*[a-z].*"  # noqa: S105
    password_regex_numbers = r".*[0-9].*"  # noqa: S105

    if (  # noqa: SIM103
        len(password) >= constants.PASSWORD_MIN_LENGTH
        and re.match(password_regex_complexity, password)
        and re.match(password_regex_uppercase, password)
        and re.match(password_regex_lowercase, password)
        and re.match(password_regex_numbers, password)
    ):
        return True
    return False


@signup_controller.route("/signup", methods=["POST"])
def signup_post() -> Response | str:
    """
    Verifies user signup credentials and handles account creation.

    :return: Successful signup, return dashboard template, else return to signup.
    """
    email = request.form.get("email").lower()  # Get email
    password = request.form.get("password")  # Get password
    confirm_password = request.form.get(  # noqa: F841
        "confirm-password"
    )  # Get password

    # Check if the user already exists.
    user = UserDAO.get_user_by_email(email)
    if user:
        return render_template(
            "signup.html", noexist=True
        )  # Show signup

    if not check_email(email):
        print("Email check failed")
        return redirect("/signup")

    if not check_password(password):
        print("Password check failed")
        return redirect("/signup")

    user_str = User(email=email)
    user_str.set_password(password)
    user = UserDAO.create_user(user_str)
    login_user(user, remember=True)
    return redirect("/dashboard")
