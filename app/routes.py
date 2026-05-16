from flask import Blueprint, render_template, request, redirect, url_for
from .models import climber, route, send, location, grade
from .extensions import db
from datetime import datetime
from sqlalchemy import func

main = Blueprint("main", __name__)


@main.route("/")
def index():
    # records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
    climbers = climber.query.order_by(climber.climber_id.desc()).all()
    routes = route.query.order_by(route.route_id.desc()).all()
    sends = send.query.order_by(send.send_id.desc()).all()
    locations = location.query.order_by(location.location_id.desc()).all()
    grades = grade.query.order_by(grade.grade_id.desc()).all()
    totalSends = db.session.query(func.count(send.send_id)).scalar()
    totalClimbers = db.session.query(func.count(climber.climber_id)).scalar()
    totalRoutes = db.session.query(func.count(route.route_id)).scalar()

    return render_template("index.html", climbers=climbers, routes=routes, sends=sends, locations=locations, grades=grades, totalSends=totalSends, totalClimbers=totalClimbers, totalRoutes=totalRoutes)

#create POST for creating new climber via user input
@main.route("/climbers/create", methods=["POST"])
def create_climber():
    full_name_input = request.form.get("full_name")
    email_input = request.form.get("email")
    
    #server-side validation to ensure no "bad data" enters database
    #validation already there since database schema set up correct but another example if not structured 
    if not full_name_input or not email_input: 
        print("missing information")
        return redirect(url_for("main.index"))
        
    if "@" not in email_input or "." not in email_input:
        print("email format is invalid")
        return redirect(url_for("main.index"))
    
    try:
        unique = climber.query.filter_by(email=email_input).first()
        if unique:
            print("Email address already exists.")
            return redirect(url_for("main.index"))
        
        new_climber = climber(full_name=full_name_input, email=email_input, join_date = datetime.utcnow(), recent_activity = datetime.utcnow())
        db.session.add(new_climber)
        db.session.commit()
    except Exception as e:
        db.session.rollback() #ATOMIC Database Transaction principle
        print(f"failed to create user: {e}")
        
    return redirect(url_for("main.index"))

#transaction logic here for example

@main.route("/trackSend", methods=["POST"])
def trackSend():
    climber_id = request.form.get("climber_id")
    route_id = request.form.get("route_id")
    
    if not climber_id or not route_id:
        return redirect(url_for("main.index"))
    try:
        #get climbers information to update relational tables for send information
        active_climber = climber.query.get(climber_id)
        

        #create send record for new ascent entry
        new_send = send(climber_id=int(climber_id), route_id=int(route_id), send_date=datetime.utcnow(), entry_date=datetime.utcnow())
        db.session.add(new_send)
        
        # need to update the recent activity metadata in the climber table to reflect latest activity
        if active_climber:
            active_climber.recent_activity = datetime.utcnow()
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(f"failed to log send: {e}")
    return redirect(url_for("main.index"))

#delete an entry of a send by a climber by send_id
@main.route("/delete_send/<int:send_id>", methods=["POST"])
def delete_send(send_id):

    removeSendEntry = send.query.get(send_id)
    try:
        db.session.delete(removeSendEntry)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Failed to remove: {e}")
        
    return redirect(url_for("main.index"))