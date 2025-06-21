"""controllers/dashboard.py."""
import csv
import os
from pathlib import Path

import requests
from flask import Blueprint, Response, abort, render_template
from flask_login import current_user, login_required

import constants
from models.Affiliate import Affiliate
from models.AffiliateDAO import AffiliateDAO
from models.User_DAO import UserDAO

dashboard_controller = Blueprint("dashboard_controller", __name__)

def get_bitly_links_stat(affiliate: Affiliate) -> int | None:
    """Get bitly links stat."""
    headers = {
        "Authorization": f"Bearer {os.getenv('BITLY_API')}"
    }
    # Get the default group_guid for the account
    try:
        #group_resp = requests.get(
        #   f"https://api-ssl.bitly.com/v4/bitlinks/bit.ly/Salad-IGNAIT/clicks?unit=month&units=1",
        #   headers=headers,
        #   timeout=10,
        # )
        group_resp = requests.get(
            f"https://api-ssl.bitly.com/v4/bitlinks/bit.ly/Salad-{affiliate.referral_code}/clicks?unit=month&units=1",
            headers=headers,
            timeout=10,
        )
        group_resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        abort(500)
    if group_resp.status_code != requests.codes.ok:
        return None
    return group_resp.json()["link_clicks"][0]["clicks"]

@dashboard_controller.route("/dashboard", methods=["GET"])
@login_required
def dashboard_get() -> Response | str:
    """
    Get the user dashboard if logged in.

    :return: Returns the dashboard template, or redirect to login.
    """
    user = UserDAO.get_user_by_id(current_user.id_user)
    affiliate = AffiliateDAO.get_affiliate_by_email(user.email)
    if not affiliate:
        return abort(403) # The user is not an affiliate...

    if not Path.is_file(constants.CSV_LINKS_PATH) or \
            not Path.is_file(constants.CSV_CODES_PATH):
        abort(404)

    qualifying_links = 0
    with Path.open(constants.CSV_LINKS_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("Initial UTM Campaign").lower() == affiliate.referral_code.lower() \
                    and row.get("Cohort") == "All User Profiles":
                qualifying_links += int(row.get(
                    "Jun 1 2024, 12:00AM - Jun 21 2025, 8:51AM"
                ))


    qualifying_codes = 0
    with Path.open(constants.CSV_CODES_PATH, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("ReferralCode").lower() == affiliate.referral_code.lower() \
                    and row.get("Cohort") == "All User Profiles":
                qualifying_codes += int(row.get(
                    "Jun 1 2024, 12:00AM - Jun 21 2025, 9:27AM"
                ))

    return render_template(
        "dashboard.html",
        bitly_clicks=get_bitly_links_stat(affiliate),
        qualifying_links=int(qualifying_links),
        qualifying_codes=int(qualifying_codes),
        affiliate=affiliate)

    return abort(403)
