########CAPSTONE PROJECT I########
# Nama: Sendhi Anshari Rasyid    #
# Kelas: JCDSOL-012 (A)          #
##################################

# PROGRAM
# import library PrettyTable
from prettytable import *

# list data
list_buku=[['F01', 'Fiksi', 'One Piece', 'Eiichiro Oda', 90, 50000],
      ['N01', 'Non Fiksi', 'Atomic Habits', 'James Clear', 10, 110000],
      ['N02', 'Non Fiksi', 'Filosofi Teras', 'Henry Manampiring', 22, 90000],
      ['N03', 'Non Fiksi', "Don't Read This!", 'Prabu Pramayougha', 5, 150000],
      ['F02', 'Fiksi', 'Naruto', 'Masashi Kishimoto', 20, 40000]]

# header tabel
header_lengkap=['Index', 'Kode Buku', 'Jenis Buku', 'Judul Buku', 'Penulis', 'Stok', 'Harga']

# function table
def buat_tabel(data, headers):
    tabel_buku=PrettyTable(headers)
    tabel_buku.set_style(SINGLE_BORDER)
    tabel_buku.align['Harga']='r'
    tabel_buku.align['Judul Buku']='l'
    tabel_buku.align['Penulis']='l'
    for index, row in enumerate(data, start=1):
        tabel_buku.add_row([index] + row)
    return tabel_buku

def tabel_lengkap():
    tabel_hasil=buat_tabel(list_buku, header_lengkap)
    print(tabel_hasil)

# DAFTAR FUNCTION
# function 0: cek jumlah data
def jumlah_data():
    jumlah_data=len(list_buku)
    print(f'Jumlah data buku pada sistem sebanyak {jumlah_data} data.')

# function 1.1: lihat daftar buku
def daftar_buku_lengkap():
    if not list_buku:
        print('Saat ini data buku kosong. Silakan tambahkan data terlebih dulu untuk melihat daftar buku.')
    else:
        print(f'\nDaftar Data Buku\n---')
        tabel_lengkap()
        jumlah_data()

# function 1.2: lihat daftar buku pilihan
def daftar_buku_pilihan():
    while(True):
        try:
            if not list_buku:
                print('Data buku kosong. Silakan masukkan data buku terlebih dulu.')
                break
            else:
                jumlah_data()
                buku_pilihan=int(input(f'Masukkan index buku yang ingin Anda lihat data lengkapnya (1-{len(list_buku)}): '))-1
                if buku_pilihan >= 0 and buku_pilihan < len(list_buku):
                    print(f'\nBerikut adalah Data Buku untuk index {buku_pilihan+1}')
                    print(list_buku[buku_pilihan])
                    break
                elif buku_pilihan < 0 or buku_pilihan == 0:
                    print('Anda tidak bisa memasukkan index 0 atau negatif.')
                    break
                elif buku_pilihan >= len(list_buku):
                    print('Index yang Anda masukkan tidak terdapat pada sistem. Silakan pilih index yang tersedia.')
                    break
        except ValueError:
            print('Anda hanya bisa memasukkan index berupa angka.')
            break

# function 1.3: menu lihat daftar buku
def menu_lihat_buku():
    while(True):
        pilihan_menu=input('''\nMenu Lihat Buku\n---
1. Lihat Seluruh Data Buku
2. Lihat Data Buku Tertentu
3. Kembali ke Menu Utama\n
Masukkan angka menu yang dituju (1-3): ''')
        if(pilihan_menu == '1'):
            daftar_buku_lengkap()
        elif(pilihan_menu == '2'):
            daftar_buku_pilihan()
        elif(pilihan_menu == '3'):
            break
        else:
            print('Menu yang Anda pilih tidak ditemukan. Silakan pilih menu yang tersedia.')

# function cek data existing
def cek_data(list, input):
    for row in list:
        for element in row:
            if element == input:
                return True
    return False
   
