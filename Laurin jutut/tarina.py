import textwrap

alkutarina = ('Peli alkaa seuraavanlaisesti: mummosi on ollut Euroopan matkalla ja kotiin palattuuaan hän on huomannut '
              'miten hänen arvotavaransa ovat hävinneet ')

wrapper = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
johdantoteksti = wrapper.wrap(text=alkutarina)


def haetarina():
    return johdantoteksti