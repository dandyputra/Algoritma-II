import random #ramdomangka#

print ("Selamat datang di aplikasi Jodoh Meter")
print ("1. cek berdasarkan nama")
print ("2. cek berdasarkan pekerjaan")
print ("3. cek berdasarkan hoby")
answer = input ("Inputkan yang di pilih : ")

if answer == '1':
    loop = True
    while loop:
        pria = input("Masukkan nama Pria : ")
        wanita= input("Masukkan nama Wanita : ")

        print ("==================================")
        print ("Nama Pria : ", pria)
        print ("Nama Wanita :", wanita )

        confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n : ")

        if confirm == "y" :
          loop = False

        match = random.randrange(0,100)

        print("")
        print("MATCH METER", match,"%")
        print("")

        if match > 80 :
          print ("Ndang Rabi")
        else :
          if match > 60 :
            print ("Pikir-Pikir")
          else : 
              if match > 40 :
                print ("Yaaakinn...!")
              else :
                  if match > 20 :
                    print ("cari lagi")
                  else :
                    print ("putus aja")

if answer == '2':
    loop = True
    while loop:
      pekerjaan = input ("Masukkan Pekerjaan Pria : ")
      pekerjaanW = input ("Masukkan Pekerjaan Wanita : ")

      print ("============================")
      print ("Pekerjaan Pria : ",pekerjaan)
      print ("Pekerjaan Wanita : ",pekerjaanW)

      confirm = input ("Apakah pekerjaan yang di masukkan sudah benar? y/n : ")

      if confirm == "y" :
        loop = False

    match = random.randrange(0,100)

    print ("")
    print ("MATCH METER", match,"%")
    print ("")

    if match > 80:
      print ("anda dan pasangan cocok dalam cinta dan karir")
    else :
      if match > 60:
        print ("pikirkan baik baik sebelum bertindak selanjutnya")
      else :
        if match > 40:
          print ("anda dan pasangan belum cocok")
        else :
          if match > 20:
            print ("cari pasangan lain")
          else :
            print ("maaf kurang beruntung")

if answer == '3':
    loop = True
    while loop:
        hobyP = input ("Masukkan Hoby Pria : ")
        hobbyW = input ("Masukkan Hobby Wanita : ")

        print ("=======================")
        print ("Hobby pria : ",hobyP)
        print ("Hobby Wanita : ",hobbyW)

        confirm = input ("Apakah Hobby yang di masukkan sudah benar? y/n : ")

        if confirm == "y":
            loop = False

    match = random.randrange(0,100)

    print ("")
    print ("MATCH METER", match,"%")
    print ("")

    if match > 80:
      print ("Hobby anda dan pasagan sama")
    else :
      if match > 60:
        print ("Sedikit berbeda dengan pasangan anda")
      else :
        if match > 40:
          print ("Banyak perbedaan hobby antara anda dan pasangan")
        else :
          if match > 20:
            print ("cari pasangan lain")
          else :
            print ("maaf kurang beruntung")



        
