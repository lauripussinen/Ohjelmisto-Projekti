

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
