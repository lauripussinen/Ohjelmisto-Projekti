create
database
ohjelmistopeli;

source(mulla
on
tässä
seuraavanlainen
koodi: C:\o1\lp1.sql;)

SET
FOREIGN_KEY_CHECKS = 0;

DROP
TABLE
IF
EXISTS
game;
DROP
TABLE
IF
EXISTS
goal;
DROP
TABLE
IF
EXISTS
goal_reached;
DROP
TABLE
IF
EXISTS
ports;
SET
FOREIGN_KEY_CHECKS = 1;

CREATE
TABLE
game(
    id
INT
AUTO_INCREMENT
PRIMARY
KEY,
screen_name
VARCHAR(40)
NULL,
location
VARCHAR(40)
NULL,
co2_consumed
FLOAT
DEFAULT
0,
co2_budget
FLOAT
DEFAULT
5000,
current_item
INT
DEFAULT
0,
attempts
INT
DEFAULT
0
)
DEFAULT
CHARSET = latin1;

create
table
item
(
    id           int auto_increment
primary key,
nimi         varchar(100)
null,
maa
varchar(40)
null,
vihje1
varchar(255)
null,
vihje2
varchar(255)
null,
vihje3
varchar(255)
null
)
charset = latin1;