import textwrap

alkutarina = ('Kaikki pelissä esiintyvät tarinat tulevat löytymään täältä. '
              'Kun kaikki tarinat on yhdellä tiedostolla, tarinoita pystyy muokata helposti '
              'eikä pääohjelma mene ihan tukkoon.')

wrapper = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
johdantoteksti = wrapper.wrap(text=alkutarina)


def haejohdanto():
    return johdantoteksti

välivaihe = ('Tällein voi lisätä uusia tekstejä.')

wrapper1 = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
keskivaihe = wrapper.wrap(text=välivaihe)


def haevälitarina():
    return keskivaihe

kirje = ('Pelin lopuksi, kun pelaaja on löytänyt viimeisen vihjeen ohjelma hakee tämän funktion'
         'johon tulee ajanmyötä mummon kirjoittama kirje pelaajalle. '
         'Esimerkiksi jokin opetus elämästä tms.')

wrapper2 = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
loppu = wrapper.wrap(text=kirje)


def kirje():
    return loppu