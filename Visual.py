import os, time, util_function


Manajerial = [
"                                                    @@@@@@                         ",
"                              ,       %@@@@@@#      @@   @%                        ",
"               /*#      @@@@ (@@       @@   @@      %@&  @@@@@@@@@@                ",
"           @@@/  @@     @@@   @@       @@@  /@@@@@@@@@@   @@     @@@               ",
"           #@@   @@      @@.   @@@@@@@@@@@   @@      @@@  @@&    ,@@*              ",
"            @@,   @@@@@@@@@@   @@*      @@@@@@@&                  @@@              ",
"    *@@@@@@@@@@   @@(     @@@@@@@@                                 @@@             ",
"   @@@.         \@@  @@@@                                          @@@@%           ",
"   @@@@                                                              @@@           ",
"   &@@@                                                               @@@          ",
"    @@@,                                                              #@@@@        ",
"    @@@@                  @@                         &@@@@@@@@        //@@&        ",
"    #@@@                   \             *@@@@@@@@@@@%                  @@@@       ",
"     @@@@          @@@@@@\\\    @@@@@@@@@@.                               @@.       ",
"     @@@@          \\\ \\\\&                                                @@@@      ",
"     *@@@,         @@ \\\@@@                                               @@@      ",
"      @@@@                    \                             /@@@@/        @@@      ",
"      @@@@                  \\                ,@@@@@@@@@@/                 @@@      ",
"      .@@@@         @@@@@@@\\\     *@@@@@@@@@@,                            @@@@     ",
"       @@@@         \\\  \\\@/                                             #@@@      ",
"       @@@@@         @@\\\@@@@                                            @@@@@     ",
"        @@@@                   \                      #@@@@@@@@@.        %@@@#     ",
"        @@@@@              .%\\            @@@@@@@@@@.          .        (@@/@@.    ",
"        &@@@@@        @@@@&\\\@     @@@@@@                   @@  @@@     &@@@@@     ",
"         @@@@@        \\\  \\@@                                           \#%@@      ",
"         @@@@@@        @\\\\@@#                                          %#@@        ",
"          @@@@@@                                                     .@@@@         ",
"          @@ &@@@@/                                       (@@@@@@@@(               ",
"           @@    @@@@@@@,,..                  .&@@@@@@@@%                          ",
"           *@@              ``,,//@@@@@@@@@@.//                                    ",
"             @@@@@@@@@@@@@@@@@*                                                    ",
"",
"",
'Selamat datang di program “Manajerial Candi”',
'Silahkan masukkan username Anda!']



'''------------------------------------------------------------ Print Animasi ------------------------------------------------------------'''

'''-------------------- Get Window Size --------------------'''
def window_size():
    # get size of the current terminal
    size = os.get_terminal_size()
    # set window width from terminal size
    window_width = size.columns
    # set initial window height from terminal size
    window_height = size.lines
    # we set five line in the bottom for the input, so modified window_height
    number_of_lines_for_input = 5
    window_height -= number_of_lines_for_input # (it is the same as window_height = window_height - number_of_lines_for_input)
    # return the function with dictionary data
    return [window_width, window_height]
'''-------------------- Get Window Size --------------------'''