# function 2: tambah_buku
# function 2.1: tambah buku
def tambah_buku():
    daftar_buku_lengkap()
    max_char = 3
    kode_buku_baru=input(f'\nMasukkan kode buku baru yang ingin Anda masukkan (maks. {max_char} karakter): ')
    kode_buku_upper=kode_buku_baru.upper()
    #print(kode_buku_upper)
    if len(kode_buku_upper) > max_char or len(kode_buku_upper) < max_char:
        print(f'Jumlah karakter yang Anda masukkan tidak sesuai. Kode Buku harus terdiri dari {max_char} karakter.')
    elif cek_data(list_buku, kode_buku_upper):
        print(f'Kode buku {kode_buku_upper} sudah ada pada sistem. Silakan masukkan kode buku lain.')
    else:
        jenis_buku_baru=input('Masukkan jenis buku baru yang ingin Anda masukkan (Fiksi/Non Fiksi): ')
        jenis_buku_title=jenis_buku_baru.title()
        #print(jenis_buku_title)
        if jenis_buku_title == 'Fiksi' or jenis_buku_title == 'Non Fiksi':
            judul_buku_baru=input('Masukkan judul buku baru yang ingin Anda masukkan: ')
            penulis_baru=input('Masukkan penulis buku baru yang ingin Anda masukkan: ')
            while(True):
                try:
                    stok_baru=int(input(f'Masukkan stok buku baru yang ingin Anda masukkan: '))
                    if stok_baru < 0 or stok_baru == 0:
                        print('Anda tidak bisa memasukkan angka 0 atau negatif.\n')
                    else:
                        break
                except ValueError:
                    print('Anda hanya bisa memasukkan stok berupa angka(integer).\n')
            while(True):
                try:
                    harga_baru=int(input(f'Masukkan harga buku baru yang ingin Anda masukkan: '))
                    if harga_baru < 0 or harga_baru == 0:
                        print('Anda tidak bisa memasukkan angka 0 atau negatif.\n')
                    else:
                        break
                except ValueError:
                    print('Anda hanya bisa memasukkan harga berupa angka(integer).\n')
                    break
            while(True):
                jawaban=(input(f'\nApakah data yang Anda masukkan sudah benar? (ya/tidak) '))
                jawaban_upper = jawaban.upper()
                if jawaban_upper == 'TIDAK':
                    break
                elif jawaban_upper == 'YA':
                    list_buku.append([kode_buku_upper, jenis_buku_title, judul_buku_baru, penulis_baru, stok_baru, harga_baru])
                    daftar_buku_lengkap()
                    print(f'Data buku baru dengan kode {kode_buku_upper} berhasil ditambahkan.')
                    # print(list_buku)
                    break
                else:
                    print(f'Opsi yang Anda masukkan tidak ditemukan, silakan masukan "ya" atau "tidak".')
                    break
        elif jenis_buku_title != 'Fiksi' or jenis_buku_title != 'Non Fiksi':
            print('Jenis buku yang Anda masukkan tidak terdapat pada sistem.')

# function 2.2: menu tambah buku
def menu_tambah_buku():
    while(True):
        pilihan_menu=input('''\nMenu Tambah Buku\n---
1. Tambah Data Buku
2. Kembali ke Menu Utama\n
Masukkan angka menu yang dituju (1-2): ''')
        if(pilihan_menu == '1'):
            tambah_buku()
        elif(pilihan_menu == '2'):
            break
        else:
            print('Menu yang Anda pilih tidak ditemukan. Silakan pilih menu yang tersedia.')

