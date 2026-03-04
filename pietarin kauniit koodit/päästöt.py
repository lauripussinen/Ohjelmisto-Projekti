# funktio laskee kahden lentokentän etäisyyden.
def etaisyys(icao1, icao2):
    kentta1 = lentokentat(icao1)
    kentta2 = lentokentat(icao2)
    p1 = (kentta1["latitude_deg"], kentta1["longitude_deg"])
    p2 = (kentta2["latitude_deg"], kentta2["longitude_deg"])

    return distance.distance(p1, p2).km

# funktio laskee co2 päästöt kahden lentokentän välillä riippuen vaikeustasosta
def vaikeustaso(H, K, V, km, vaikeustaso):
    if vaikeustaso == 'H':
        return km * 0.2
    elif vaikeustaso == 'K':
        return km * 0.4
    elif vaikeustaso == 'V':
        return km * 0.6