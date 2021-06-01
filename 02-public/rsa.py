#python3 rsa.py -p rsa_plain.txt
import random
import argparse
def main():
        p = BigPrime()
        q = BigPrime()
        n = p*q
        _n = (p-1)*(q-1)
        e = 0
        while(1):
                e = random.randint(1,_n+1)
                if gcd(e,_n)==1:
                        break
        d = Ex_Euclid(e,_n)
        print('p=',str(hex(p))[2:])
        print('q=',str(hex(q))[2:])
        print('n=',str(hex(n))[2:])
        print('e=',str(hex(e))[2:])
        print('d=',str(hex(d))[2:])

        print("public key:","\n","n=",str(hex(n))[2:],"\n","e=",str(hex(e))[2:])
        print("private key:","\n","n=",str(hex(n))[2:],"\n","d=",str(hex(d))[2:])

        parser = argparse.ArgumentParser(description="This is a description, it includes the whole file's loactions of RSA algorithm.")
        parser.add_argument('-p', required = True, type = argparse.FileType('r'), help = 'plainfile')
        args = parser.parse_args() 
        m = args.p.read()
        #加密与签名
        if m=='':
            print('plaintext not found')
        else:
            print('plaintext=',m)
            cipher = encrypt(m,e,n)
            print("cipher:",cipher)
            sign = encrypt(m,d,n)
            print("sign:",sign)
            plain = decrypt(cipher,d,n)
            print("decrypt:",plain)
 
#平方—乘法算法
def MRF(b,n,m):
    
        a=1
        x=b;y=n;z=m
        binstr = bin(n)[2:][::-1]	#通过切片去掉开头的0b，截取后面，然后反转
        for item in binstr:
                if item == '1':
                        a = (a*b)%m
                        b = (b**2)%m
                elif item == '0':
                        b = (b**2)%m
        return a

def MillerRabin(n):
    m=n-1
    k=0
    while(m%2==0):
        m=m//2
        k=k+1
    a=random.randint(2,n)
    #b=a**m%n
    b = MRF(a,m,n)
    if(b==1):
        return 1
    for i in range(k):
        if(b==n-1):
            return 1
        else:
            b=b*b%n
    return 0

def BigPrime():
        Min = 10**11;Max = 10**15;p = 0
        while(1):
                p = random.randrange(Min,Max,1)
                for i in range(20):
                        if MillerRabin(p)==0:
                                break
                        elif i==19:
                                return p
                                
#加密，传入公钥，通过读取明文文件进行加密
def encrypt(m,e,n):
        cipher = ""
        nlength = len(str(hex(n))[2:])  #计算n的16进制长度，以便分组
        message = m             #读取明文
        for i in range(0,len(message),8):
            if i==len(message)//8*8:
                m = int(a2hex(message[i:]),16)  #最后一个分组
            m = int(a2hex(message[i:i+8]),16)
            c = MRF(m,e,n)
            cipher1 = str(hex(c))[2:]
            if len(cipher1)!=nlength:
                cipher1 = '0'*(nlength-len(cipher1))+cipher1    #每一个密文分组，长度不够，高位补0
            cipher += cipher1
        return cipher
#解密,传入私钥，通过文件读写进行解密
def decrypt(c,d,n):
        #加密之后每一个分组的长度和n的长度相同
        cipher = c
        message = ""
        nlength = len(str(hex(n))[2:])
        for i in range(0,len(cipher),nlength):
            c = int(cipher[i:i+nlength],16)     #得到一组密文的c
            m = MRF(c,d,n)
            info = hex2a(str(hex(m))[2:])
            message += info
        return message
 
#求最大公因子
def gcd(a,b):  
        if a%b == 0:
                return b
        else :
                return gcd(b,a%b)
 
#求逆元
def Ex_Euclid(x,n):
    r0=n
    r1=x%n
    if r1==1:
        y=1
    else:
        s0=1
        s1=0
        t0=0
        t1=1
        while (r0%r1!=0):
            q=r0//r1  
            r=r0%r1  
            r0=r1  
            r1=r  
            s=s0-q*s1 
            s0=s1 
            s1=s  
            t=t0-q*t1  
            t0=t1  
            t1=t  
            if r==1:
                y = (t+n)%n
    return y
 
def a2hex(raw_str):
        hex_str = ''
        for ch in raw_str:
                hex_str += hex(ord(ch))[2:]
        return hex_str

def hex2a(raw_str):
        asc_str = ''
        for i in range(0,len(raw_str),2):
                asc_str += chr(int(raw_str[i:i+2],16))
        return asc_str

if __name__ == "__main__":
        main()