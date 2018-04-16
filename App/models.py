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

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name
        }

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

    def __str__(self):
        return 'User {} {} {}'.format(self.first_name, self.middle_name, self.last_name)
