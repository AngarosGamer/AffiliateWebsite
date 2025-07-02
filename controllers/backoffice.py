"""controllers/backoffice.py."""
import os

from flask import Blueprint, Response, abort, render_template, request, flash, redirect
from flask_login import current_user, login_required

import constants
from models.User import User
from models.User_DAO import UserDAO

backoffice_controller = Blueprint("backoffice_controller", __name__)

@backoffice_controller.route("/backoffice", methods=["GET"])
@login_required
def backoffice_get() -> Response | str:
    """
    Get the user backoffice if logged in.

    :return: Returns the backoffice template, or redirect to login.
    """
    user: User = UserDAO.get_user_by_id(current_user.id_user)
    if not user.email.lower() == os.getenv('ADMIN_EMAIL').lower():
        return abort(404) # The user is not an admin, drop the request

    users: list[User] = UserDAO.get_all_users()
    users = [user.to_dict() for user in users]
    return render_template(
        "backoffice.html",
        current_user=current_user,
        users=users,
    )

@backoffice_controller.route(
    "/backoffice/search", methods=["GET"]
)
@login_required
def backoffice_users_search() -> str:
    """Search users dynamically based on query parameters."""
    query = request.args.get("query", "").strip()

    if query.isdigit():  # Search by ID if query is a number
        users = [UserDAO.get_user_by_id(int(query))]
    elif query:  # Search by email / ref code
        users = UserDAO.search_users(query)
    else:  # No query, return all users
        users = UserDAO.get_all_users()

    if len(users) <= 0 or users[0] is None:
        users = []
    else:
        users = [user.to_dict() for user in users]


    return render_template(
        "_backoffice_users.html",
        users=users,
        current_user=current_user,
    )


@backoffice_controller.route(
    "/backoffice/update", methods=["POST"]
)
@login_required
def backoffice_users_update() -> Response | str:
    """
    Update a user from request params if allowed.

    :return: Returns the user management template, or redirect to login.
    """
    user: User = UserDAO.get_user_by_id(int(current_user.id_user))
    if not user.email.lower() == os.getenv('ADMIN_EMAIL').lower():
        return abort(404) # The user is not an admin, drop the request

    user_id = request.form.get("user_id")  # Get user ID
    user_email = request.form.get("user_email")  # Get their email
    user_affiliate_status = bool(request.form.get("user_affiliate_status"))
    user_referral_code = request.form.get("user_referral_code")

    if not user_id.isdigit():
        flash("Error updating user")
        return redirect("/backoffice")

    # Cannot edit Self.
    if int(user_id) == int(current_user.id_user):
        flash("Cannot update self")
        return redirect("/backoffice")

    user_db = UserDAO.get_user_by_id(int(user_id))

    user = User(
        id_user=int(user_id),
        email=user_email,
        password=user_db.password,
        affiliate_status=user_affiliate_status,
        referral_code=user_referral_code
    )

    UserDAO.update_user(user)

    return redirect("/backoffice")

@backoffice_controller.route(
    "/backoffice/delete", methods=["POST"]
)
@login_required
def backoffice_users_delete() -> Response | str:
    """
    Delete a user using request params if user has permission.

    :return: Returns the user management template, or redirect to login.
    """

    user: User = UserDAO.get_user_by_id(current_user.id_user)
    if not user.email.lower() == os.getenv('ADMIN_EMAIL').lower():
        return abort(404)  # The user is not an admin, drop the request

    user_id = request.form.get("user_id")  # Get user ID

    if not user_id.isdigit():
        flash("Error updating user")
        return redirect("/backoffice")

    # Cannot delete Self.
    if int(user_id) == int(current_user.id_user):
        flash("Cannot delete self")
        return redirect("/backoffice")

    UserDAO.delete_user(int(user_id))

    return redirect("/backoffice")