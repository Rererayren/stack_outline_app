NORMALIZATION.md that contains:
• Original Functional Dependencies: A list of all functional dependencies identified in the starting schema.

    Climbers Table:
    Climber ID -> full_name, email, join_date, recent_activity

    Routes Table: 
    Route ID -> route_name, grade, location, recent_activity

    Sends Table: 
    Send ID -> climber_id, route_id, send_date, entry_date

• Anomaly Identification: An explanation of any potential update, insertion, or deletion anomalies found in the original structure.
    Assumptions: Locations do not change for routes since they are outside or in one location/ unique for that route id/name
    
    Update Anomaly: if a grade is renamed to a different scale like '5.5-' is equivalent to '5.5a' if a gym decides to rename the grade then theyd have to update that for all multiple plus routes associated with it. Additionally if a route is reevaluated harder (+) then that change would need to be updated to all.

    Insert Anomaly: Cannot create or use new grade until at least one route uses the grade

    Deletion Anomaly: If a route is deleted and it contains the only unique grade for a certain route like '5.14a' then that is no longer available to use in the system

• Decomposition Steps: If a table violates 3rd Normal Form, show the step-by-step decomposition into smaller tables.

    Remove transitive depenedecies in table: Grade was moved to a new table because these need to be allowed to exist beyond a route tied to it by creating a lookup table. Location dependecny also exists to store metadata about the location field for a lookup instead via a key and then you can have location name and state. The location and grade columns were replaced with foreign keys Location ID and Grade ID to remove the transitive dependency
    
    Climbers Table: 
    climber_id (PK), full_name, email, join_date, recent_activity

    Grade Table: 
    grade_id (PK), grade_name

    Locations Table:
    location_id (PK), location_name, state

    Routes Table:
    route_id (PK), route_name, grade_id (FK), location_id (FK), date_created

    Sends Table:
    send_id (PK), climber_id (FK), route_id (FK), send_date, entry_date
