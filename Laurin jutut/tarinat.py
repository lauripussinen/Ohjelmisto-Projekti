import textwrap

alkutarina = ('Näin voi lisätä tekstejä.')

wrapper = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
johdantoteksti = wrapper.wrap(text=alkutarina)


def haejohdanto():
    return johdantoteksti

alkutarina1 = ('Tällein voi lisätä uusia tekstejä.')

wrapper1 = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
johdantoteksti1 = wrapper.wrap(text=alkutarina1)


def haejohdanto1():
    return johdantoteksti1

alkutarina2 = ('Ja näin tekstejä lisätään selkeästi päätiedostoon. '
               'Näin saadaan selkeytettyä ohjelmia huomattavasti. '
               'Tänne ajattelin, että voidaan lisätä kaikki pelin tarinat, '
               'jossa niitä oystytään helposti muokkaamaan tarpeen tullen.')

wrapper2 = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)
johdantoteksti2 = wrapper.wrap(text=alkutarina2)


def haejohdanto2():
    return johdantoteksti2