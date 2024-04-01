'''
14S21034 Stefen Parlindungan Sinaga
14S21035 Efraim Asidovanio Butarbutar
'''
class Film:
    def __init__(self, judul, genre, durasi, tahun, jumlah_tiket_tersedia):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi
        self.tahun = tahun
        self.jumlah_tiket_tersedia = jumlah_tiket_tersedia
    
    # Fungsi untuk mengemballikan informasi yang mengacu pada string yang berisi atas informasi objek Film
    def get_info(self):
        return f"Judul: {self.judul}, Genre: {self.genre}, Durasi: {self.durasi}, Tahun rilis: {self.tahun}, Jumlah tiket tersedia: {self.jumlah_tiket_tersedia} "
    
    # Fungsi untuk menampilkan informasi objek Film pada films
    def tampilkan_film(films):
        for film in films:
            print(film.get_info())

class Bioskop:
    def __init__(self, nama, alamat, telepon):
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.films = [] # list kosong untuk menyimpan objek Film
        self.pemesanan_tiket = [] # list kosong untuk menyimpan objek PemesananTiket
    
    # Fungsi untuk mengembalikan informasi atas objek Bioskop dengan nomor Index
    def get_info(self, index):
        return f'[{index}] {self.nama}'
    
    # Fungsi menambahkan film terhadap list kosong 
    def add_film(self, film):
        self.films.append(film)
    
    # Fungsi mencari film berdasarkan letak sesuai Index terhadap judul film pada variabel films
    def find_film(self, film):
        index = -1 # inisialisasi variabel index
        for f in self.films:
            index += 1 
            if f.judul == film.judul: # memeriksa judul apakah telah sesuai
                return index
        return -1

    # Fungsi menambahkan pemesanan tiket ke dalam daftar pemesanan tiket bioskop
    def add_pemesanan_tiket(self, pemesanan):
        index_file = self.find_film(pemesanan.film) # mencari index film dalam daftar films dari objek pemesanan tiket
        if index_file >= 0:
            if self.films[index_file].jumlah_tiket_tersedia >= pemesanan.jumlah_tiket_dipesan:
                self.films[index_file].jumlah_tiket_tersedia -= pemesanan.jumlah_tiket_dipesan
                self.pemesanan_tiket.append(pemesanan)
                print("Tiket sudah dibeli.")
            else:
                print("Maaf, tiket tidak tersedia.")
        else:
            print("Film tidak ditemukan")
            
    def tampilkan_pemesanan(self):
        print("Tiket yang sudah dipesan: ")
        for pemesanan in self.pemesanan_tiket:
            pemesanan.tampilkan_info()

    # Fungsi untuk mencetak daftar film yang tersedia pada bioskop
    def show_all_film(self):
        print("Film yang tersedia:")
        for f in self.films:
            print(f.get_info())
    
class PemesananTiket:
    def __init__(self, film, pembeli, jumlah_tiket_dipesan):
        self.film = film
        self.pembeli = pembeli
        self.jumlah_tiket_dipesan = jumlah_tiket_dipesan

    # Fungsi untuk mencetak informasi atas tiket yang sudah dipesan
    def tampilkan_info(self):
        print("Informasi Tiket")
        print("===============")
        print("Film: ", self.film.judul)
        print("Genre: ", self.film.genre)
        print("Durasi: ", self.film.durasi)
        print("Jumlah Tiket Dipesan: ", self.jumlah_tiket_dipesan)

# main program
films_1 = [
    Film("Film A", "Aksi", "120 menit", 2003, 5),
    Film("Film B", "Komedi", "100 menit", 2022, 3),

]

films_2 = [
    Film("Film C", "Animasi", "110 menit", 2006, 10),
    Film("Film D", "Horror", "130 menit", 2012, 7)
]

bioskops = [
    Bioskop("Bioskop A", "Jalan Tangerang", "081275140623"),
    Bioskop("Bioskop B", "Jalan Jakarta", "081120140623"),
]

for f in films_1:
    bioskops[0].add_film(f)

for f in films_2:
    bioskops[1].add_film(f)

while True:
    print("=== Aplikasi Pemesanan Tiket Bioskop ===")
    print("1. Lihat Daftar Bioskop")
    print("2. Lihat Daftar Film")
    print("3. Pesan Tiket")
    print("4. Lihat Pemesanan")
    print("5. Keluar")

    pilihan = input("Masukkan Pilihan Anda: ")

    if pilihan == "1":
        index = 1 # inisialisasi variabel index
        for b in bioskops:
            print(b.get_info(index))
            index +=1 # urutan bioskop

    elif pilihan == "2":
        print("==========================================")
        bioskop = int(input("Masukkan nomor bioskop: "))
        Film.tampilkan_film(bioskops[bioskop - 1].films) # menampilkan daftar film terhadap bioskop yang dipilih
        # mengakskes atribut films untuk mmendapatkan daftar film

    elif pilihan == "3":
        print("==========================================")
        bioskop = int(input("Masukkan nomor bioskop: "))
        Film.tampilkan_film(bioskops[bioskop - 1].films)

        print("Pesan Tiket Anda")
        pembeli = input("Masukkan nama pembeli: ")
        if pembeli.strip() == "":
            print("Nama pembeli harus diisi.")
        else:
            judul_film = input("Masukkan judul film yang ingin ditonton: ")
            film_ditemukan = False
            for film in bioskops[bioskop - 1].films:
                if film.judul == judul_film:
                    film_ditemukan = True
                    jumlah_tiket = int(input("Masukkan jumlah tiket yang dipesan: "))
                    pemesanan = PemesananTiket(film, pembeli, jumlah_tiket)
                    bioskops[bioskop - 1].add_pemesanan_tiket(pemesanan)
                    break
            if not film_ditemukan:
                print("Judul film tidak ditemukan.")
    
    elif pilihan == "4":
        print("==========================================")
        bioskop = int(input("Masukkan nomor bioskop: "))
        bioskops[bioskop - 1].tampilkan_pemesanan()
    
    elif pilihan == "5":
        print("Terimakasih telah menggunakan aplikasi kami.")
        break

    else: 
        print("Pilihan tidak valid.")