"""controllers/privacy.py."""

from flask import Blueprint, render_template
from werkzeug import Response

privacy_controller = Blueprint("privacy_controller", __name__)

@privacy_controller.route("/privacy", methods=["GET"])
def privacy() -> Response | str:
    """
    Renders the privacy page.
    """
    return render_template("privacy.html")
