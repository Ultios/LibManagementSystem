

#MySqlConnector
import mysql.connector
from mysql.connector import Error
import pandas as pd
#Textwrap
import textwrap
#DateTime
import datetime

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: {err}")
    return connection
#Fungsi Inisialisasi
def Intro():
    return print(textwrap.dedent("""\
    ............LIBRARY MANAGEMENT............
        1. Pendaftaran User Baru
        2. Pendaftaran Buku Baru
        3. Peminjaman
        4. Tampilkan Daftar Buku
        5. Tampilkan Daftar User
        6. Tampilkan Daftar Peminjaman
        7. Cari Buku
        8. Pengembalian
        9. Exit
    """))

#Try except input dari user
def Input():
    while True:
        userchoice=input('Masukkan Nomor Tugas:')
        try:
            val=int(userchoice) 
            if val < 1 or val > 9:
                raise ValueError
            userchoice=val
            return userchoice;
        except ValueError:
            print("Input salah, mohon masukkan angka 1-9 sesuai tugas yang dikehendaki.")

def isINT(teks_prompt='Masukkan Input:'):
    #mengecek apakah input adalah Integer
    while True:
        userinput=input(teks_prompt)
        try:
            val=int(userinput)
            userinput=val
            return userinput;
        except ValueError:
            print("Input salah, mohon masukkan angka.")
def isDATE(teks_prompt='Masukkan tanggal dalam format YYYY-MM-DD:'):
    #Mengecek apakah input benar merupakan tanggal
    #Me return string yang sesuai dengan format query SQL
    while True:
        userinput=input(teks_prompt)
        try:
            year, month, day = map(int, userinput.split('-'))  #Memisahkan year month dan day
            try_date = datetime.date(year, month, day) #Cek apakah string input benar merupakan tanggal
            return userinput;
        except ValueError:
            print("Input salah, mohon masukkan tanggal dalam format YYYY-MM-DD.")

def read_query(connection, query,val=0):
    #mengeksekusi string query ke database
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query,val) #mengeksekusi query dan mengubah %s di query menjadi string dari variabel val
        result = cursor.fetchall()
        connection.commit()
        df = pd.DataFrame(result)
        return print(df.to_markdown())  #Markdown agar lebih terlihat bagus di terminal
    except Error as err:
        print(f"Error: {err}")

#1. Fungsi daftar user baru
def Add_user():
    #Menambahkan user baru ke tabel user di database SQL
    memberID=isINT('Masukkan member ID:')
    lastname=input('Masukkan nama terakhir:')
    firstname=input('Masukkan nama depan:')
    address=input('Masukkan alamat:')
    phone_number=isINT('Masukkan nomor telepon:')
    limit=10
    query='''
    INSERT INTO library.Member_ (memberID, lastname, firstname, address_, phone_number, limit_)
    VALUES (%s, %s, %s, %s, %s, %s);
    '''
    val=(memberID,lastname,firstname,address,phone_number,limit)
    return read_query(connection,query,val)

#2. Fungsi daftar buku baru
def Add_book():
    #menambahkan katalog buku baru ke database SQL
    BookID=isINT('Masukkan nomor buku:')
    ISBN=isINT('Masukkan nomor ISBN:')
    book_title=input('Masukkan nama buku:')
    book_author=input('Masukkan nama penulis:')
    publish_year=isINT('Masukkan tahun penerbitan:')
    book_category=input('Masukkan kategori buku:')
    query='''
    INSERT INTO library.Book (bookID,ISBN,title,Author,publish_year,category)
    VALUES (%s, %s, %s, %s, %s, %s);
    '''
    val=(BookID,ISBN,book_title,book_author,publish_year,book_category)
    return read_query(connection,query,val)

#3. Fungsi peminjaman
def Book_loan():
    #Mencatat peminjaman buku ke database SQL
    memberID=isINT('Masukkan member ID:')
    BookID=isINT('Masukkan nomor buku:')
    loan_date=isDATE('Masukkan tanggal peminjaman dalam format YYYY-MM-DD:')
    due_date=isDATE('Masukkan tanggal pengembalian dalam format YYYY-MM-DD:')
    query='''
    INSERT INTO library.CurrentLoan (memberID,bookID,loan_date,due_date)
    VALUES (%s, %s, %s, %s);
    '''
    val=(memberID,BookID,loan_date,due_date)
    return read_query(connection,query,val)

#4. Fungsi Tampilkan Daftar Buku
def View_book_list():
    #Menampilkan daftar buku
    query='''
    SELECT * FROM Book
    '''
    return read_query(connection,query)

#5. Fungsi tampilkan daftar user
def View_user_list():
    #Menampilkan daftar pengguna
    query='''
    SELECT * FROM Member_
    '''
    return read_query(connection,query)

#6. Fungsi tampilkan daftar peminjaman
def View_loan_list():
    #Menampilkan daftar peminjam
    query='''
    SELECT * FROM CurrentLoan
    '''
    return read_query(connection,query)

#7. Fungsi cari buku
def Find_book():
    #Mencari buku berdasarkan 4 kriteria:
    #Nomor, judul, pengarang dan tahun penerbitan buku
    print(textwrap.dedent("""\
        Cari Berdasarkan:
        1. Nomor Buku (Book ID)
        2. Judul Buku
        3. Pengarang
        4. Tahun penerbitan
    """))
    while True:
        userinput=input('Masukkan nomor filter pencarian:')
        functions={
                1:'bookID',
                2:'title',
                3:'Author',
                4:'publish_year'
            }
        try:
            userinput=int(userinput)

            find=functions[userinput]
            break
        except:
            print('Masukkan angka 1-4 sesuai pencarian yang diinginkan')
    keyword=input('Masukkan keyword yang ingin dicari:') 
    query='''
    SELECT bookID, 
    title,
    Author, 
    publish_year 
    FROM library.Book
    WHERE 
    '''
    query=query+find+"='"+str(keyword)+"';"
    val=(find,keyword)
    return read_query(connection,query)

#8. Fungsi pengembalian buku
def Return_book_loan():
    #Mendelete peminjaman dari daftar peminjaman
    val=isINT('Masukkan nomor anggota:')
    query="DELETE FROM library.CurrentLoan WHERE memberID='"+str(val)+"';"
    return read_query(connection,query)

#9. Fungsi keluar program
def Exit():
    print('Sampai jumpa!')
    return quit()


#Connect ke Databse
# definisi parameter
user = "lmsconn"
pw = "sobo123"
db = "library"

# koneksi ke database 'library'
connection = create_db_connection("localhost", user, pw, db)

#Dictionary untuk lookup fungsi-fungsi yang digunakan program
functions={
    1:Add_user,
    2:Add_book,
    3:Book_loan,
    4:View_book_list,
    5:View_user_list,
    6:View_loan_list,
    7:Find_book,
    8:Return_book_loan,
    9:Exit
}
#2.Pilih Program, infinite loop sampai user memilih exit.
while True:
    Intro()
    functions[Input()]()
