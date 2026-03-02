# 1. luo aluksi uusi tietokanta.
create database ohjelmistopeli;

#2. käytä uutta luotua tietokantaa.
use ohjelmistopeli;

#3. lisää tietokantaan sql tiedosto, jota on käytetty flight_game:ssa.
# Minulla tiedosto löytyy tietokoneen C-levyltä o1 kansiosta lp1.sql nimellä
source C:\o1\lp1.sql;

#4. poistetaan tuodusta qsl- tiedostosta game, goal ja goal_reached-taulut.
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS goal_reached;
SET FOREIGN_KEY_CHECKS = 1;

#5. luodaan ensiksi uusi game-taulu.
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

#6. luodaan lopuksi oma item-taulu.
create table item (
      id int auto_increment primary key,
      nimi         varchar(100) null,
	  maa          varchar(40)  null,
      vihje1       varchar(255) null,
      vihje2       varchar(255) null,
      vihje3       varchar(255) null
)
	charset=latin1;

#ryhmän 3 Ohjlemisto 1 ohjelmistopeli-tietokanta on nyt luotu ja valmis.