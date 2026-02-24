import textwrap

tarina = 'Tähän tulee pelin tarina'

# Set column width to 80 characters
wrapper = textwrap.TextWrapper(width=80, break_long_words=False, replace_whitespace=False)
# Wrap text
word_list = wrapper.wrap(text=tarina)


def haetarina():
    return word_list