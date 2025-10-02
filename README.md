# MAD1 PROJECT 

- Web App

Flask - is the framework to make and host web applications easily with python .

# Music Streaming App 

MVC ------ Model View Controller 

1) Model ----- Data Storage
2) Controller ----- The Logic Handler 
3) View ----- What the user will see 

VIEW -> 
        HTML Pages that user will see .
        -> Login Page
        -> Dashboard 
        -> Menu 

MODEL -> 
        SQLite DataBase (can just store values)
        User Data -- Name, email, pwd
        Songs -- Song Name, Singer, Lyrics, Rating, Language 

CONTROLLER -> 
            Lets say you are a user and you want to login using your email, pwd
            Logic/bridge b/w the html pages and database
            Login ->
                    Controller will check in DB, if the user exists and verifies the pwd and proceeds .
            Search Songs ->
                            Songs are in the DB, HTML has search bar => Controller will give you the songs that you searched for .

HTML/CSS - To make the interface that the user will see
                -> form tag
                -> table tag 
                -> href

Jinja - To make the templates 
            e.g.
            -> Server's work is to just simply give me html page with my name
            -> name ===> html page with my name (e.g. Anjali - Chennai, Charu - New Delhi)                                              
            <html>                                                      
                <head>
                    <title>Jinja Example</title>
                </head>
            <body>
                Hello {name} {state} <-------- the name that I will give
            </body>
            </html>

FLASK - build our application and run/serve it .
        -> writing the controller logic 
        -> be the server of our application

SQL-Alchemy - 
            -> how can i talk to my database
            -> will help us to talk to the database efficiently in a Python
            -> psycopg (dbms way) => open cursor then write sql query (user adding query) closing
            -> SQL-Alchemy => User(name=Anjali, email=anjali@gmail.com, password=pwd)
                              db.session.add()
                              db.session.commit()

# LET's START

1) Creating Virtual Environment

HTTP Methods - 
-> GET - when we are seeking some resource from the server (getting the resources)
-> POST - when I want to send a resource to the server (make a post to the server)
-> PUT - to update a rsource 
-> DELETE - to delete the resource

GET/POST/PUT/DELETE ------ Server ------- Status code and response

200 - OK/Success
201 - Resource 
e.g. you are signing (email and pwd) up for Spotify --> save in the database 
404 - Not Found 

render_template - is a function using which we can render html templates to the server basically I can send html pages to the users from the server .

templates folder - in order to give html pages as a response all the pages should be in the templates folder

Models 
DataBase
sql-alchemy 
pythonic way helps us talk to the DB 

ORM - Object Relational Making


