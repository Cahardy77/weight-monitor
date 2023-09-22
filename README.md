# Weight Monitor!
***
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
    * weight_id | integer   |
    * user_id   | integer   |
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
    
###### More to come...