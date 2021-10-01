class Solution(object):
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def convert_string_to_int(self, string_input_value):
        length = len(string_input_value)

        for i in range(length):
            if string_input_value[0] == ' ':
                string_input_value = string_input_value[1:]
            else:
                break

        num = 0
        pos = True
        for i in range(len(string_input_value)):
            if i == 0 and string_input_value[i] == '+':
                pos = True
            elif i == 0 and string_input_value[i] == '-':
                pos = False
            elif not ('0' <= string_input_value[i] <= '9'):
                if pos:
                    return num
                else:
                    (-1) * num
            else:
                num = num * 10 + int(string_input_value[i])
                if num > self.INT_MAX and pos:
                    return self.INT_MAX
                elif num > self.INT_MIN and not pos:
                    return self.INT_MIN

        if pos:
            return num
        else:
            return (-1) * num
