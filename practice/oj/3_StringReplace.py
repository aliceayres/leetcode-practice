'''
3. 替换空格
题目描述:
将一个字符串中的空格替换成 "%20"
'''

class Solution:
    def stringReplace(self, original, old, new):
        result = ''
        last = 0
        for i in range(len(original)):
            if original[i] == old:
                if i == 0:
                    result += new
                elif i-1 == 0:
                    result += original[i-1] + new
                else:
                    result += original[last:i] + new
                last = i+1
        if last < i+1:
            result += original[last:len(original)]
        return result

slt = Solution()
original = "We are family! "
print(slt.stringReplace(original, ' ', '%20'))