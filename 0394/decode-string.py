def extract_digit(self, i: int, s: str):
    digit = ""
    while (s[i] != "["):
        digit += s[i]
        i += 1
    # i + 1 to skip the [
    return i + 1, digit


def decode_word(self, i: int, s: str):
    concat = ""
    while(i < len(s) and s[i] != "]"):
        if (s[i].isdigit()):
            i, digit = self.extract_digit(i, s)
            i, word = self.decode_word(i, s)
            concat += int(digit) * word
        else:
            concat += s[i]
            i += 1
    return i + 1, concat


def decodeString(self, s: str) -> str:
    i, word = self.decode_word(0, s)
    return word
