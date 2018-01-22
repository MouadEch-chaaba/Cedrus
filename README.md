# [Cedrus](https://www.cedrus.ma/) internship application project

### Project description
This is an internship test application project.

The main idea of the project is to Build a REST API using Django Rest Framework.
The API should give the users the possibility to deal with Ideas.

Each user can create/update and delete an idea. All users could view 
other users ideas but only the creator of the idea that could update or delete it.

### Project details

* The Idea model:

        The idea is composed of 3 parts:
        1.The idea content : a string which holds the text of the idea.
        2.The creation date : the Idea creation date.
        3.The modification date : the date where the idea was last modified.

* The HTTP methods and Endpoints:

|Method|Endpoint|Description|
|------|:---------------------:|------------------------------------------:|
|GET   |/users/<id>/ideas/​     |​allow to list all ideas of a specific user.|
|GET   |/users/<id>/ideas/<id>/​|​allow to retrieve an idea.                 |
|POST  |/users/<id>/ideas/     ​​|​allow to create a new idea.                |
|PUT   |/users/<id>/ideas/<id>/​​|​allow to modify an existing idea.          |
|DELETE|/users/<id>/ideas/<id>/​​|​allow to delete an idea.                   |

* Authentication:
    
    Before a user can perform any action to the API, he must be authenticated, which means he
already have an account and provided the necessary credentials to access the api.

    We can choose any authentication method that we want, for example:
        
        1.Basic Username/Passwork
        2.Token based authentication
        3. ...

