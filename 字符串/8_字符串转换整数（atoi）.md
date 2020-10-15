# 8. 字符串转换整数（atoi）

## [原题](https://leetcode-cn.com/problems/string-to-integer-atoi)

请你来实现一个`atoi`函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

+ 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
+ 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
+ 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
+ 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回0 。

提示：

+ 本题中的空白字符只包括空格字符`' '`
+ 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为`[−2^31, 2^31 − 1]`。如果数值超过这个范围，请返回 `INT_MAX(2^31 − 1)`或`INT_MIN(−2^31)`。

## 解题思路 & 代码实现

### 遍历判断

这种思路比较简单，但是对于边界条件和特殊情况的处理需要反复斟酌，调试~~测试数据wdnmd~~。具体代码如下：

```Python
class Solution:
    # Normal
    # 用类型名作为变量名真的大丈夫？？ 形参：str: str -> s: str
    # def myAtoi(self, str: str) -> int:
    def myAtoi(self, s: str) -> int:
        out = []
        # 去除字符串前导空格
        s = s.lstrip()

        flag = '+'
        sym = ['+', '-']

        # 特殊情况：
        # 1. 空字符串
        # 2. 只有一个符号
        if not s:
            return 0
        if s[0] in sym and len(s) == 1:
            return 0

        # 如果有符号，记录符号并删除
        if s[0] in sym and len(s) > 1:
            flag = s[0]
            s = s[1:]

        for ch in s:
            if ch.isdigit():
                out.append(ch)
            else:
                break

        # 处理溢出（人生苦短我用Python）
        if not out:
            return 0
        elif flag == '-':
            return -min(int(''.join(out)), 2147483648)
        else:
            return min(int(''.join(out)), 2147483647)
```

### __自动机__

> 这种思路我还是第一次学习到（  
> 很巧妙的一种思路

将字符串分为多个字符并经过自动机处理，根据其返回值决定操作。

![自动机](https://assets.leetcode-cn.com/solution-static/8_fig1.PNG)

状态表格：

|               |  ' '  |  +/-   |  number   | other |
| :-----------: | :---: | :----: | :-------: | :---: |
|   __start__   | start | signed | in_number |  end  |
|  __signed__   |  end  |  end   | in_number |  end  |
| __in_number__ |  end  |  end   | in_number |  end  |
|    __end__    |  end  |  end   |    end    |  end  |

左侧一栏表示自动机状态，上侧表示输入要处理的字符。譬如自动机当前字符位于`start`，则下一个接受到空格，仍为`start`状态（前导空格）；若接受到符号，则自动机转为`signed`状态，即当前位变为符号；若接受到了数字字符，则自动机转为`in_number`，即处于一串数字之中；最后若收到了其他字符，则进入了`end`，处理也就终止。对于其他状态也是类似的。

```Python
class Solution:
    class Automation:
        def __init__(self):
            # 0: start
            # 1: signed
            # 2: in_number
            # 3: end
            self.state = 0
            self.sign = 1
            self.ans = 0
            self.table = [
                [0, 1, 2, 3],
                [3, 3, 2, 3],
                [3, 3, 2, 3],
                [3, 3, 3, 3]
            ]

        def get_col(self, c: str):
            if c == ' ':
                return 0
            elif c in ['+', '-']:
                return 1
            elif c.isdigit():
                return 2
            else:
                return 3

        def get(self, c: str):
            self.state = self.table[self.state][self.get_col(c)]

            if self.state == 1:
                self.sign = 1 if c == '+' else -1
            elif self.state == 2:
                self.ans = min(self.ans * 10 + int(c),
                               2147483647 if self.sign == 1 else 2147483648)

    def myAtoi(self, s: str) -> int:
        auto = self.Automation()
        for c in s:
            auto.get(c)
        return auto.sign * auto.ans
```
