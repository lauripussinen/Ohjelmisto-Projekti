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

alter
table
airport
add
unique
key
ident_unique(ident);

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
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
location
VARCHAR(40)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
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
0,
FOREIGN
KEY(location)
REFERENCES
airport(ident)
)
ENGINE = InnoDB
DEFAULT
CHARSET = latin1
COLLATE = latin1_swedish_ci;

CREATE
TABLE
item(
    id
INT
AUTO_INCREMENT
PRIMARY
KEY,
nimi
VARCHAR(100)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
maa
VARCHAR(40)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
vihje1
VARCHAR(255)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
vihje2
VARCHAR(255)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
vihje3
VARCHAR(255)
CHARACTER
SET
latin1
COLLATE
latin1_swedish_ci,
FOREIGN
KEY(maa)
REFERENCES
country(iso_country)
) ENGINE = InnoDB
DEFAULT
CHARSET = latin1
COLLATE = latin1_swedish_ci;