from flask import Blueprint, render_template

from .models import climber, route, send, location, grade

main = Blueprint("main", __name__)


@main.route("/")
def index():
    # records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
    climbers = climber.query.order_by(climber.climber_id.desc()).all()
    routes = route.query.order_by(route.route_id.desc()).all()
    sends = send.query.order_by(send.send_id.desc()).all()
    locations = location.query.order_by(location.location_id.desc()).all()
    grades = grade.query.order_by(grade.grade_id.desc()).all()
    return render_template("index.html", climbers=climbers, routes=routes, sends=sends, locations=locations, grades=grades)
