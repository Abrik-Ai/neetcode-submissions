class Solution:

    def encode(self, strs: List[str]) -> str:
        e_s = ""
        for s in strs:
            e_s += str(len(s)) + "#" + s
        return e_s
    def decode(self, s: str) -> List[str]:
        d_s, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            d_s.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length 
        return d_s
