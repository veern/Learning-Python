def myAtoi(s: str) -> int:
        s = s.strip()
        if s == "": 
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0].isdigit():
            sign = 1
        for i, number in enumerate(s):
            if not number.isdigit():
                s = s[:i]
                break
        if len(s):
            result = int(s) * sign
        else:
            result = 0
        if result < -2**31:
            result = -2**31
        elif result > 2**31-1:
            result = 2**31-1
        return result
        

print(myAtoi("+1"),)