import mysql.connector


def main() :
    check = True
    while(check):
      print(">>>> Selamat Datang di Movie List Python <<<<")
      print("1. Daftar Film")
      print("2. Keluar")
      chooseMenu(check)
      enter_app = input("Ingin Keluar ? Yes/No : ")
      if(enter_app == 'yes'):
            check = False
      else:
            check = True
    print("Terima kasih")

def chooseMenu(check) :
    pilih = input("Pilih : ")
    if(int(pilih) == 1):
      print("berikut adalah daftar film")
      seefilm()
    if(int(pilih) == 2):
      check = False

def seefilm() :
    db = database()
    cursor = db.cursor()
    seeAll = "SELECT movie_id,name FROM movies"
    cursor.execute(seeAll)

    movies = cursor.fetchall()
    for movie in movies:
          print('{}.{}'.format(movie[0],movie[1]))


def database() :
    db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="movie_list"
    )
    # cursor = db.cursor()

    return db
    # cursor = db.cursor()
    # insert = "INSERT INTO movies (name,genre) VALUES (%s,%s)"
    # values = [
    #   ("Avengers End Game","Adventure, Action"),
    #   ("Harry Potter", "Fantasy,Action")
    # ]
    # for value in values:
    #     cursor.execute(insert, value)
    #     db.commit()
    # print("{} data ditambahkan".format(len(values)))

main()
# database()