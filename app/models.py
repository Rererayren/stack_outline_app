from .extensions import db
from datetime import datetime

class climber(db.Model):
    climber_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    recent_activity = db.Column(db.DateTime, default=datetime.utcnow)
    sends = db.relationship("send", back_populates="climber")
    
    def __repr__(self):
        return f"<Climber {self.full_name}>"
    
class route(db.Model):
    route_id = db.Column(db.Integer, primary_key=True)  
    route_name = db.Column(db.String(120), nullable=False)
    grade_id = db.Column(db.String(20),  db.ForeignKey("grade.grade_id"), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("location.location_id"), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    grade = db.relationship("grade", back_populates="routes")
    location = db.relationship("location", back_populates="routes")
    
    def __repr__(self):
        return f"<Route {self.route_name}>"
    
class send(db.Model):
    send_id = db.Column(db.Integer, primary_key=True)
    climber_id = db.Column(db.Integer, db.ForeignKey("climber.climber_id"), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("route.route_id"), nullable=False)
    send_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    climber = db.relationship("climber", back_populates="sends")
    route = db.relationship("route", back_populates="sends")
    
    def __repr__(self):
        return f"<Send {self.send_id}>"
    
class location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    routes = db.relationship("route", back_populates="location")
    
    def __repr__(self):
        return f"<Location {self.location_name}>"
    
class grade(db.Model):
    grade_id = db.Column(db.Integer, primary_key=True)
    grade_name = db.Column(db.String(120), nullable=False)
    routes = db.relationship("route", back_populates="grade")
    
    def __repr__(self):
        return f"<Grade {self.grade_name}>"