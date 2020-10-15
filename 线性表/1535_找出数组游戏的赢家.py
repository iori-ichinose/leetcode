class Solution:
    def getWinner(self, arr: list, k: int) -> int:
        cur, next = 0, 1
        lim = len(arr)
        count = 0
        while next < lim:
            if arr[cur] > arr[next]:
                count += 1
                next += 1
            else:
                count = 1
                cur = next
                next += 1
            if count == k:
                return arr[cur]
        return arr[cur]
    '''
    def getWinner(self, arr: list, k: int) -> int:
        flag = arr[0]
        count = 0
        m = max(arr)
        for i in range(len(arr)):
            if arr[0] > arr[1]:
                count += 1
                arr.append(arr.pop(1))
            else:
                flag = arr[1]
                count = 1
                arr.append(arr.pop(0))
            if count == k:
                    return flag
            elif flag == m:
                    return m

        return m
    
    def getWinner(self, arr: list, k: int) -> int:
        win_stat = {}
        m = max(arr)
        while True:
            if arr[0] > arr[1]:
                if arr[0] == m:
                    return m
                try:
                    win_stat[arr[0]] += 1
                except KeyError:
                    win_stat[arr[0]] = 1

                if win_stat[arr[0]] == k:
                    return arr[0]
                arr.append(arr.pop(1))
            else:
                if arr[1] == m:
                    return m
                try:
                    win_stat[arr[1]] += 1
                except KeyError:
                    win_stat[arr[1]] = 1

                if win_stat[arr[1]] == k:
                    return arr[1]
                arr.append(arr.pop(0))
    '''
