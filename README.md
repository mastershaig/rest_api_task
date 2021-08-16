## Task
Using a python web framework, you must build a REST web service that exposes CRUD
functionality to a database that stores carbon usage data for customers.

## Database
The database should have at least this structure. Feel free to make your data structure
more complex, but be prepared to explain it if it is not obvious.

### user
|  field name       |  type          |
| ------------- |:-------------:|
| id      | long |
| name      | sring      |  

### usage
|  field name       |  type          |
| ------------- |:-------------:|
| id      | long |
| user_id      | id      |  
| usage_type_id      | long      |  
| usage_at      | datetime      |  
| amount      | float      |  

### usage_types
|  field name       |  type          |
| ------------- |:-------------:|
| id      | long |
| name      | string      |  
| unit      | string      |  
| factor      | float      |  


### Data
### usage_types
|  id  | name | unit | factor |
| ---- |:----:|:----:|:------:|
| 100 | electricity | kwh | 1.5 |
| 101 | water | kg | 26.93 |
| 102 | heating | kwh | 3.892 |
| 103 | heating | l | 8.57 |
| 104 | heating | m3 | 19.456 |

### Requirements
- The backend must be made in a python web framework
- You must use an ORM such as SQLAlchemy or Django
- Your backend supports authentication (It's built in to Django)
- The data in the usage_types table above is pre-loaded
- Your API is secured with token-based authentication (such as JWT)
- Your API supports pagination, sorting and a filter by time range when retrieving
- Your API should support all CRUD actions. Try to think about how a frontend might
need to use this to allow users to submit, edit or delete their usage and retrieve it.
- You may use an in-memory database like SQLite
- Your files should be in a Github repository we can access.
- The README in the root directory of your repository should provide instructions so
that we can run and test it locally. We highly recommend you set it up with Docker
to make both our lives easier.
- Your API is documented somewhere and mentioned in your README.
- Please also include in your README how long it took you to complete this task, and
if you had any challenges that you had to overcome.
## Installation and running locally
After you cloned the repository, you can run the docker by this command
- run ```docker-compose up --build -d```

After this, you can view the API documentation on
[http://127.0.0.1:8000/api/v1/docs/](http://127.0.0.1:8000/api/v1/docs/)

```usage_types ``` table is automatically preloaded using data migration. ```users``` and ```usage``` need to be created using API.

It took me around 3 hours to build this. Actually, didn't have any specific challenges.
