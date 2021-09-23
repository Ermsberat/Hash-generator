import hashlib

print("""
this HASH GENERATOR was created by Berat

github.com/Ermsberat
""")



print("""
Lütfen Sifrelenecek Veriyi Giriniz

Please Enter the Data to be Encrypted

""")

data = input("Veri / Data: ")

print("""
Lütfen Sifreleme Türünü Giriniz

Please Enter Encryption Type

1)md5
2)sha224
3)sha256
4)sha384
5)sha512
6)blake2b
7)blake2s
""")

hashtype = input("Hash Türü / Encryption Type: ")

if hashtype == "1":
    veri=data
    sifrele=hashlib.md5()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "2":
    veri=data
    sifrele=hashlib.sha224()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "3":
    veri=data
    sifrele=hashlib.sha256()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "4":
    veri=data
    sifrele=hashlib.sha384()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "5":
    veri=data
    sifrele=hashlib.sha512()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "6":
    veri=data
    sifrele=hashlib.blake2b()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)

elif hashtype == "7":
    veri=data
    sifrele=hashlib.blake2s()
    sifrele.update(veri.encode("utf-8"))
    sonuc=sifrele.hexdigest()
    print(sonuc)
