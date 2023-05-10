import datetime
from application import db, flask_bcrypt


class User(db.Model):

    # The primary key for each user record.
    id = db.Column(db.Integer, primary_key=True)

    # The unique email for each user record.
    email = db.Column(db.String(255), unique=True)

    # The unique username for each record.
    username = db.Column(db.String(40), unique=True)

    # The hashed password for the user
    password = db.Column(db.String(60))

    #  The date/time that the user account was created on.
    created_on = db.Column(db.DateTime, default=datetime)

    #there phone number
    phone_number = db.Column(db.String(60))

    #user homepage number
    homePage_number = db.Column(db.Integer) #can be null

    def __init__(self, email, username, phone_number, homePage_number, password):
        """Initialize the user object with the required attributes."""

        self.email = email
        self.username = username
        self.phone_number = phone_number
        self.homePage_number = homePage_number
        self.password = flask_bcrypt.generate_password_hash(password)
        self.created_on = datetime.datetime.utcnow()


    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        """All our registered users are authenticated."""
        return True

    def is_active(self):
        """All our users are active."""
        return True

    def is_anonymous(self):
        """We don't have anonymous users; always False"""
        return False

    def get_id(self):
        """Get the user ID."""
        return str(self.id)
