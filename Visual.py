import os, time


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


def render_screen(ascii, height_of_ascii):
    # clear terminal before render the screen
    os.system("cls||clear")
    

    ws = window_size()
    number_of_lines = height_of_ascii
    vertical_padding_before_divided = ws[1] - number_of_lines
    if vertical_padding_before_divided % 2 == 0: 
        vertical_padding_before_divided = vertical_padding_before_divided 
    else:
        vertical_padding_before_divided - 1
    vertical_padding = vertical_padding_before_divided // 2
    line_of_sentence_start = vertical_padding

    for i in range(ws[1]):
        # first line and last line set with full border
        if i == 0 or i == ws[1] - 1:
            print("-"*ws[0])
        # other lines
        elif i < line_of_sentence_start or i >= line_of_sentence_start + number_of_lines:
            print("|", end="")
            print(" "*(ws[0]-2), end="|\n")
        else:
            sentence = ascii[i-line_of_sentence_start]

            horizontal_padding_before_divided = ws[0] - len(sentence)

            if horizontal_padding_before_divided % 2 == 0: 
                is_odd = False 
            else:
                is_odd = True

            if is_odd:
                horizontal_padding = int(horizontal_padding_before_divided - 1)//2 
            else:
                horizontal_padding =  int(horizontal_padding_before_divided // 2)
            print("|", end="")
            print(" "*(horizontal_padding - 1), end="")
            print(sentence, end="")
            if is_odd:
                print(" "*(horizontal_padding), end='|\n')
            else:
                print(" "*(horizontal_padding - 1), end="|\n")


def printascii(typegambar,access):
    import ayamKokok, animasi.bangunCandi, animasi.batchBangun, animasi.door, animasi.hancurCandi, animasi.hapusJin, animasi.jinBangun, animasi.jinKumpul, animasi.karakterGame, animasi.kumpul, laporan, animasi.saving, animasi.ubahJin

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

    if typegambar == "bangun_candi":
        for i in range(animasi.bangunCandi.animasi):
            render_screen(animasi.bangunCandi.banguncandi[i], animasi.bangunCandi.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "laporan_jin":
        for i in range(laporan.animasi):
            render_screen(laporan.laporan_jin[i], laporan.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "laporan_candi":
        for i in range(laporan.animasi):
            render_screen(laporan.laporan_candi[i], laporan.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "bandung_bondowoso":
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
    elif typegambar == "roro_jonggrang":
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
    elif typegambar == "Pembangun":
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
    elif typegambar == "Pengumpul":
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
    elif typegambar == "logout":
        for i in range(animasi.door.animasi):
            render_screen(animasi.door.exit[i], animasi.door.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "summon_pembangun":
        from Main_Function import user
        animasi.jinBangun.summon[6][32] = f"Jin {user} berhasil dipanggil!"
        for i in range(animasi.jinBangun.animasi):
            render_screen(animasi.jinBangun.summon, animasi.jinBangun.length + 2)
            time.sleep(0.5)            
        time.sleep(2)
    elif typegambar == "summon_pengumpul":
        from Main_Function import user
        animasi.jinKumpul.summon[6][32] = f"Jin {user} berhasil dipanggil!"
        for i in range(animasi.jinKumpul.animasi):
            render_screen(animasi.jinKumpul.summon, animasi.jinKumpul.length + 2)
            time.sleep(0.5)            
        time.sleep(2)
    elif typegambar == "hapus_jin_bangun":
        for i in range(animasi.hapusJin.animasi):
            render_screen(animasi.hapusJin.hapusjinbangun[i], animasi.hapusJin.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "hapus_jin_kumpul":
        for i in range(animasi.hapusJin.animasi):
            render_screen(animasi.hapusJin.hapusjinkumpul[i], animasi.hapusJin.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "ubah_kumpul_bangun":
        for i in range(animasi.ubahJin.animasi):
            render_screen(animasi.ubahJin.kumpul_ke_bangun[i], animasi.ubahJin.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "ubah_bangun_kumpul":
        for i in range(animasi.ubahJin.animasi):
            render_screen(animasi.ubahJin.bangun_ke_kumpul[i], animasi.ubahJin.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "kumpul":
        for i in range(animasi.kumpul.animasi):
            render_screen(animasi.kumpul.kumpul[i], animasi.kumpul.length)
            time.sleep(0.5)
        time.sleep(1)
    elif typegambar == "batch_bangun":
        for i in range(animasi.batchBangun.animasi):
            render_screen(animasi.batchBangun.batchbangun[i], animasi.batchBangun.length)
            time.sleep(0.5)
        time.sleep(2) 
    elif typegambar == "hancur_candi":
        for i in range(animasi.hancurCandi.animasi):
            render_screen(animasi.hancurCandi.hancurkancandi[i], animasi.hancurCandi.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "bondo_menang":
        for i in range(ayamKokok.animasi):
            render_screen(ayamKokok.bondomenang[i], ayamKokok.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "roro_menang":
        for i in range(ayamKokok.animasi):
            render_screen(ayamKokok.roromenang[i], ayamKokok.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "save1":
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Membuat folder {path_folder}   "
        animasi.saving.save[1][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)
    elif typegambar == "save2":
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Membuat folder save...   "
        animasi.saving.save[1][23] = f"Membuat folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)
    elif typegambar == "save3":
        from Main_Function import path_folder
        animasi.saving.save[0][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[1][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[2][23] = f"Menyimpan data pada folder {path_folder}   "
        animasi.saving.save[3][23] = f"Berhasil menyimpan data di folder {path_folder}!"
        for i in range(animasi.saving.animasi):
            render_screen(animasi.saving.save[i], animasi.saving.length)
            time.sleep(1.5)
        time.sleep(2)
    elif typegambar == "exit":
        for i in range(animasi.door.animasi):
            render_screen(animasi.door.exit[i], animasi.door.length)
            time.sleep(0.5)
        time.sleep(2)
    elif typegambar == "home":
        render_screen(Manajerial, 35)
        time.sleep(0.5)
        time.sleep(1)


# printascii("roro_jonggrang","roro_jonggrang")

# INFO
# BONDO COLOR 9
# RORO COLOR 5
# BANGUN COLOR 3
# KUMPUL COLOR 6