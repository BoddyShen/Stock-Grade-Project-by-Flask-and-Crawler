"""User model"""
from flask_login import UserMixin
from werkzeug.security import check_password_hash

from root.globals import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Load the user object from the user ID stored in the session"""
    return User.objects(pk=user_id).first()


class User(db.Document, UserMixin):

    """User model

    When sparse=True combined with unique=True and required=False
    means that uniqueness won't be enforced for None values
    """

    # User editable fields
    username = db.StringField(
        required=True, unique=True, max_length=40, index=True)

    password_hash = db.StringField(required=False, index=True)

    stocks = db.ListField(required=False, index=True)

    def __repr__(self):
        """Define what is printed for the user object"""
        return f"Username: {self.username} id: {self.id}"

    def check_password(self, password):
        """Checks that the pw provided hashes to the stored pw hash value"""
        return check_password_hash(self.password_hash, password)

    def add_stock(self, stock):
        '''Add stock to user's stock list'''
        self.stocks.append(stock)
        return

    def delete_stock(self, index):
        '''Delete stock from user's stock list'''
        self.stocks.pop(index)
        return
