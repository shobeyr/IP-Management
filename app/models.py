from . import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class IP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    server_name = db.Column(db.String(100), nullable=False)
    ip_public = db.Column(db.String(100), nullable=False)
    ip_private = db.Column(db.String(100), nullable=False)
    dc = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
