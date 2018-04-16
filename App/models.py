from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    first_name = db.Column(db.Text)
    middle_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'User {} {} {}'.format(self.first_name, self.middle_name, self.last_name)
