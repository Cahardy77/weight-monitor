# Weight Monitor!
***
Please contact the developer at: https://www.linkedin.com/in/christopher-hardy/

Weight Monitor! is a full-stack application that allows a user to keep track of daily weight goals, caloric intake, water intake, and body mass index!
This application is built with Python and Flask at the core. It utilizes an SQL database to record user data. Users can register a new account or login
to an existing account. From there we are able to update and track our weight goals. API calls create a personalized weight monitor program that suggests 
how many calories you should eat as well as how much water you should be drinking.



![Register](https://github.com/Cahardy77/weight-monitor/assets/88852684/6b8e97c6-7561-4ee3-8bfa-1ac2eaac413f) 
![Profile Top](https://github.com/Cahardy77/weight-monitor/assets/88852684/de9ade72-b0e2-4e40-8212-e2e70c856782)
![Profile Bottom](https://github.com/Cahardy77/weight-monitor/assets/88852684/44ea03e9-190c-4c06-995b-9f448ce6bdff)


  ## Tech

Weight Monitor! uses multiple languages and libraries:

- [Python] - object-oriented, high-level programming language with dynamic semantics
- [Flask] - a micro web framework written in Python
- [SQLAlchemy] - designed to operate with a DBAPI implementation built for a particular database
- [PostgreSQL] - highly stable database management system
- [Bootstrap] - front-end development framework for the creation of websites and web apps
- [ChartJS] - free JavaScript library for making HTML-based charts
- [JavaScript] - dynamic programming language that's used for web development
- [HTML, CSS] - The core of any webpage!

## Data Model
![Territory Management 2 0 data model (1)](https://github.com/Cahardy77/weight-monitor/assets/88852684/491e354a-283c-4d68-bc8f-ba8de2b30d65)


## Database:
* users:
    * user_id        | integer   | Primary Key
    * email          | character | Foreign Key
    * password       | character |
    * fname          | character |
    * lname          | character |
    * birth          | timestamp |
    * height         | integer   |
    * gender         | character |
    * activity_level | character |
    * goal           | character |
* weights:
    * weight_id | integer   | Primary Key
    * user_id   | integer   | Foreign Key
    * weight    | double    |
    * date      | timestamp |
    * comment   | character |
* calories:
    * calorie_id | integer   | Primary Key
    * user_id    | integer   | Foreign Key
    * calories   | integer   |
    * date       | timestamp |
    * comment    | character |
* water:
    * water_id | integer   | Primary Key         
    * user_id  | integer   | Foreign Key
    * water    | integer   |         
    * date     | timestamp |
 
      
  ## Installation

Weight Monitor! requires Python3 or higher.
I used Ubuntu for development of this application and I recommend using this or a similar Linux distribution.

Install Python3, PostgreSQL, pip, and VirtualEnv

Using pip install dependencies with this command:


```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

For production environments:
In server.py - main function:

Change
```
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
```

To
```
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=False)
```

You don't want all the logs printing out in a production environment. You should pass logs into a dedicated log file

   ## Running
This command will start the application and you can then view the application at the local address or deploy the application and travel to your created url.

```sh
python3 server.py
```

###### More to come...


