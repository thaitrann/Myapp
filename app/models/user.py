from app import db
 
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    notes = db.relationship('Note', backref='author', lazy='dynamic')
 
    def __repr__(self):
        return '<User {}>'.format(self.email)   