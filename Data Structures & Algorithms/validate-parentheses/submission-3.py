class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "}":"{", "]":"["}
        st=[]

        for x in s:
            if x in dic and len(st)>0:
                temp = st.pop()
                if dic[x] != temp:
                    return False
                
            else:
                st.append(x)
                
        if len(st)==0:
            return True
        else: 
            return False