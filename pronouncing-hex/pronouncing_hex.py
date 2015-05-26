import fileinput
from collections import namedtuple

HexChar = namedtuple('HexChar', ['ones', 'tens', 'teens'])

HEX_CHARS = {
    '0': HexChar('bitey', 'zero', None),
    '1': HexChar('one', 'ten', 'eleven'),
    '2': HexChar('two', 'twenty', 'twelve'),
    '3': HexChar('three', 'thirty', 'thirteen'),
    '4': HexChar('four', 'fourty', 'fourteen'),
    '5': HexChar('five', 'fifty', 'fifteen'),
    '6': HexChar('six', 'sixty', 'sixteen'),
    '7': HexChar('seven', 'seventy', 'seventeen'),
    '8': HexChar('eight', 'eighty', 'eighteen'),
    '9': HexChar('nine', 'ninety', 'nineteen'),
    'A': HexChar('a', 'atta', 'abteen'),
    'B': HexChar('bee', 'bibbity', 'bibteen'),
    'C': HexChar('cee', 'city', 'cleventeen'),
    'D': HexChar('dee', 'dickety', 'dibbleteen'),
    'E': HexChar('e', 'ebbity', 'eggteen'),
    'F': HexChar('ef', 'fleventy', 'fleventeen'),
}

def pronounce_byte(byte):
    nib1, nib2 = byte

    if nib2 == '0':
        return HEX_CHARS[nib1].tens
    elif nib1 == '1':
        return HEX_CHARS[nib2].teens
    else:
        mapped_nibs = [HEX_CHARS[nib1].tens, HEX_CHARS[nib2].ones]
        return '-'.join(nib for nib in mapped_nibs if nib)


for line in fileinput.input():
    if not line:
        continue

    value = line.strip()[2:]
    hex_bytes = [(value[i*2], value[i*2 + 1]) for i in range(len(value) // 2)]

    pronounced = ' bitey '.join(pronounce_byte(b) for b in hex_bytes)

    print('0x%s: "%s"' % (value, pronounced.replace('bitey bitey', 'bitey')))
