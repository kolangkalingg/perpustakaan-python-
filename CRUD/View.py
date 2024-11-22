from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data bro\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
              tahun = int(input("Tahun\t: "))
              if len(str(tahun)) == 4:
                  break
              else:
                  print("tahun lu kebanyakan kocakkkkkkk")
        except:
            print("tahun harus angka bos, silahkan isi ulang")
    Operasi.create(tahun,judul,penulis)
    print("\nData berhasil ditambahkan gg geming bos")
    print("\nBerikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header ini lek
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    #ini Data 
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    #kalo ini Footer
    print("="*100+"\n")