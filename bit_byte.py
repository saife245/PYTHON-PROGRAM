#bitis available for 2ms
#nibble is avilable for 8ms
#Byte is available for 16ms
#what is popuplition after n-ms
t = int(input())
for i in range(t):
        n = int(input())
    
        bit = 1
        nib = 0
        byt = 0
        while n > 0:
            if 0 <= n <= 2:
                bit = bit
                nib = 0
                byt = 0
                n = n-2

            elif 2< n <= 10:
                nib = bit
                bit = 0
                byt = 0
                n = n-10

            elif 10< n <= 26:
                byt = bit
                bit = 0
                nib = 0
                n = n-26

            else:
                bit = 2*(bit + byt)
                nib = 0
                byt = 0
                n = n-26

        print(bit, nib, byt)

