#Luhn Algorithm

myString = input('Enter 16 digit card number: ')

index_nums = myString
odd_nums = index_nums
a = (index_nums[15])
int_a = int(a)
b = (index_nums[13])
int_b = int(b)
c = (index_nums[11])
int_c = int(c)
d = (index_nums[9])
int_d = int(d)
e = (index_nums[7])
int_e = int(e)
f = (index_nums[5])
int_f = int(f)
g = (index_nums[3])
int_g = int(g)
h = (index_nums[1])
int_h = int(h)

odd_sum = int_a + int_b + int_c + int_d + int_e + int_f + int_g + int_h

index_nums = myString
even_nums = index_nums
i = (index_nums[14])
int_i = int(i)
di = int_i * 2
if di < 10:
    result = di
else:
    sdi = str(di)
    isdi = sdi[0]
    int_isdi = int(isdi)
    iisdi = sdi[1]
    int_iisdi = int(iisdi)
    result_14 = int_isdi + int_iisdi
    
j = (index_nums[12])
int_j = int(j)
dj = int_j * 2
if dj < 10:
    result_12 = dj
else:
    sdj = str(dj)
    isdj = sdj[0]
    int_isdj = int(isdj)
    iisdj = sdj[1]
    int_iisdj = int(iisdj)
    result_12 = int_isdj + int_iisdj
    
k = (index_nums[10])
int_k = int(k)
dk = int_k * 2
if dk < 10:
    result_10 = dk
else:
    sdk = str(dk)
    isdk = sdk[0]
    int_isdk = int(isdk)
    iisdk = sdk[1]
    int_iisdk = int(iisdk)
    result_10 = int_isdk + int_iisdk

l = (index_nums[8])
int_l = int(l)
dl = int_l * 2
if dl < 10:
    result_8 = dl
else:
    sdl = str(dl)
    isdl = sdi[0]
    int_isdl = int(isdl)
    iisdl = sdl[1]
    int_iisdl = int(iisdl)
    result_8 = int_isdl + int_iisdl

m = (index_nums[6])
int_m = int(m)
dm = int_m * 2
if dm < 10:
    result_6 = dm
else:
    sdm = str(dm)
    isdm = sdm[0]
    int_isdm = int(isdm)
    iisdm = sdm[1]
    int_iisdm = int(iisdm)
    result_6 = int_isdm + int_iisdm

n = (index_nums[4])
int_n = int(n)
dn = int_n * 2
if dn < 10:
    result_4 = dn
else:
    sdn = str(dn)
    isdn = sdn[0]
    int_isdn = int(isdn)
    iisdn = sdn[1]
    int_iisdn = int(iisdn)
    result_4 = int_isdn + int_iisdn

o = (index_nums[2])
int_o = int(o)
do = int_o * 2
if do < 10:
    result_2 = do
else:
    sdo = str(do)
    isdo = sdo[0]
    int_isdo = int(isdo)
    iisdo = sdo[1]
    int_iisdo = int(iisdo)
    result_2 = int_isdo + int_iisdo

p = (index_nums[0])
int_p = int(p)
dp = int_p * 2
if dp < 10:
    result_0 = dp
else:
    sdp = str(dp)
    isdp = sdp[0]
    int_isdp = int(isdp)
    iisdp = sdp[1]
    int_iisdp = int(iisdp)
    result_0 = int_isdp + int_iisdp

even_sum = result_14 + result_12 + result_10 + result_8 + result_6 + result_4 + result_2 + result_0

final_sum = odd_sum + even_sum
if final_sum % 10 == 0:
    print ('Valid Card')
else:
    print('Invalid Card')
