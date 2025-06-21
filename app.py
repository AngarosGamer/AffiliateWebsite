"""Main Flask app file."""

import os

from dotenv import load_dotenv
from flask import (
    Flask,
    Response,
    redirect,
    render_template,
)
from flask_login import LoginManager

from controllers.dashboard import dashboard_controller  # Import dashboard_controller
from controllers.legal import legal_controller  # Import legal controller
from controllers.login import login_controller  # Import login_controller
from controllers.privacy import privacy_controller  # Import privacy controller
from controllers.signup import signup_controller  # Import signup_controller
from models.User import User
from models.User_DAO import UserDAO


def create_app() -> Flask:
    """
    Factory function to create and configure the Flask application.

    This function is used to initialize the app with necessary configurations.
    """
    # Créer l'application Flask
    load_dotenv()  # take environment variables from .env.
    app = Flask(
        __name__, template_folder="views/templates/", static_folder="views/static"
    )

    with app.app_context():
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Enregistrer les blueprints
    app.register_blueprint(login_controller)
    app.register_blueprint(signup_controller)
    app.register_blueprint(dashboard_controller)
    app.register_blueprint(legal_controller)
    app.register_blueprint(privacy_controller)


    login_manager = LoginManager()
    login_manager.login_view = "login_controller.login_get"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: int) -> User | None:
        """
        Flask-login default function for checking who is logging in.

        Must be called by login_manager at session open.
        :param user_id: The user ID.
        """
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return user
        return None

    @app.errorhandler(403)
    def forbidden_access(_e: Exception) -> tuple[str, int]:
        """Handle 403 errors gracefully."""
        return render_template("403.html"), 403

    # Handle 404 (Not Found) and 405 (Method Not Allowed)
    @app.errorhandler(404)
    @app.errorhandler(405)
    def page_not_found(_e: Exception) -> tuple[str, int]:
        """Handle 404 / 405 errors gracefully."""
        return render_template("404.html"), 404

    # Handle 500 (Internal)
    @app.errorhandler(500)
    def server_error(_e: Exception) -> tuple[str, int]:
        """Handle 500 errors gracefully."""
        return render_template("500.html"), 500

    @app.route("/")
    def index() -> Response:
        """The dashboard is our index page."""
        return redirect("/dashboard")

    return app


# If executed directly, use debug - CAUTION for production.
if __name__ == "__main__":
    app = create_app()
    from waitress import serve
    # context = (
    #    "C:\\Users\\angaros\\server.crt",
    #    "C:\\Users\\angaros\\server.key",
    # )  # certificate and key files
    serve(app, host="0.0.0.0", port=8085)  # noqa: S104
