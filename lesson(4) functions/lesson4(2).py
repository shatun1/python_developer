def get_sep(sep, sep_len):
    return sep * sep_len

get_sep("-", 100)
get_sep('*', 100)

sep = get_sep('-', 25)
text = 'Hello {} Func {}'.format(sep, sep)
print(text)







