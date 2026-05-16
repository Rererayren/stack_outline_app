from flask import Flask

from config import Config
from .extensions import db
from .models import climber, route, send, location, grade
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        #check if lookup tables are empty to upload starting data
        if not grade.query.first() and not location.query.first():
            grade510a = grade(grade_name="5.10a")
            grade510b = grade(grade_name="5.10b")
            grade511a = grade(grade_name="5.11a")
            grade511b = grade(grade_name="5.11b")
            grade512a = grade(grade_name="5.12a")
            grade512b = grade(grade_name="5.12b")

            db.session.add_all([grade510a, grade510b, grade511a, grade511b, grade512a, grade512b])  

            yosemite = location(location_name="Yosemite", state="CA")
            joshuaTree = location(location_name="Joshua Tree", state="CA")
            redRock = location(location_name="Red Rock", state="NV")
            redRiverGorge = location(location_name="Red River Gorge", state="KY")
            db.session.add_all([yosemite, joshuaTree, redRock, redRiverGorge])  

            db.session.commit()

            route1 = route(route_name="El Capitan", grade_id=grade512b.grade_id, location_id=yosemite.location_id, date_created=datetime.utcnow())
            route2 = route(route_name="Serenity Crack", grade_id=grade510b.grade_id, location_id=yosemite.location_id, date_created=datetime.utcnow())
            route3 = route(route_name="Illusion Dweller", grade_id=grade510b.grade_id, location_id=joshuaTree.location_id, date_created=datetime.utcnow())
            route4 = route(route_name="Triassic Sands", grade_id=grade510a.grade_id, location_id=redRock.location_id, date_created=datetime.utcnow())
            route5 = route(route_name="Banshee", grade_id=grade511a.grade_id, location_id=redRiverGorge.location_id, date_created=datetime.utcnow())
            db.session.add_all([route1, route2, route3, route4, route5])

            db.session.commit()
            
    return app