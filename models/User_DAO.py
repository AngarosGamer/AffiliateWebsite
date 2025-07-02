"""Handles Data Access for the User Object."""

from models import sqlite_connection
from models.User import User


class UserDAO:
    """Represents a User's Data Access class - methods handle data access."""

    @staticmethod
    def create_user(user: User) -> User:
        """
        Add user to DB.

        :return: A USER once created.
        """
        query = """INSERT INTO User (
                            email,
                            password,
                            affiliate_status,
                            referral_code
                            )
                   VALUES (?, ?, ?, ?)"""
        params = (
            user.email,
            user.password,
            False, # Affiliate Status defaults to False
            "", # Referral code is empty by default
        )
        # TODO: Add try / except clause
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        user.id_user = cursor.lastrowid  # Récupère l'ID généré automatiquement
        cursor.close()
        return user

    @staticmethod
    def get_user_by_id(user_id: int) -> User | None:
        """
        Get a USER by their ID.

        :return: A User Object, or None if not found.
        """
        query = "SELECT * FROM User WHERE id_user = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row)
        return None

    @staticmethod
    def get_user_by_email(user_email: str) -> User | None:
        """
        Get a USER by their email.

        :return: A User object, or None if not found.
        """
        query = "SELECT * FROM User WHERE email = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (user_email,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row)
        return None

    @staticmethod
    def update_user(user: User) -> bool:
        """
        Update User objet in DB using User python object.

        :return: Boolean, true if successful update.
        """
        query = """UPDATE User
                   SET  email = ?, 
                        password = ?,
                        affiliate_status = ?,
                        referral_code = ?
                   WHERE id_user = ?"""
        params = (
            user.email,
            user.password,
            user.affiliate_status,
            user.referral_code,
            user.id_user,
        )
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        user_updated = cursor.rowcount > 0  # Return true if line was updated
        cursor.close()
        return user_updated

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """
        Delete User via their UserID.

        :return: Bool of successful delete operation.
        """
        query = "DELETE FROM User WHERE id_user = ?"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, (user_id,))
        db.commit()
        user_deleted = (
            cursor.rowcount > 0
        )
        cursor.close()
        return user_deleted

    @staticmethod
    def get_all_users() -> list[User]:
        """
        Get all database users.

        :return: A list of all Users in database.
        """
        query = "SELECT * FROM User"
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return [User(*row) for row in rows]

    @staticmethod
    def search_users(query: str) -> list[User]:
        """
        Search for all Users in database matching query email.

        :param query: Match string to look for.
        :return: A list of all matching Users in database.
        """
        query_text = f"%{query}%"
        query = """
                SELECT * FROM User
                WHERE email LIKE ? OR
                referral_code LIKE ?
            """
        params = (query_text, query_text, )
        db = sqlite_connection.get_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        return [User(*row) for row in rows]