'''-------------------- Render Screen --------------------'''
def render_screen(ascii: list, height_of_ascii: int):
    
    os.system("cls||clear") # clear terminal sebelum render screen
    
    ws = window_size() # Get Window Size

    number_of_lines = height_of_ascii # Jumlah baris yang perlu di print
    vertical_padding_before_divided = ws[1] - number_of_lines # Jumlah padding atas dan bawah

    if vertical_padding_before_divided % 2 != 0: # Kondisi saat jumlah padding atas dan bawah ganjil 
        vertical_padding_before_divided -= 1

    vertical_padding = vertical_padding_before_divided // 2 # Padding vertikal untuk bagian atas dan bagian bawah
    line_of_sentence_start = vertical_padding # Baris ke-n saat teks mulai diprint

    for i in range(ws[1]): # Loop untuk mengeprint baris sebanyak terminal size 

        # Baris pertama dan terakhir ngeprint full '-'
        if i == 0 or i == ws[1] - 1:
            print("-"*ws[0])

        # Baris lainnya yang kosong (bukan baris untuk mengeprint teks)
        elif i < line_of_sentence_start or i >= line_of_sentence_start + number_of_lines:
            print("|", end="")
            print(" "*(ws[0]-2), end="|\n")

        # Baris lainnya yang berisi teks
        else:
            sentence = ascii[i-line_of_sentence_start] # Kalimat pada baris pertama list

            horizontal_padding_before_divided = ws[0] - util_function.length(sentence + '♥', '♥') # Padding kiri dan kanan 

            if horizontal_padding_before_divided % 2 == 0: # ketika padding kiri dan kanan jumlah nya genap
                horizontal_padding =  int(horizontal_padding_before_divided // 2) # Padding kanan dan padding kiri
                is_odd = False # Bukan ganjil
            else:
                horizontal_padding = int(horizontal_padding_before_divided - 1)//2 # Padding kanan dan padding kiri
                is_odd = True # Ganjil

            print("|", end="") # Print border kiri
            print(" "*(horizontal_padding - 1), end="") # Print padding kiri
            print(sentence, end="") # Print kalimat

            if is_odd: # Ketika ganjil
                print(" "*(horizontal_padding), end='|\n') # Print padding kanan
            else:
                print(" "*(horizontal_padding - 1), end="|\n") # Print padding kanan
'''-------------------- Render Screen --------------------'''

'''------------------------------------------------------------ Print Animasi ------------------------------------------------------------'''




'''------------------------------------------------------------ Animasi ------------------------------------------------------------'''
def printascii(typegambar: str,access: str):
    import ayamKokok, animasi.bangunCandi, animasi.batchBangun, animasi.door, animasi.hancurCandi, animasi.hapusJin, animasi.jinBangun, animasi.jinKumpul, animasi.karakterGame, animasi.kumpul, laporan, animasi.saving, animasi.ubahJin

    '''-------------------- Atur Warna Terminal--------------------'''
    os.system("cls||clear")
    if access == "bandung_bondowoso":
        cmd = 'color 9'     
    elif access == "roro_jonggrang":
        cmd = 'color 5'     
    elif access == "Pembangun":
        cmd = 'color 3'     
    elif access == "Pengumpul":
        cmd = 'color 2'     
    else:
        cmd = "color 0"
    os.system(cmd)
    '''-------------------- Atur Warna Terminal --------------------'''


    '''-------------------- Tipe Animasi --------------------'''

    if typegambar == "laporan_jin": # Menampilkan Animasi Laporan Jin
        for i in range(laporan.animasi):
            render_screen(laporan.laporan_jin[i], laporan.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "laporan_candi": # Menampilkan Animasi Laporan Jin
        for i in range(laporan.animasi):
            render_screen(laporan.laporan_candi[i], laporan.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "bandung_bondowoso": # Menampilkan Animasi Karakter Bondowoso
        from Main_Function import user
        arr_print = ["" for i in range(animasi.karakterGame.length + 3)]
        for i in range(animasi.karakterGame.length):
            arr_print[i] = animasi.karakterGame.bondo[i]
        arr_print[animasi.karakterGame.length] = " "
        arr_print[animasi.karakterGame.length + 1] = f"Selamat datang, {user}!"
        arr_print[animasi.karakterGame.length + 2] = "Masukkan command \"help\" untuk daftar command yang dapat kamu panggil."
        for i in range(animasi.karakterGame.animasi):
            render_screen(arr_print, animasi.karakterGame.length + 3)
            time.sleep(0.5)            

    elif typegambar == "roro_jonggrang": # Menampilkan Animasi Karakter Roro
        from Main_Function import user
        arr_print = ["" for i in range(animasi.karakterGame.length + 3)]
        for i in range(animasi.karakterGame.length):
            arr_print[i] = animasi.karakterGame.Roro[i]
        arr_print[animasi.karakterGame.length] = " "
        arr_print[animasi.karakterGame.length + 1] = f"Selamat datang, {user}!"
        arr_print[animasi.karakterGame.length + 2] = "Masukkan command \"help\" untuk daftar command yang dapat kamu panggil."
        for i in range(animasi.karakterGame.animasi):
            render_screen(arr_print, animasi.karakterGame.length + 3)
            time.sleep(0.5)            

    elif typegambar == "Pembangun": # Menampilkan Animasi Karakter Jin Pembangun
        from Main_Function import user
        arr_print = ["" for i in range(animasi.karakterGame.length + 3)]
        for i in range(animasi.karakterGame.length):
            arr_print[i] = animasi.karakterGame.jinBangun[i]
        arr_print[animasi.karakterGame.length] = " "
        arr_print[animasi.karakterGame.length + 1] = f"Selamat datang, {user}!"
        arr_print[animasi.karakterGame.length + 2] = "Masukkan command \"help\" untuk daftar command yang dapat kamu panggil."
        for i in range(animasi.karakterGame.animasi):
            render_screen(arr_print, animasi.karakterGame.length + 3)
            time.sleep(0.5)        

    elif typegambar == "Pengumpul": # Menampilkan Animasi Karakter Jin Pengumpul
        from Main_Function import user
        arr_print = ["" for i in range(animasi.karakterGame.length + 3)]
        for i in range(animasi.karakterGame.length):
            arr_print[i] = animasi.karakterGame.jinKumpul[i]
        arr_print[animasi.karakterGame.length] = " "
        arr_print[animasi.karakterGame.length + 1] = f"Selamat datang, {user}!"
        arr_print[animasi.karakterGame.length + 2] = "Masukkan command \"help\" untuk daftar command yang dapat kamu panggil."
        for i in range(animasi.karakterGame.animasi):
            render_screen(arr_print, animasi.karakterGame.length + 3)
            time.sleep(0.5)            

    elif typegambar == "logout": # Menampilkan Animasi Logout
        for i in range(animasi.door.animasi):
            render_screen(animasi.door.exit[i], animasi.door.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "summon_pembangun": # Menampilkan Animasi Summon Jin Pembangun
        from Main_Function import username_jin_summon
        animasi.jinBangun.summon[6][32] = f"Jin {username_jin_summon} berhasil dipanggil!"
        for i in range(animasi.jinBangun.animasi):
            render_screen(animasi.jinBangun.summon[i], animasi.jinBangun.length)
            time.sleep(0.5)            
        time.sleep(2)

    elif typegambar == "summon_pengumpul": # Menampilkan Animasi Summon Jin Pengumpul
        from Main_Function import username_jin_summon
        animasi.jinKumpul.summon[6][32] = f"Jin {username_jin_summon} berhasil dipanggil!"
        for i in range(animasi.jinKumpul.animasi):
            render_screen(animasi.jinKumpul.summon[i], animasi.jinKumpul.length )
            time.sleep(0.5)            
        time.sleep(2)

    elif typegambar == "hapus_jin_bangun": # Menampilkan Animasi Hapus Jin Bangun
        for i in range(animasi.hapusJin.animasi):
            render_screen(animasi.hapusJin.hapusjinbangun[i], animasi.hapusJin.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "hapus_jin_kumpul": # Menampilkan Animasi Hapus Jin Kumpul
        for i in range(animasi.hapusJin.animasi):
            render_screen(animasi.hapusJin.hapusjinkumpul[i], animasi.hapusJin.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "ubah_kumpul_bangun": # Menampilkan Animasi Ubah Jin Kumpul Menjadi Jin Bangun 
        for i in range(animasi.ubahJin.animasi):
            render_screen(animasi.ubahJin.kumpul_ke_bangun[i], animasi.ubahJin.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "ubah_bangun_kumpul": # Menampilkan Animasi Ubah Jin Bangun Menjadi Jin Kumpul
        for i in range(animasi.ubahJin.animasi):
            render_screen(animasi.ubahJin.bangun_ke_kumpul[i], animasi.ubahJin.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "kumpul": # Menampilkan Animasi Kumpul Bahan
        for i in range(animasi.kumpul.animasi):
            render_screen(animasi.kumpul.kumpul[i], animasi.kumpul.length)
            time.sleep(0.5)
        time.sleep(1)

    elif typegambar == "bangun_candi": # Menampilkan Animasi Bangun Candi
        for i in range(animasi.bangunCandi.animasi):
            render_screen(animasi.bangunCandi.banguncandi[i], animasi.bangunCandi.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "batch_bangun": # Menampilkan Animasi Batch Bangun
        for i in range(animasi.batchBangun.animasi):
            render_screen(animasi.batchBangun.batchbangun[i], animasi.batchBangun.length)
            time.sleep(0.5)
        time.sleep(2) 

    elif typegambar == "hancur_candi": # Menampilkan Animasi Hancurkan Candi
        for i in range(animasi.hancurCandi.animasi):
            render_screen(animasi.hancurCandi.hancurkancandi[i], animasi.hancurCandi.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "bondo_menang": # Menampilkan Animasi Ayam Berkokok Saat Bondo Menang
        for i in range(ayamKokok.animasi):
            render_screen(ayamKokok.bondomenang[i], ayamKokok.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "roro_menang": # Menampilkan Animasi Ayam Berkokok Saat Roro Menang
        for i in range(ayamKokok.animasi):
            render_screen(ayamKokok.roromenang[i], ayamKokok.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "save1": # Menampilkan Animasi Save File Saat Folder Tidak Ditemukan
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Membuat folder {path_folder}   "
        animasi.saving.save[1][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)

    elif typegambar == "save2": # Menampilkan Animasi Save File Saat Parent Folder 'save' Tidak Ditemukan
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Membuat folder save...   "
        animasi.saving.save[1][23] = f"Membuat folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)

    elif typegambar == "save3": # Menampilkan Animasi Save File Saat Folder Sudah Ada
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[1][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)
        
    elif typegambar == "exit": # Menampilkan Animasi Keluar
        for i in range(animasi.door.animasi):
            render_screen(animasi.door.exit[i], animasi.door.length)
            time.sleep(0.5)
        time.sleep(2)

    elif typegambar == "home": # Menampilkan Animasi Main Menu (Saat awal sebelum login)
        render_screen(Manajerial, 35)
        time.sleep(0.5)
        time.sleep(1)
    '''-------------------- Tipe Animasi --------------------'''

'''------------------------------------------------------------ Animasi ------------------------------------------------------------'''