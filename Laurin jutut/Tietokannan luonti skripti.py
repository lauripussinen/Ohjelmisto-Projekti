# 1. Luo aluksi uusi tietokanta.
create database ohjelmistopeli;

#2. Käytä uutta luotua tietokantaa.
use ohjelmistopeli;

#3. Lisää tietokantaan sql tiedosto, jota on käytetty flight_game-tietokannassa.
# Minulla tiedosto löytyy tietokoneen C-levyltä o1 kansiosta lp1.sql nimellä.
source C:\o1\lp1.sql;

#4. Poistetaan tuodusta qsl-tiedostosta game, goal ja goal_reached-taulut.
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS goal_reached;
SET FOREIGN_KEY_CHECKS = 1;

#5. Luodaan ensiksi uusi game-taulu.
CREATE TABLE game (
	id int auto_increment primary key,
    screen_name   varchar(40) NULL,
    location      varchar(40) NULL,
    co2_consumed  float default 0,
    co2_budget    float default 5000,
    current_item  int default 0,
    attempts      int default 0
)
	charset=latin1;

#6. Luodaan lopuksi oma item-taulu.
create table item (
      id int auto_increment primary key,
      nimi         varchar(100) null,
	  maa          varchar(40)  null,
      vihje1       varchar(255) null,
      vihje2       varchar(255) null,
      vihje3       varchar(255) null
)
	charset=latin1;

#7. Tarkistetaan onko tietokanta halutun mukainen
show tables;

#9. Jos ja kun tulostuu seuraavat taulut: airport, country, game ja itmes,
# on ryhmän 3 ohjelmistopeli-tietokanta luotu onnistuneesti.