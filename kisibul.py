import webbrowser
import os
import time
os.system("color b")
os.system("cls")
print(""" 
                                                                                                   
KKKKKKKKK    KKKKKKK  iiii                     iiii  BBBBBBBBBBBBBBBBB                     lllllll 
K:::::::K    K:::::K i::::i                   i::::i B::::::::::::::::B                    l:::::l 
K:::::::K    K:::::K  iiii                     iiii  B::::::BBBBBB:::::B                   l:::::l 
K:::::::K   K::::::K                                 BB:::::B     B:::::B                  l:::::l 
KK::::::K  K:::::KKKiiiiiii     ssssssssss   iiiiiii   B::::B     B:::::Buuuuuu    uuuuuu   l::::l 
  K:::::K K:::::K   i:::::i   ss::::::::::s  i:::::i   B::::B     B:::::Bu::::u    u::::u   l::::l 
  K::::::K:::::K     i::::i ss:::::::::::::s  i::::i   B::::BBBBBB:::::B u::::u    u::::u   l::::l 
  K:::::::::::K      i::::i s::::::ssss:::::s i::::i   B:::::::::::::BB  u::::u    u::::u   l::::l 
  K:::::::::::K      i::::i  s:::::s  ssssss  i::::i   B::::BBBBBB:::::B u::::u    u::::u   l::::l 
  K::::::K:::::K     i::::i    s::::::s       i::::i   B::::B     B:::::Bu::::u    u::::u   l::::l 
  K:::::K K:::::K    i::::i       s::::::s    i::::i   B::::B     B:::::Bu::::u    u::::u   l::::l 
KK::::::K  K:::::KKK i::::i ssssss   s:::::s  i::::i   B::::B     B:::::Bu:::::uuuu:::::u   l::::l 
K:::::::K   K::::::Ki::::::is:::::ssss::::::si::::::iBB:::::BBBBBB::::::Bu:::::::::::::::uul::::::l
K:::::::K    K:::::Ki::::::is::::::::::::::s i::::::iB:::::::::::::::::B  u:::::::::::::::ul::::::l
K:::::::K    K:::::Ki::::::i s:::::::::::ss  i::::::iB::::::::::::::::B    uu::::::::uu:::ul::::::l
KKKKKKKKK    KKKKKKKiiiiiiii  sssssssssss    iiiiiiiiBBBBBBBBBBBBBBBBB       uuuuuuuu  uuuullllllll

by @alismsk234


""")

KisiDetayi = input("Kişinin adını ve soyadını yazın>> ")
KisiDetayiF = input("Kişinin hakkında daha detaylı bilgi var mı?(E-H) ")
if KisiDetayiF == "E" or KisiDetayiF == "e":
    fkisi = input("Nereli (Plaka no olabilir)>> ")
    kisif = input("Kullandığı bir kullanıcı adı>> ")
    urlD = "www.google.com/search?q="+KisiDetayi+" "+fkisi
    webbrowser.open(urlD)
    time.sleep(3)
    urlDTY = "www.google.com/search?q="+kisif
    webbrowser.open(urlDTY)
    time.sleep(3)
    FurlF = "https://tr-tr.facebook.com/public/"+KisiDetayi+" "+fkisi
    webbrowser.open(FurlF)
    time.sleep(3)
    urlTT = "https://twitter.com/search?q="+KisiDetayi+" "+fkisi+"&src=typed_query&f=user"
    webbrowser.open(urlTT)
    time.sleep(3)
    urlG = "https://groups.google.com/search?q="+KisiDetayi
    webbrowser.open(urlG)
    time.sleep(3)
    urlPP = "https://www.peekyou.com/"+KisiDetayi
    webbrowser.open(urlPP)
elif KisiDetayiF == "h" or KisiDetayiF == "H":
    print("Daha fazla detay bulmanız daha yararlı olur.")
    urlF = "https://tr-tr.facebook.com/public/"+KisiDetayi
    urlT = "https://twitter.com/search?q="+KisiDetayi+"&src=typed_query&f=user"

    webbrowser.open(urlF)
    time.sleep(4)
    webbrowser.open(urlT)
else:
    print("Hatalı Giriş!")

