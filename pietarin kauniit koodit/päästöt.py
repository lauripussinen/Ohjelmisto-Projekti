#funktio hakee tietokannasta lentokentän nimen ja koordinaatit
def lentokentat(icao):
    sql = "SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

# funktio laskee kahden lentokentän etäisyyden.
def etaisyys(icao1, icao2):
    kentta1 = lentokentat(icao1)
    kentta2 = lentokentat(icao2)
    p1 = (kentta1["latitude_deg"], kentta1["longitude_deg"])
    p2 = (kentta2["latitude_deg"], kentta2["longitude_deg"])

    return distance.distance(p1, p2).km

# funktio laskee co2 päästöt kahden lentokentän välillä
def co2(km):
    return km * 0.2
