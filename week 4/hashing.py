import hashlib, random



def customhash(s): 
        if type(s) == int:
                hv = s
        elif type(s) == float:
                hv = 0
                mult = random.randint(1, 256)
                strval = str(s)
                for fl in strval:
                        hv += mult * ord(fl) 
                        mult += 1
        else:
                if type(s) == str:
                        mult = random.randint(1, 256)
                        hv = 0 
                        for char in s: 
                                hv += mult * ord(char) 
                                mult += 1 

        return hv
                          
                    



