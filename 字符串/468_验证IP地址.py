from typing import List


class Solution:
    def isIPv4(self, IP: List[str]) -> str:
        if len(IP) != 4:
            return 'Neither'
        for n in IP:
            if len(n) == 0 or len(n) > 3:
                return 'Neither'
            if (n[0] == '0' and len(n) > 1) or not n.isdigit() or int(n) > 255:
                return 'Neither'
        return 'IPv4'

    def isIPv6(self, IP: List[str]) -> str:
        if len(IP) != 8:
            return 'Neither'
        for n in IP:
            if len(n) == 0 or len(n) > 4 or any(
                    ch not in self.valid for ch in n):
                return 'Neither'
        return 'IPv6'

    def validIPAddress(self, IP: str) -> str:
        s = IP.split('.')
        if len(s) != 4:
            self.valid = '0123456789ABCDEFabcdef'
            return self.isIPv6(IP.split(':'))
        else:
            return self.isIPv4(s)
