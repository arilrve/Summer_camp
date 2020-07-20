from Crypto.Util.number import *
n = 83092583783534841000145280642003842283533340442637642451258941907393275732996256523893438356692786223410880194199043046345864683398238392329295750150314289824255749149834103
e = 11
c =32392151763267291269610586564983347951891395196084251182633225594245167922176424232164117237142038355860036871811244158149537196288428230971760474130300660929743492107190512
p1 = 2262150366
p2 = 3006300460
p3 = 12218233223644524650141958853163065112163255395621655741865064529020634406575730714768264558014607893896434523845321502371618344594488810317052606914954669
phi = p1*p2*(p3-1)
d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))