# function 3: ubah_buku
# function 3.1: ubah buku
def ubah_buku():
    while(True):
        try:
            if not list_buku:
                print('Data buku kosong. Silakan masukkan data buku terlebih dulu.')
                break
            elif list_buku:
                tabel_lengkap()
                buku_pilihan=int(input(f'Masukkan index buku yang ingin Anda ubah: '))-1
                #print(buku_pilihan)
                if buku_pilihan >= 0 and buku_pilihan < len(list_buku):
                    print(list_buku[buku_pilihan])
                    while(True):
                        jawaban=(input(f'\nApakah Anda ingin melanjutkan update? (ya/tidak) '))
                        jawaban_upper = jawaban.upper()
                        if jawaban_upper == 'TIDAK':
                            break
                        elif jawaban_upper == 'YA':
                            pilih_kolom=(input('Pilih nama kolom yang ingin Anda ubah datanya: '))
                            pilih_kolom_title=pilih_kolom.title()

                            # ganti kolom kode buku
                            if pilih_kolom_title == 'Kode Buku':
                                max_char = 3
                                ganti_kolom=(input(f'Masukkan Kode Buku baru (maks. {max_char} karakter): '))
                                ganti_kolom_kode=ganti_kolom.upper()
                                if len(ganti_kolom_kode) > max_char or len(ganti_kolom_kode) < max_char:
                                    print(f'Jumlah karakter yang Anda masukkan tidak sesuai. Kode Buku harus terdiri dari {max_char} karakter.')
                                elif cek_data(list_buku, ganti_kolom_kode):
                                    print(f'Kode buku {ganti_kolom_kode} sudah ada pada sistem. Silakan masukkan kode buku lain.')
                                else:
                                    jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][0]} dengan {ganti_kolom_kode}? (ya/tidak) ')
                                    jawaban2_upper=jawaban2.upper()
                                    if jawaban2_upper == 'TIDAK':
                                        break
                                    elif jawaban2_upper == 'YA':
                                        list_buku[buku_pilihan][0]=ganti_kolom_kode
                                        print(f'\nKode Buku telah berhasil diubah menjadi {ganti_kolom_kode}.')
                                        # print(list_buku[buku_pilihan])
                                        break
                                    else:
                                        print(f'Opsi yang Anda masukkan tidak ditemukan, silakan masukan "ya" atau "tidak".')
                                        break

                            # ganti kolom jenis buku                    
                            elif pilih_kolom_title == 'Jenis Buku':
                                ganti_kolom=input('Masukkan jenis buku baru (Fiksi/Non Fiksi): ')
                                ganti_kolom_jenis=ganti_kolom.title()
                                if ganti_kolom_jenis == 'Fiksi' or ganti_kolom_jenis == 'Non Fiksi':
                                    jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][1]} dengan {ganti_kolom_jenis}? (ya/tidak) ')
                                    jawaban2_upper=jawaban2.upper()
                                    if jawaban2_upper == 'TIDAK':
                                        break
                                    elif jawaban2_upper == 'YA':
                                        list_buku[buku_pilihan][1]=ganti_kolom_jenis
                                        print(f'\nJenis Buku berhasil diubah menjadi {ganti_kolom_jenis}.')
                                        break
                                elif ganti_kolom_jenis != 'Fiksi' or ganti_kolom_jenis != 'Non Fiksi':
                                    print('Jenis Buku yang Anda masukkan tidak terdapat pada sistem.')
                                    break

                            #ganti kolom judul buku
                            elif pilih_kolom_title == 'Judul Buku':
                                ganti_kolom=(input('Masukkan Judul Buku baru: '))
                                ganti_kolom_judul=ganti_kolom.title()
                                jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][2]} dengan {ganti_kolom_judul}? (ya/tidak) ')
                                jawaban2_upper=jawaban2.upper()
                                if jawaban2_upper == 'TIDAK':
                                    break
                                elif jawaban2_upper == 'YA':
                                    list_buku[buku_pilihan][2]=ganti_kolom_judul
                                print(f'\nJudul Buku telah berhasil diubah menjadi {ganti_kolom_judul}.')
                                break
                            
                            #ganti kolom penulis
                            elif pilih_kolom_title == 'Penulis':
                                ganti_kolom=(input('Masukkan nama Penulis baru: '))
                                ganti_kolom_penulis=ganti_kolom.title()
                                jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][3]} dengan {ganti_kolom_penulis}? (ya/tidak) ')
                                jawaban2_upper=jawaban2.upper()
                                if jawaban2_upper == 'TIDAK':
                                    break
                                elif jawaban2_upper == 'YA':
                                    list_buku[buku_pilihan][3]=ganti_kolom_penulis
                                print(f'\nPenulis telah berhasil diubah menjadi {ganti_kolom_penulis}')
                                break
                            
                            #ganti kolom stok
                            elif pilih_kolom_title == 'Stok':
                                while(True):
                                    try:
                                        ganti_stok=int(input(f'Masukkan jumlah Stok baru: '))
                                        if ganti_stok < 0 or ganti_stok == 0:
                                            print('Anda tidak bisa memasukkan angka 0 atau negatif.\n')
                                        else:
                                            jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][4]} dengan {ganti_stok}? (ya/tidak) ')
                                            jawaban2_upper=jawaban2.upper()
                                            if jawaban2_upper == 'TIDAK':
                                                break
                                            elif jawaban2_upper == 'YA':
                                                list_buku[buku_pilihan][4]=ganti_stok
                                                print(f'\nStok telah berhasil diubah menjadi {ganti_stok}')
                                                break
                                    except ValueError:
                                        print('Anda hanya bisa memasukkan stok berupa angka(integer).\n')

                            #ganti kolom harga
                            elif pilih_kolom_title == 'Harga':
                                while(True):
                                    try:
                                        ganti_harga=int(input(f'Masukkan Harga baru: '))
                                        if ganti_harga < 0 or ganti_harga == 0:
                                            print('Anda tidak bisa memasukkan angka 0 atau negatif.\n')
                                        else:
                                            jawaban2=input(f'Apakah Anda yakin ingin mengganti {list_buku[buku_pilihan][5]} dengan {ganti_harga}? (ya/tidak) ')
                                            jawaban2_upper=jawaban2.upper()
                                            if jawaban2_upper == 'TIDAK':
                                                break
                                            elif jawaban2_upper == 'YA':
                                                list_buku[buku_pilihan][5]=ganti_harga
                                                print(f'\nHarga telah berhasil diubah menjadi {ganti_harga}')
                                                break
                                    except ValueError:
                                        print('Anda hanya bisa memasukkan stok berupa angka(integer).\n')
                            else:
                                print(f'Opsi yang Anda masukkan tidak ditemukan.')
                            break
                        else:
                            break
                break
        except ValueError:
            print('Anda hanya bisa memasukkan index berupa angka.')
            break

