# Stack Outline App


Project Description: What is this app and who is it for?
App is for climbers that wish to track the routes they have climbed and also inputs in the future for a climbing place to hold users of climbers in their system.

• Database Setup: Instructions on how to run your provided .sql schema script.


Barebones project outline for:
- Python 3
- Flask backend
- Relational DB (SQLite by default)
- SQLAlchemy ORM
- HTML5
- Git version control

## Project Structure

```
stack_outline_app/
  app/
    __init__.py
    extensions.py
    models.py
    routes.py
    static/css/styles.css
    templates/base.html
    templates/index.html
  config.py
  run.py
  ai.md
  NORMILZATION.md
  requirements.txt
  .env.example
  .gitignore
```

## Quick Start

1. Create and activate a virtual environment.
   ```
   python -m venv venv   
   venv\Scripts\activate 
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open http://127.0.0.1:5000

5. Database set up to run fake data when app loads.
   Grades:
    -  5.10a, 5.10b, 5.11a, 5.11b, 5.12a, 5.12b

   Locations
      - Yosemite
      - Joshua Tree
      - Red Rock
      - Red River Gorge

   Routes
      - El Capitan [5.12b]
      - Serenity Crack [5.10b]
      - Illusion Dweller [5.10b]
      - Triassic Sands [5.10a]
      - Banshee [5.11a]
   
   Climbers 
      - Self Input

   Sends 
      - Self Input

## Notes

- SQLite is used out of the box via `DATABASE_URL=sqlite:///app.db`.
- Tables are auto-created at startup for this minimal starter (`db.create_all()` for the Grades and Locations tables).
