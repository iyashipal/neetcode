class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string+ str(len(s))+"#" + s

        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strs = [] #list of strings
        i =0;
        size = 0;
        length, temp = "", ""
        while i<len(s):
            if s[i] != "#":
                length += s[i]
            if s[i] == "#":
                size = int(length)
                temp = s[i+1: i+size+1]
                decoded_strs.append(temp)
                length = ""
                i += size
            i+=1
        return decoded_strs;