# function 3.2: menu ubah buku
def menu_ubah_buku():
    while(True):
        pilihan_menu=input('''\nMenu Ubah Buku\n---
1. Ubah Data Buku
2. Kembali ke Menu Utama\n
Masukkan angka menu yang dituju: ''')
        if(pilihan_menu == '1'):
            ubah_buku()
        elif(pilihan_menu == '2'):
            break
        else:
            print('Menu yang Anda pilih tidak ditemukan. Silakan pilih menu yang tersedia.')

# function 4: hapus_buku
# function 4.1: hapus buku
def hapus_buku():
    while(True):
        try:
            if not list_buku:
                print('Data buku kosong. Silakan masukkan data buku terlebih dulu.')
                break
            else:
                tabel_lengkap()
                buku_pilihan=int(input(f'Masukkan index buku yang ingin Anda hapus (1-{len(list_buku)}): '))-1
                if buku_pilihan >= 0 and buku_pilihan < len(list_buku):
                    jawaban=(input(f'Apakah Anda yakin ingin menghapus index {buku_pilihan+1}? (ya/tidak) '))
                    jawaban_upper = jawaban.upper()
                    if jawaban_upper == 'TIDAK':
                        break
                    elif jawaban_upper == 'YA':
                        del list_buku[buku_pilihan]
                        print(f'\nAnda berhasil menghapus data dengan index {buku_pilihan+1}.\n---')
                        tabel_lengkap()
                        break
                    else:
                        print(f'Opsi yang Anda masukkan tidak ditemukan, silakan masukan "ya" atau "tidak".')
                        break
                elif buku_pilihan < 0 or buku_pilihan == 0:
                    print('Anda tidak bisa memasukkan index 0 atau negatif.')
                    break
                elif buku_pilihan >= len(list_buku):
                    print('Index yang Anda masukkan tidak terdapat pada sistem. Silakan pilih index yang tersedia.')
                    break
        except ValueError:
            print('Anda hanya bisa memasukkan index berupa angka.')
            break

# function 4.2: menu hapus buku
def menu_hapus_buku():
    while(True):
        pilihan_menu=input('''\nMenu Hapus Buku\n---
1. Hapus Data Buku
2. Kembali ke Menu Utama\n
Masukkan angka menu yang dituju: ''')
        if(pilihan_menu == '1'):
            hapus_buku()
        elif(pilihan_menu == '2'):
            break
        else:
            print('Menu yang Anda pilih tidak ditemukan. Silakan pilih menu yang tersedia.')

# function 5: keluar_program
def keluar_program():
    print('\nTerima kasih telah berkunjung ke Toko Buku Kineruku.\n')
    exit()

# function menu_utama
def menu_utama():
    pilihan_menu=input(f'''\nSelamat datang di Toko Buku Kineruku!\n
Daftar Menu:
1. Lihat Daftar Buku
2. Tambah Data Buku    
3. Ubah Data Buku
4. Hapus Data Buku
5. Keluar Program\n
Masukkan angka menu yang dituju (1-5): ''')
    if(pilihan_menu == '1'):
        menu_lihat_buku()
    elif(pilihan_menu == '2'):
        menu_tambah_buku()
    elif(pilihan_menu == '3'):
        menu_ubah_buku()
    elif(pilihan_menu == '4'):
        menu_hapus_buku()
    elif(pilihan_menu == '5'):
        keluar_program()
    else:
        print('''\nMenu yang Anda masukkan tidak ditemukan.\nSilakan masukkan angka menu yang tersedia.\n---''')

# menu utama
while(True):
    menu_utama()