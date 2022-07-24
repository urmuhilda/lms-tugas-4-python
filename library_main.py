import mysql.connector
from datetime import date

def daftar_user():
    ''' 
    Fungsi ini ditujukan untuk meminta data user baru 
    dan memasukkannya ke dalam tabel daftar_user di MySQL
    '''
    conn = mysql.connector.connect(
      host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()

    input_nama = input("Masukkan nama anda: ")
    input_pekerjaan = input("Pekerjaan: ")
    input_email = input("Masukkan email anda: ")
  
 
    sql = 'insert into data_user(nama_user,pekerjaan_user,email_user) values ("' + \
      input_nama + '","' + input_pekerjaan+'","'+input_email+'");'
    
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nUser berhasil ditambahkan')


def daftar_buku():
    ''' 
    Fungsi ini ditujukan untuk menambahkan data buku baru 
    dan memasukkannya ke dalam tabel daftar_buku di MySQL
    '''
    conn = mysql.connector.connect(
       host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()
    
    input_judul = input("Judul: ")
    input_kategori = input("Kategori: ")
    input_stok = int(input("Stock: "))
    sql = 'insert into data_buku(judul_buku,kategori_buku,stock_buku) values ( "' + \
    input_judul + '","' + input_kategori+'","' + str(input_stok)+'");'
    
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nBuku berhasil ditambahkan')


def peminjaman_buku():
    ''' 
    Fungsi ini ditujukan untuk membuat data peminjaman baru 
    dan memasukkannya ke dalam tabel data_peminjaman di MySQL
    '''
    conn = mysql.connector.connect(
    host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()
    
    input_id_buku = int(input("Masukkan id buku yang dipinjam: "))
    input_id_peminjam = int(input("Masukkan id user: "))
    tanggal_peminjaman = date.today()
    
    sql = 'insert into data_peminjaman(idbuku,iduser,tanggal_peminjaman) values ( "' + \
    str(input_id_buku) + '","' + str(input_id_peminjam)+'","' + str(tanggal_peminjaman)+'");'
                                                          
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nBuku berhasil dipinjam')
    

def tampilkan_data_buku():
    ''' Fungsi ini ditujukan untuk menampilkan seluruh data buku '''
    conn = mysql.connector.connect(
        host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()

    print('\n MENAMPILKAN DATA BUKU ')
    
    sql = 'select * from data_buku'
    
    cursor.execute(sql)
    
    hasil_data_buku = cursor.fetchall()
    for data_buku in hasil_data_buku:
       print(data_buku)
    conn.close()

def tampilkan_data_user():
    ''' Fungsi ini ditujukan untuk menampilkan seluruh data user '''
    conn = mysql.connector.connect(
        host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()

    print('\n MENAMPILKAN DATA USER ')
    
    sql = 'select * from data_user'
    
    cursor.execute(sql)
    hasil_data_user = cursor.fetchall()
    for user in hasil_data_user:
       print(user)
    conn.close()


def cari_buku():
    ''' Fungsi ini adalah fungsi untuk melakukan pencarian buku berdasarkan judul buku '''
    conn = mysql.connector.connect(
        host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()

    print('\n PENCARIAN BUKU ')
    input_judul = input('Masukkan judul buku: ')
    
    sql ='select * from data_buku where '+ "judul_buku" + ' like "%'+ input_judul+'%"'
    
    cursor.execute(sql)
    hasil_pencarian_buku = cursor.fetchall()

    print('Hasil pencarian',"judul buku",' :' ,input_judul)
    for pencarian_buku in hasil_pencarian_buku:
      print(pencarian_buku)
    conn.close()
    
def pengembalian_buku():
    ''' 
    Fungsi ini ditujukan untuk membuat data pengembalian buku 
    dan memasukkannya ke dalam tabel daftar_peminjaman di MySQL
    '''
    conn = mysql.connector.connect(
    host='localhost', database='library_project', user='root', password='urmuhil8a')
    cursor = conn.cursor()
    
    input_id_buku = int(input("Masukkan id buku yang dipinjam: "))
    input_id_peminjam = int(input("Masukkan id user: "))
    tanggal_pengembalian = date.today()
    
    sql = 'insert into data_peminjaman(idbuku,iduser,tanggal_peminjaman) values ( "' + \
    str(input_id_buku) + '","' + str(input_id_peminjam)+'","' + str(tanggal_pengembalian)+'");'
    
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nBuku berhasil dikembalikan')
    

finished = False

''' Program untuk menampilkan menu Library Management System sederhana '''

while not finished:
    library_menu = """
    ...LIBRARY MENU...
    1. Pendaftaran User Baru
    2. Pendaftaran Buku Baru
    3. Peminjaman
    4. Tampilkan Daftar Buku
    5. Tampilkan Daftar User
    6. Cari Buku
    7. Pengembalian
    8. Keluar
    """
    print(library_menu)

    pilihan = int(input("Masukkan pilihan anda: "))
    
    if pilihan == 1:
        daftar_user()
    elif pilihan == 2:
        daftar_buku()
    elif pilihan == 3:
        peminjaman_buku()
    elif pilihan == 4:
        tampilkan_data_buku()
    elif pilihan == 5:
        tampilkan_data_user()
    elif pilihan == 6:
        cari_buku()
    elif pilihan == 7:
        pengembalian_buku()
    else:
        break
    
    print("Terima kasih sudah mengunjungi Library Management System")

    is_finished = input("Apakah Anda ingin keluar? (Y/N)")
    if is_finished == 'Y':
        finished = True