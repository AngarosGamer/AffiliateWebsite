"""controllers/legal.py."""

from flask import Blueprint, render_template
from werkzeug import Response

legal_controller = Blueprint("legal_controller", __name__)

@legal_controller.route("/legal", methods=["GET"])
def legal() -> Response | str:
    """
    Renders the legal page.
    """
    return render_template("legal.html")
