class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = True, True
        person = 0
        se_list = list(senate)
        while R and D:
            R, D = False, False
            for i in range(len(se_list)):
                if se_list[i] == 'R':
                    R = True
                    if person < 0:
                        se_list[i] = '0'
                    person += 1
                elif se_list[i] == 'D':
                    D = True
                    if person > 0:
                        se_list[i] = '0'
                    person -= 1
        return 'Radiant' if person > 0 else 'Dire'
