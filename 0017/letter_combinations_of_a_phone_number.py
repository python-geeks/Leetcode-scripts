class Solution:
    def letterCombinations(self, digits: str):

        # first we will be creating a dictionary that
        # maps the digit corresponding letters
        d = {}
        asci = 97  # ascii value of 'a'
        for i in range(2, 10):
            if i == 9 or i == 7:
                # 9 and 7 have 4 letters
                for _ in range(4):
                    if str(i) in d:
                        d[str(i)].append(chr(asci))
                        asci += 1
                    else:
                        d[str(i)] = [chr(asci)]
                        asci += 1

            else:
                for _ in range(3):
                    if str(i) in d:
                        d[str(i)].append(chr(asci))
                        asci += 1
                    else:
                        d[str(i)] = [chr(asci)]
                        asci += 1

        ans = []
        # now we will generate all the possible combinations of the number
        for i in range(len(digits) - 1, -1, -1):
            if ans:
                ans1 = []
                for elem in d[digits[i]]:
                    for ele in ans:
                        ans1.append(elem + ele)

                ans = ans1[:]
                del ans1

            else:
                for ele in d[digits[i]]:
                    ans.append(ele)

        return ans
