)
tarina_funktiot = {
    "Kirje": Tarinat.kirje,
    "Kultainen teelusikka": Tarinat.teelusikka,
    "Kaulakoru": Tarinat.kaulakoru,
    "Nahkahanskat": Tarinat.nahkahanskat,
    "Taskukello": Tarinat.taskukello
}


#esineen tarkistus funktioon lisäys, jotta oikeaan
if tarkista_maa(pelaajan_maa, esine):
    print("Löysit esineen:", esine["nimi"])
if esine["nimi"] in tarina_funktiot:
    for rivi in tarina_funktiot[esine["nimi"]](): \
    print(rivi)

for rivi in Tarinat.johdanto():
        print(rivi)


#pelin luomisfunktio
def luo_peli(nimi, aloitus_icao, difficulty):
    sql = 'INSERT INTO game (screen_name, location, co2_consumed, co2_budget, current_item, attempts, difficulty) VALUES (%s, %s, 0, 5000, 0, 0, %s)'
    cursor = yhteys.cursor()
    cursor.execute(sql, (nimi, aloitus_icao, difficulty))
    yhteys.commit()
    return cursor.lastrowid