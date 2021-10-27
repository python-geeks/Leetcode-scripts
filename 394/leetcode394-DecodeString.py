class Solution:
    def decodeString(self, s: str) -> str:
        import re
        patt = "(\d+)\[([a-z]+)\]"

        found = re.findall(patt, s)
        while found:
            for rep, cnt in found:
                s = s.replace(f'{rep}[{cnt}]', cnt * int(rep))
            found = re.findall(patt, s)

        return s