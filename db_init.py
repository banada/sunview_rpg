import MySQLdb

#Connect to localhost - user must be created first
db = MySQLdb.connect("localhost", "banada", "banada")
#Create a separate workspace (cursor instance) with the connection
cursor = db.cursor()

def create_db():
    cursor.execute("CREATE DATABASE sunview_rpg")
    cursor.execute("use sunview_rpg")
    cursor.execute("CREATE TABLE map (\
                     id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\
                     x INT,\
                     y INT,\
                     terrain VARCHAR(32)\
                   )")
    cursor.execute("CREATE TABLE characters (\
                     id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,\
                     name VARCHAR(32),\
                     x INT,\
                     y INT,\
                     speed INT,\
                     is_player BIT(1) NOT NULL DEFAULT 0\
                   )")

#Set map dimensions
def set_map_dim(x_dim, y_dim):
    for x in range(0,x_dim):
        for y in range (0,y_dim):
            cursor.execute("INSERT INTO map(x,y) VALUES(%s,%s)", (x, y))
            db.commit()

#Create player
def create_player(player_name, x_dim, y_dim, speed):
    cursor.execute("INSERT INTO characters(name,x,y,speed)\
                    VALUES(%s,%s,%s,%s)", (player_name, x_dim, y_dim, speed))
    db.commit()

#Move a player / Change their stats
def set_player(player_name, x_dim=-1, y_dim=-1, speed=-1):

    #Request and store previous values - this allows optional args
    cursor.execute("SELECT speed FROM characters WHERE name=%s", (player_name))
    prev_speed = cursor.fetchone()
    if speed < 0:
        speed = prev_speed
    print(speed)

    cursor.execute("SELECT x FROM characters WHERE name=%s", (player_name))
    prev_x = cursor.fetchone()
    if x_dim < 0:
        x_dim = prev_x
    print(x_dim)

    cursor.execute("SELECT y FROM characters WHERE name=%s", (player_name))
    prev_y = cursor.fetchone()
    if y_dim < 0:
        y_dim = prev_y
    print(y_dim)

    cursor.execute("UPDATE characters SET\
                     x=%s,\
                     y=%s,\
                     speed=%s\
                    WHERE name=%s", (x_dim, y_dim, speed, player_name))
    db.commit()

#Set/Destroy a wall

#TESTING
create_db()
set_map_dim(5, 5)
create_player("Perezoso the Folivore",0,0,1)
set_player("Perezoso the Folivore",1,1,0)
