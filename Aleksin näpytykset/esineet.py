#1. Kultainen teelussikka sijaitsee Ruotsissa.
#1. vihje: Kultainen teelusikka sijaitsee maassa joka tunnetaan kolmesta kruunusta
#2. vihje: Kultainen teelusikka sijaitsee maassa jossa on paremmat lihapullat
#3. vihje: Kultainen teelusikka sijatsee maassa jossa juhlitanaan keskikesän juhlaa

#2. Taskukello sijaitsee Italiassa.
#1. vihje: Taskukello sijaitsee maassa, jossa eqyptin prinssi syntyi
#2. vihje: Taskukello sijaitsee maassa, joka tunnettaan eräästä diktaattorista
#3. vihje: Taskukello sijaitsee maassa, jossa syödään pizzaa ja pastaa, Tollo!

#3. Kaulakoru sijaitsee Englannissa
#1. vihje: Kaulakoru sijaitsee maassa, jossa sinua tarkkaillaan jatkuvasti
#2. vihje: Kaulakoru sijaitsee maassa, jossa yleensä sää on kamala
#3. vihje: Kaulakoru sijaitsee maassa, jossa juodaan paljon teetä.

#4. Nahkahanskat sijaitsee Ranskassa
#1. vihje: Nahkahanskat sijaitsee maassa, jossa ilma savuaa
#2. vihje: Nahkahanskat sijaitsee maassa, johon kaikki haluavat matkustaa, mutta eivät pidä paikallisista
#3. vihje: Nahkahanskat sijaitsee maassa, jossa patonki ja croisantit on iso juttu

#5. Kirje sijaitsee Romaniassa
#1. Kirje sijaitsee maassa, jossa jokainen ajaa vanhalla mersulla.
#2. kirje sijaitsee maassa joka on hyvin köyhä
#3. Kirje sijaitsee samassa maassa mistä Dracula on kotoisin.

esineet = [
    {   "nimi": "Kultainen teelusikka",
        "maa": "Ruotsi",
        "vihje1": "Kultainen teelusikka sijaitsee maassa, joka tunnetaan kolmesta kruunusta.",
        "vihje2": "Kultainen teelusikka sijaitsee maassa, jossa on paremmat lihapullat.",
        "vihje3": "Kultainen teelusikka sijaitsee maassa, jossa juhlitaan keskikesän juhlaa."
    },
    {"nimi": "Taskukello",
        "maa": "Italia",
        "vihje1": "Taskukello sijaitsee maassa, jossa Egyptin prinssi syntyi.",
        "vihje2": "Taskukello sijaitsee maassa, joka tunnetaan eräästä diktaattorista.",
        "vihje3": "Taskukello sijaitsee maassa, jossa syödään pizzaa ja pastaa, Tollo!"
    },
    {   "nimi": "Kaulakoru",
        "maa": "Englanti",
        "vihje1": "Kaulakoru sijaitsee maassa, jossa sinua tarkkaillaan jatkuvasti.",
        "vihje": "Kaulakoru sijaitsee maassa, jossa sää on yleensä kamala.",
        "vihje3": "Kaulakoru sijaitsee maassa, jossa juodaan paljon teetä."
    },
    {   "nimi": "Nahkahanskat",
        "maa": "Ranksa",
        "vihje1": "Nahkahanskat sijaitsevat maassa, jossa ilma savuaa.",
        "vihje2": "Nahkahanskat sijaitsevat maassa, johon kaikki haluavat matkustaa, mutta eivät pidä paikallisista.",
        "vihje3": "Nahkahanskat sijaitsevat maassa, jossa patonki ja croissantit ovat iso juttu."
    },
    {  "nimi": "Kirje",
        "maa": "Romania",
        "vihje1": "Kirje sijaitsee maassa, jossa jokainen ajaa vanhalla mersulla.",
        "vihje2": "Kirje sijaitsee maassa, joka on hyvin köyhä.",
        "vihje3": "Kirje sijaitsee maassa, mistä Dracula on kotoisin."
    }
]

#Funktio vihjeelle
yritykset = 0
nykyinen_esine = 0

def anna_vihje():
    esine=esineet[nykyinen_esine]
    if yritykset == 0:
        return esine["vihje1"]
    elif yritykset == 1:
        return esine["vihje2"]
    else:
        return esine["vihje3"]

#Funktio joka tarkastaa onko pelaaja siinä maassa jossa vihje on
def tarkistus_maa_oikea(pelaajan_maa,nykyinen_esine,esineet):
    esine=esineet[nykyinen_esine]
    return pelaajan_maa == esine["maa"]
#Funktio jos pelaaja on lentänyt oikeaan maahan
#pelaajan_maa muuttuja pitää esitellä kun haetaan tietokannasta oikea maa.
if tarkistus_maa_oikea(pelaajan_maa, nykyinen_esine, esineet):
    print("Olet löytänyt esineen: ", esineet[nykyinen_esine]["nimi"])
    nykyinen_esine += 1
    yritykset = 0
else:
    yritykset += 1
    print("Väärä maa!!!")
    print("Vihje: ", anna_vihje())
#tee hakemis funktio tietokannasta


CREATE TABLE iso_country (
    iso_country CHAR(2) PRIMARY KEY,
    name VARCHAR(100),
    continent VARCHAR(10),
    wikipedia_link VARCHAR(255),
    keywords VARCHAR(255)
);

CREATE TABLE airport (
    ident VARCHAR(10) PRIMARY KEY,
    id INT,
    type VARCHAR(20),
    name VARCHAR(100),
    latitude_deg DOUBLE,
    longitude_deg DOUBLE,
    elevation_ft INT,
    continent VARCHAR(10),
    iso_country CHAR(2),
    iso_region VARCHAR(10),
    municipality VARCHAR(100),
    scheduled_service VARCHAR(10),
    gps_code VARCHAR(10),
    iata_code VARCHAR(10),
    local_code VARCHAR(10),
    home_link VARCHAR(255),
    wikipedia_link VARCHAR(255),
    keywords VARCHAR(255),
    FOREIGN KEY (iso_country) REFERENCES iso_country(iso_country)
);

CREATE TABLE game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    screen_name VARCHAR(40) NOT NULL,
    location VARCHAR(10),
    co2_consumed FLOAT DEFAULT 0,
    co2_budget FLOAT DEFAULT 5000,
    current_item INT DEFAULT 0,
    attempts INT DEFAULT 0,
    FOREIGN KEY (location) REFERENCES airport(ident)
);

CREATE TABLE goal (
    id INT PRIMARY KEY,
    name VARCHAR(40),
    description VARCHAR(255),
    icon VARCHAR(255),
    target VARCHAR(40),
    target_minvalue INT,
    target_maxvalue INT,
    target_text VARCHAR(255)
);

CREATE TABLE goal_reached (
    game_id INT,
    goal_id INT,
    FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (goal_id) REFERENCES goal(id)
);

CREATE TABLE item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nimi VARCHAR(100),
    maa CHAR(2),
    vihje1 VARCHAR(255),
    vihje2 VARCHAR(255),
    vihje3 VARCHAR(255),
    FOREIGN KEY (maa) REFERENCES iso_country(iso_country)
);

CREATE TABLE flight_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    from_airport VARCHAR(10),
    to_airport VARCHAR(10),
    distance_km FLOAT,
    co2_used FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (game_id) REFERENCES game(id)
);