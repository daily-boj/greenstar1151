keyboard = ['`','1','2','3','4','5','6','7','8','9','0','-','=','','Q','W','E','R','T','Y','U','I','O','P','[',']','\\','','A','S','D','F','G','H','J','K','L',';',"'",'','Z','X','C','V','B','N','M',',','.','/']
s_out = ''

s_in = input()
try:
    while s_in != '':
        for s in s_in:   
            if s == ' ':
                s_out += ' '
            else:
                i = keyboard.index(s)
                s_out += keyboard[i - 1]
        else:
            print(s_out)
            s_out = ''
        s_in = input()
except EOFError:
    pass
