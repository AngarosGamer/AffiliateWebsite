"""controllers/login.py."""

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug import Response

from models.User_DAO import UserDAO

login_controller = Blueprint("login_controller", __name__)


@login_controller.route("/login", methods=["GET"])
def login_get() -> Response | str:
    """
    Renders the login page when called with HTTP 'GET' method.

    If the user is already logged in, redirects to dashboard.

    :return: Returns the login template, or redirect to dashboard.
    """
    return render_template("login.html", noexist=False)  # Show login page


@login_controller.route("/login", methods=["POST"])
def login_post() -> Response | str:
    """
    Verifies user login credentials and handles redirect if necessary.

    :return: Successful login returns dashboard template, else return to login.
    """
    # login logic here
    email = request.form.get("email").lower()
    password = request.form.get("password")
    next_url = request.form.get("next")

    user = UserDAO.get_user_by_email(email)
    if not user:
        return render_template("login.html", current_user=current_user, noexist=True)

    if user.check_password(password):
        login_user(user, remember=True)
        if next_url:  # Redirect to passed URL instead of Dashboard
            return redirect(next_url)
        return redirect(
            url_for("dashboard_controller.dashboard_get"),
        )  # default to dashboard if no next page given

    return render_template("login.html", current_user=current_user, noexist=True)
