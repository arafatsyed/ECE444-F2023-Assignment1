class utils:

    def reversed (self, num):
        if (type(num) != int):
            return "invalid"
        reversed_string = str(num)[::-1]
        return int(reversed_string)
    
    def formatter (self, num):
        if (type(num) != int):
            return "invalid"
        binary = bin(num);
        octal = oct(num)

        return binary, octal
