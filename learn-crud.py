import mysql.connector

class db_component:
  def __init__(self):
    self.host = "localhost"
    self.user = "root"
    self.password = ""
    self.db_name = "latihan_crud"
    self.tb_name = "mhs"
    self.createConnection()

    # connection method
  def createConnection(self):
    db = mysql.connector.connect(
      host = self.host,
      user = self.user,
      passwd = self.password,
      database = self.db_name
    )
    self.__db = db

  def insert_record(self):
    print("enter your name : ")
    name = input()

    print("enter your address : ")
    alamat = input()

    print("enter your number : ")
    no_mhs = input()

    cursor = self.__db.cursor()

    values = (name, alamat, no_mhs)
    # cursor.execute("INSERT INTO "+ self.tb_name+ "(name, alamat, no_mhs) VALUES (%s, %s, %s)", values)
    cursor.execute(""" insert into {} (name, alamat, no_mhs)
    values ('{}', '{}', {})
    """.format(self.tb_name, name, alamat, no_mhs))

    self.__db.commit()
    print(cursor.rowcount, "Record inserted.")

  def show_record(self):

    cursor = self.__db.cursor()
    # untuk mengambil koneksi database dan untuk error exception
    cursor.execute(""" select * from {}""".format(self.tb_name))
    # untuk menampilkan data dalam table dengan looping
    hasil = cursor.fetchall()
    for i in hasil:
      print(i)

  def update_record(self):
    self.show_record()
    
    print('Berdasarkan ID: ')
    id_mhs = input()

    print('Edit nama: ')
    name = input()
    if name is "":
      print("jika dikosongkan maka data akan terupdate dengan isi yang kosong")

    print('Edit alamat: ')
    alamat = input()
    if alamat is "":
      print("jika dikosongkan maka data akan terupdate dengan isi yang kosong")

    print('Edit NIM: ')
    no_mhs = input()
    if no_mhs is "":
      print("jika dikosongkan maka data akan terupdate dengan isi yang kosong")

    cursor = self.__db.cursor()

    cursor.execute(""" 
    update {} set name = '{}', 
    alamat = '{}', 
    no_mhs = {} 
    where id_mhs = {}""".format(self.tb_name, name, alamat, no_mhs, id_mhs))
    self.__db.commit()

    print(cursor.rowcount, "record update. ")

  def delete_record(self):
    self.show_record()

    print("deleted by ID : ")
    id_mhs = input()

    cursor = self.__db.cursor()

    cursor.execute("""delete from {} where id_mhs = {}""".format(self.tb_name, id_mhs))
    self.__db.commit()

    print(cursor.rowcount, "record deleted.")

hero = db_component()
hero.show_record()
# hero.delete_record()
# hero.update_record()
# hero.insert_record()