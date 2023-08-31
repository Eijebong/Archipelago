from typing import List, Optional, Iterable

from .data import data


character_decoding_map = {
  0x00: " ", 0x01: "À", 0x02: "Á", 0x03: "Â", 0x04: "Ç",
  0x05: "È", 0x06: "É", 0x07: "Ê", 0x08: "Ë", 0x09: "Ì",
  0x0B: "Î", 0x0C: "Ï", 0x0D: "Ò", 0x0E: "Ó", 0x0F: "Ô",
  0x10: "Œ", 0x11: "Ù", 0x12: "Ú", 0x13: "Û", 0x14: "Ñ",
  0x15: "ß", 0x16: "à", 0x17: "á", 0x19: "ç", 0x1A: "è",
  0x1B: "é", 0x1C: "ê", 0x1D: "ë", 0x1E: "ì", 0x20: "î",
  0x21: "ï", 0x22: "ò", 0x23: "ó", 0x24: "ô", 0x25: "œ",
  0x26: "ù", 0x27: "ú", 0x28: "û", 0x29: "ñ", 0x2A: "°",
  0x2B: "ª", 0x2D: "&", 0x2E: "+", 0x35: "=", 0x36: ";",
  0x50: "▯", 0x51: "¿", 0x52: "¡", 0x5A: "Í", 0x5B: "%",
  0x5C: "(", 0x5D: ")", 0x68: "â", 0x6F: "í", 0x79: "⬆",
  0x7A: "⬇", 0x7B: "⬅", 0x7C: "➡", 0x7D: "*", 0x84: "ᵉ",
  0x85: "<", 0x86: ">", 0xA1: "0", 0xA2: "1", 0xA3: "2",
  0xA4: "3", 0xA5: "4", 0xA6: "5", 0xA7: "6", 0xA8: "7",
  0xA9: "8", 0xAA: "9", 0xAB: "!", 0xAC: "?", 0xAD: ".",
  0xAE: "-", 0xB0: "…", 0xB1: "“", 0xB2: "”", 0xB3: "‘",
  0xB4: "’", 0xB5: "♂", 0xB6: "♀", 0xB8: ",", 0xB9: "×",
  0xBA: "/", 0xBB: "A", 0xBC: "B", 0xBD: "C", 0xBE: "D",
  0xBF: "E", 0xC0: "F", 0xC1: "G", 0xC2: "H", 0xC3: "I",
  0xC4: "J", 0xC5: "K", 0xC6: "L", 0xC7: "M", 0xC8: "N",
  0xC9: "O", 0xCA: "P", 0xCB: "Q", 0xCC: "R", 0xCD: "S",
  0xCE: "T", 0xCF: "U", 0xD0: "V", 0xD1: "W", 0xD2: "X",
  0xD3: "Y", 0xD4: "Z", 0xD5: "a", 0xD6: "b", 0xD7: "c",
  0xD8: "d", 0xD9: "e", 0xDA: "f", 0xDB: "g", 0xDC: "h",
  0xDD: "i", 0xDE: "j", 0xDF: "k", 0xE0: "l", 0xE1: "m",
  0xE2: "n", 0xE3: "o", 0xE4: "p", 0xE5: "q", 0xE6: "r",
  0xE7: "s", 0xE8: "t", 0xE9: "u", 0xEA: "v", 0xEB: "w",
  0xEC: "x", 0xED: "y", 0xEE: "z", 0xEF: "▶", 0xF0: ":"
}

character_encoding_map = {value: key for key, value in character_decoding_map.items()}

valid_name_characters = {
    " ", "0", "1", "2", "3", "4", "5", "6", "7", "8",
    "9", "!", "?", ".", "-", "…", "“", "”", "‘", "’",    
    "♂", "♀", ",", "/", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
}


def encode_string(string: str, length: Optional[int] = None) -> bytearray:
    arr = []
    length = len(string) if length is None else length

    for i in range(length):
        if i >= len(string):
            arr.append(0xFF)
            continue

        char = string[i]
        if char in character_encoding_map:
            arr.append(character_encoding_map[char])
        else:
            arr.append(character_encoding_map["?"])

    return bytearray(arr)


def decode_string(string_data: Iterable[int]):
    string = ""
    for code in string_data:
        if code == 0xFF:
            break

        if code in character_decoding_map:
            string += character_decoding_map[code]
        else:
            raise KeyError(f"The following value does not correspond to a character for Pokemon Emerald: {code}")

    return string


def location_name_to_label(name: str) -> str:
    return data.locations[name].label


def int_to_bool_array(num: int) -> List[bool]:
    binary_string = format(num, '064b')
    bool_array = [bit == '1' for bit in reversed(binary_string)]
    return bool_array


def bool_array_to_int(bool_array: List[bool]) -> int:
    binary_string = ''.join(['1' if bit else '0' for bit in reversed(bool_array)])
    num = int(binary_string, 2)
    return num
