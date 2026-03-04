)
tarina_funktiot = {
    "Kirje": Tarinat.kirje,
    "Kultainen teelusikka": Tarinat.teelusikka,
    "Kaulakoru": Tarinat.kaulakoru,
    "Nahkahanskat": Tarinat.nahkahanskat,
    "Taskukello": Tarinat.taskukello
}


#esineen tarkistus funktioon lisäys, jotta esineen löydyttyä tulostuu sen tarina
if tarkista_maa(pelaajan_maa, esine):
    print("Löysit esineen:", esine["nimi"])
if esine["nimi"] in tarina_funktiot:
    for rivi in tarina_funktiot[esine["nimi"]](): \
    print(rivi)

#luo pelin alkuun johdantotarinan
for rivi in Tarinat.johdanto():
        print(rivi)

#resetoi vanhan pelin
def resetoi_peli(game_id, aloitus_icao, difficulty):
    sql = 'UPDATE game SET location=%s, co2_consumed=0, current_item=0, attempts=0, difficulty=%s WHERE id=%s'
    cursor = yhteys.cursor()
    cursor.execute(sql, (aloitus_icao, difficulty, game_id))
    yhteys.commit()
    cursor.close()

#luo uuden pelin
def luo_peli(nimi, aloitus_icao, difficulty):
    sql = 'INSERT INTO game (screen_name, location, co2_consumed, co2_budget, current_item, attempts, difficulty) VALUES (%s, %s, 0, 5000, 0, 0, %s)'
    cursor = yhteys.cursor()
    cursor.execute(sql, (nimi, aloitus_icao, difficulty))
    yhteys.commit()
    return cursor.lastrowid

#hakee peliin
def hae_maan_iso_koodi(nimi):
    sql = "SELECT iso_country FROM country WHERE name = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (nimi,))
    tulos = cursor.fetchone()
    cursor.close()
    if tulos:
        return tulos["iso_country"]

#pääohjelmassa, jos pelaaja haluaa tehdö jo luodulle pelaajalle uuden pelin
else:
    for rivi in Tarinat.johdanto():
        print(rivi)
    print("Peli alkaa! CO2-budjetti: 5000")
    aloitus = 'EFHK'
    difficulty = input("Valitse vaikeustaso (HELPPO/KESKIVAIKEA/VAIKEA): ").upper()
    resetoi_peli(vanha_peli["id"], aloitus, difficulty)
    game_id = vanha_peli["id"]