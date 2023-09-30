def parse(str):
    p = {}
    if len(str) == 0:
        return p
    for i in str.split('\n'):
        p[i[0:i.find('=')].strip()] = i[i.find('=')+1:].strip()
    return p

def stringfy(dict):
    str = []
    for k, v in dict.items():
        str.append(f'{k} = {v}')
    return '\n'.join(str)

