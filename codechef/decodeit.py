def binaryToDecimal(s):
    return (8 * int(s[0]) + 4 * int(s[1]) + 2 * int(s[2]) + 1 * int(s[3]))

def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        s=input()
        m=n//4
        out = ""
        if n>4:
            for _ in range(m):
                temp = s[-4:]
                s = s[0:-4]
                bin1=binaryToDecimal(temp)
                out1=chr(int(bin1)+97)
                out = out1+out
            print(out)
        else:
            binary=binaryToDecimal(s)
            out=chr(int(binary)+97)
            print(out)
    return 0
main()