class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for ch in num:
            while k and st and st[-1] > ch:
                st.pop()
                k -= 1
            st.append(ch)

        while k:
            st.pop()
            k -= 1

        res = ''.join(st).lstrip('0')
        return res if res else '0'
