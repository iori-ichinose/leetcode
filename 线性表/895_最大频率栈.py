class FreqStack:
    def __init__(self):
        self.max_freqs = {1: []}
        self.counters = {}
        self.maxing = [1]

    def push(self, x: int) -> None:
        if x in self.counters:
            self.counters[x] += 1
            f = self.counters[x]
            if f not in self.max_freqs:
                self.max_freqs[f] = [x]
            else:
                self.max_freqs[f].append(x)
            if f > self.maxing[-1]:
                self.maxing.append(f)
        else:
            self.counters[x] = 1
            self.max_freqs[1].append(x)

    def pop(self) -> int:
        res = self.max_freqs[self.maxing[-1]].pop()
        self.counters[res] -= 1
        if not self.max_freqs[self.maxing[-1]]:
            self.maxing.pop()
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
