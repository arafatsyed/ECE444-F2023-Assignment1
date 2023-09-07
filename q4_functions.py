class utils:

    def reversed (self, num):
        if (type(num) != int):
            return -1
        reversed_string = str(num)[::-1]
        return int(reversed_string)
    
    def formatter (self, num):
        if (type(num) != int):
            return -1
        binary = bin(num);
        octal = oct(num)

        return binary, octal
