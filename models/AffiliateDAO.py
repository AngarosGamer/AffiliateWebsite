"""Handles Data Access for the Affiliate Object."""

from models import sqlite_connection
from models.Affiliate import Affiliate


class AffiliateDAO:
    """Represents an Affiliate's Data Access class - methods handle data access."""

    @staticmethod
    def create_affiliate(affiliate: Affiliate) -> Affiliate:
        """
        Add affiliate to DB.

        :return: An Affiliate once created.
        """
        query = """INSERT INTO Affiliates (
                            email,
                            referral_code
                            )
                   VALUES (?, ?)"""
        params = (
            affiliate.email,
            affiliate.referral_code,
        )
        # TODO: Add try / except clause
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        affiliate.id_affiliate = cursor.lastrowid  # Get generated ID
        cursor.close()
        return affiliate

    @staticmethod
    def get_affiliate_by_id(affiliate_id: int) -> Affiliate | None:
        """
        Get an Affiliate by their ID.

        :return: An Affiliate Object, or None if not found.
        """
        query = "SELECT * FROM Affiliates WHERE id_affiliate = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (affiliate_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Affiliate(*row)
        return None

    @staticmethod
    def get_affiliate_by_email(affiliate_email: str) -> Affiliate | None:
        """
        Get an Affiliate by their email.

        :return: An Affiliate object, or None if not found.
        """
        query = "SELECT * FROM Affiliates WHERE email = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (affiliate_email,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Affiliate(*row)
        return None

    @staticmethod
    def get_affiliate_by_referral_code(referral_code: str) -> Affiliate | None:
        """
        Get an Affiliate by their referral code.

        :return: An Affiliate object, or None if not found.
        """
        query = "SELECT * FROM Affiliates WHERE referral_code = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (referral_code,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Affiliate(*row)
        return None

    @staticmethod
    def update_affiliate(affiliate: Affiliate) -> bool:
        """
        Update Affiliate objet in DB using Affiliate python object.

        :return: Boolean, true if successful update.
        """
        query = """UPDATE Affiliates
                   SET  email = ?, 
                        referral_code = ?
                   WHERE id_affiliate = ?"""
        params = (
            affiliate.email,
            affiliate.referral_code,
            affiliate.id_affiliate,
        )
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        affiliate_updated = cursor.rowcount > 0  # Return true if line was updated
        cursor.close()
        return affiliate_updated

    @staticmethod
    def delete_affiliate(affiliate_id: int) -> bool:
        """
        Delete Affiliate via their AffiliateID.

        :return: Bool of successful delete operation.
        """
        query = "DELETE FROM Affiliates WHERE id_affiliate = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (affiliate_id,))
        db.commit()
        affiliate_deleted = (
            cursor.rowcount > 0
        )
        cursor.close()
        return affiliate_deleted

    @staticmethod
    def get_all_affiliates() -> list[Affiliate]:
        """
        Get all database affiliates.

        :return: A list of all Affiliates in database.
        """
        query = "SELECT * FROM Affiliates"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return [Affiliate(*row) for row in rows]
