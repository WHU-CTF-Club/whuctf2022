from Crypto.Util.number import long_to_bytes,bytes_to_long
import gmpy2


p= gmpy2.mpz(9291095464339049501122016215036801609076690409439759243805806156758162822504691051968625099221631819591773271234574111033316745132333558209010061036734597)
q= gmpy2.mpz(9291095464339049501122016215036801609076690409439759243805806156758162822504691051968625099221631819591773271234574111033316745132333558209010061036735209)
c= gmpy2.mpz(876851121104739345117962799998119485368108052039719404473681505579813906912557099779107544401004214323865342767020800198880192420241884018664173054643151880946855081934008483398143718911568949069289502351512585971656191386484150304636301682335868717006939018739786924440253701238064854859508067371680165173106392239035702426186453240943310691974525444557390896728322252549262394235149010305333125219770982791626540503491002034057898900114459843363048177972609921006802304480939700327021380491590424977039337077606210319253498656607890139663198043419378328751748202331325210284273742169487199361604236557824021310534)
n= gmpy2.mpz(86324454927461657860007410096336840120979839503674904701948712657586983855807988669560143211912037323769847108631053790908388282060017418955323734615211515597325512546062852172016400460654196227703541549912619998323486704517632234662974095606978779497089776947742868040584904963272448129397635067619098325773)
phi = (p-1)*(q-1)
u = gmpy2.invert(phi,n)

def L(x):
	return (x-1)//n

b = gmpy2.powmod(c,phi,n*n)

m = (L(b)*u) % n
flag = long_to_bytes(m)

print(flag)
