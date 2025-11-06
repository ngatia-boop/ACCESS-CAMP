🏕️ ACCESS-CAMP Flask API
A RESTful Flask API for managing campers, activities, and signups for Access Camp. This backend service allows logging campers, their activities, and signups that link campers to activities at specific times.

🚀 Features
RESTful API with proper HTTP status codes and response formatting

MVC Architecture with clear separation of concerns

Database Models with relationships and validations

Flask-SQLAlchemy ORM for database operations

Flask-Migrate for database migrations

Comprehensive Validations for data integrity

📋 API Endpoints
Campers
GET /campers - List all campers

GET /campers/<id> - Get camper details with signups

POST /campers - Create a new camper

PATCH /campers/<id> - Update camper information

Activities
GET /activities - List all activities

DELETE /activities/<id> - Delete an activity and associated signups

Signups
POST /signups - Create a new signup linking camper to activity

🛠️ Installation & Setup
Prerequisites
Python 3.8+
pip (Python package manager)

Step 1: Clone and Setup
```
git clone <repository-url>
cd ACCESS-CAMP
python3 -m venv env
source env/bin/activate  # Mac/Linux
# OR
.\env\Scripts\activate  # Windows
```

Step 2: Install Dependencies
```
pip install -r requirements.txt
```

Step 3: Database Setup
```
cd server
flask db init
flask db migrate -m 'initial models'
flask db upgrade head
```

Step 4: Seed Database
```
python seed.py
```

Step 5: Run the Server
```
python server/app.py
Server runs on http://localhost:5555
```

🗄️ Database Models
Camper
id (Integer, Primary Key)

name (String, Required)

age (Integer, Required, 8-18)

created_at (DateTime)

updated_at (DateTime)

Activity
id (Integer, Primary Key)

name (String, Required)

difficulty (Integer, Required)

created_at (DateTime)

updated_at (DateTime)

Signup
id (Integer, Primary Key)

time (Integer, Required, 0-23)

camper_id (Integer, Foreign Key)

activity_id (Integer, Foreign Key)

created_at (DateTime)

✅ Validations
Camper Validations
Name is required

Age must be integer between 8 and 18

Signup Validations
Time must be integer between 0 and 23 (hour of day)

Camper must exist

Activity must exist

🧪 Testing
Using Postman
Import the provided Postman collection to test all endpoints.

Using Pytest
```
pytest -x
```

📝 Example API Responses
GET /campers
json
[
  {"id": 1, "name": "Caitlin", "age": 8},
  {"id": 2, "name": "Lizzie", "age": 9}
]
GET /campers/1
json
{
  "id": 1,
  "name": "Nicholas Martinez",
  "age": 12,
  "signups": [
    {
      "id": 39,
      "activity_id": 5,
      "camper_id": 1,
      "time": 8,
      "activity": {
        "id": 5,
        "name": "Hiking by the stream.",
        "difficulty": 2
      }
    }
  ]
}

POST /signups (Success)
json
{
  "id": 100,
  "camper_id": 1,
  "activity_id": 3,
  "time": 9,
  "activity": {
    "id": 3,
    "name": "Swim in the lake.",
    "difficulty": 3
  },
  "camper": {
    "id": 1,
    "name": "Ashley Delgado",
    "age": 11
  }
}


🗂️ Project Structure
```
ACCESS-CAMP/
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── routes/
│   │   ├── campers.py
│   │   ├── activities.py
│   │   └── signups.py
│   └── migrations/
├── requirements.txt
├── seed.py
└── README.md
```

🔗 Relationships
Camper has many Activities through Signups

Activity has many Campers through Signups

Signup belongs to both Camper and Activity

Cascade delete: Deleting an activity removes associated signups

🚨 Error Responses
Validation Errors
json
{
  "errors": ["validation errors"]
}
Not Found Errors
json
{
  "error": "Camper not found"
}

👨‍💻 Development
This is an API-only implementation - no frontend code is included. The focus is on building a robust, well-structured Flask backend following MVC architecture patterns.

📄 License
This project is part of the Access Camp technical assessment.

Author
Ann Ngatia.

