class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        segments = [0] * 4

        def dfs(seg_num=0, seg_id=0):
            if seg_id == 4:
                if seg_num == len(s):
                    res.append('.'.join(str(ip) for ip in segments))
                return
            elif seg_num == len(s):
                return
            elif s[seg_num] == '0':
                segments[seg_id] = 0
                dfs(seg_num + 1, seg_id + 1)

            addr = 0
            for end in range(seg_num, len(s)):
                addr = addr * 10 + int(s[end])
                if 0 < addr <= 0xFF:
                    segments[seg_id] = addr
                    dfs(end + 1, seg_id + 1)
                else:
                    break

        dfs()
        return res
