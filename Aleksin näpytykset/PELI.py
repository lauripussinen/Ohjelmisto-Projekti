import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Allu8221!",
    database="ohjelmistopeli"
)

def hae_esineet():
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute("SELECT * FROM item")
    return cursor.fetchall()

def lentokentta(icao):
    sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    return cursor.fetchone()

def etaisyys(icao1, icao2):
    k1 = lentokentta(icao1)
    k2 = lentokentta(icao2)
    p1 = (k1["latitude_deg"], k1["longitude_deg"])
    p2 = (k2["latitude_deg"], k2["longitude_deg"])
    return distance.distance(p1, p2).km

def co2(km):
    return km * 0.2
def luo_peli(nimi, aloitus_icao):
    sql = """
        INSERT INTO game (screen_name, location, co2_consumed, co2_budget, current_item, attempts)
        VALUES (%s, %s, 0, 5000, 0, 0)
    """
    cursor = yhteys.cursor()
    cursor.execute(sql, (nimi, aloitus_icao))
    yhteys.commit()
    return cursor.lastrowid
def hae_peli(game_id):
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute("SELECT * FROM game WHERE id = %s", (game_id,))
    return cursor.fetchone()
def paivita_peli(game_id, location, co2_consumed, current_item, attempts):
    sql = """
        UPDATE game
        SET location=%s, co2_consumed=%s, current_item=%s, attempts=%s
        WHERE id=%s
    """
    cursor = yhteys.cursor()
    cursor.execute(sql, (location, co2_consumed, current_item, attempts, game_id))
    yhteys.commit()

    def anna_vihje(esine, yritykset):
        if yritykset == 0:
            return esine["vihje1"]
        elif yritykset == 1:
            return esine["vihje2"]
        else:
            return esine["vihje3"]

    def tarkista_maa(pelaajan_maa, esine):
        return pelaajan_maa == esine["maa"]

    def lennä(game_id, kohde_icao):
        peli = hae_peli(game_id)

        nykyinen = peli["location"]
        kulutus = peli["co2_consumed"]
        budjetti = peli["co2_budget"]

        km = etaisyys(nykyinen, kohde_icao)
        paasto = co2(km)

        if kulutus + paasto > budjetti:
            print("❌ Et voi lentää! CO₂‑budjetti ylittyisi.")
            return False

        uusi_kulutus = kulutus + paasto
        paivita_peli(game_id, kohde_icao, uusi_kulutus, peli["current_item"], peli["attempts"])

        print(f"✈️ Lensit {km:.1f} km ja kulutit {paasto:.1f} CO₂.")
        print(f"CO₂ yhteensä: {uusi_kulutus:.1f} / {budjetti}")
        return True

    def tarkista_esine(game_id, pelaajan_maa, esineet):
        peli = hae_peli(game_id)
        idx = peli["current_item"]
        yritykset = peli["attempts"]

        esine = esineet[idx]

        if tarkista_maa(pelaajan_maa, esine):
            print("🎉 Löysit esineen:", esine["nimi"])
            paivita_peli(game_id, peli["location"], peli["co2_consumed"], idx + 1, 0)
            return True
        else:
            yritykset += 1
            vihje = anna_vihje(esine, yritykset)
            paivita_peli(game_id, peli["location"], peli["co2_consumed"], idx, yritykset)
            print("❌ Väärä maa!")
            print("💡 Vihje:", vihje)
            return False

def peli():
    nimi = input("Anna pelaajan nimi: ")
    aloitus = input("Anna aloituslentokenttä (ICAO): ").upper()

    game_id = luo_peli(nimi, aloitus)
    esineet = hae_esineet()

    print("\nPeli alkaa! CO₂‑budjetti: 5000\n")

    while True:
        peli = hae_peli(game_id)

        if peli["current_item"] >= len(esineet):
            print("\n🎉 Olet löytänyt kaikki esineet! Peli päättyy!")
            break

        kohde = input("\nMinne haluat lentää (ICAO)? ").upper()

        if not lennä(game_id, kohde):
            continue

        pelaajan_maa = kohde[:2]  # esim. EFHK → FI
        tarkista_esine(game_id, pelaajan_maa, esineet)

peli()