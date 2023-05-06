def lapor(type:str)->list:
    import tempdata, function_jin, function_candi, util_function
    laporan2 = [
    "",
    "       ..,,,*                     ,.,.            ",
    "         ,*,,,                        .,,         ",
    "         &%%((##*/((####((#(###(#(((%##(#         ",
    "        &&&%####//((#############((((%%#(#        ",
    "        &&&%##%/(((##%#%##########(((&%((#        ",
    "         &&%#%%(/(#%%%%%%%%%########&%#(#         ",
    "         &&##%%((##%%%%%#%%%%%%%####&%###         ",
    "         &%####(###%%%%%%%%%%%%%###%&%###         ",
    "         &%###(((#%%%%%%%%%##%%%###&%####         ",
    "         &%%##((##%%%%%%%#%%%%#####%%#(##         ",
    "         &%###((##%%%%%%%%#%%%%####&%#(##         ",
    "         &%###((##%%%%%%%%%%%%%%###&%#((#         ",
    "         %%#%#((##%%%%%%%%%%%%%%##&&%####         ",
    "        &&%#%(((##%%%%%%%%%%%%%%##&&%###%         ",
    "        &%%##(((##%%%%%%%%%%%%%%%%#&&%####        ",
    "        &&###/((###%%%%%%%%&%%%####&&%####        ",
    "        &%###//(####%##%%###%######%&%####(       ",
    "        &%##*//(((#############((%&%#((((         ",
    "        ,*//(                         .**/.,,     ",
    "         ,,,                           ,...       "
    "",
    ""]

    laporan3 = [
    "       ..,,,*   ,.,.             ",
    "         ,*,,,    .,,            ",
    "         &%%((##*(((%##(#        ",
    "        &&&%######((%%#(#        ",
    "        &&&%##%/((((&%((#        ",
    "         &&%#%%(/##&%#(#         ",
    "         &&##%%(()##&%###        ",
    "         &%####(##)&%###         ",
    "         &%###(())#&%####        ",
    "         &%%##(())%%#(##         ",
    "         &%###(())&%#(##         ",
    "         &%###(())#&%#((#        ",
    "         %%#%#())&&%####         ",
    "        &&%#%(())&%###%          ",
    "        &%%##(())&&%####         ",
    "        &&###/(())&%####         ",
    "        &%###//()))####(         ",
    "        &%##*/####&%#((((        ",
    "        ,*//(  .**/.,,           ",
    "         ,,,    ,...             ",
    "",
    ""]

    data_bahan = tempdata.data_bahan_bangunan # Mengambil data bahan dari module tempdatas 
    if type == "candi": # Ketika user ingin menampilkan laporan candi
        ter_mahal, harga_mahal = function_candi.canditer(True) # Mencari id candi termahal dengan harganya (Parameter True berarti termahal)
        ter_murah, harga_murah = function_candi.canditer(False) # Mencari id candi termurah dengan harganya (Parameter False berarti termurah)

        laporancandi = [
        "       ..,,,*                                                     ,.,.           ",
        "         ,*,,,                                                       .,,         ",
        "         &%%((##*/((###############(######(#(((((((###((((#(###(#(((%##(#        ",
        "        &&&%####//((#####%#%###%#%#%%%##########################((((%%#(#        ",
        "        &&&%##%/(((##%                                     %#####(((&%((#        ",
        "         &&%#%%(/(#%                                          ######&%#(#        ",
        "         &&##%%((##                                            %####&%###        ",
        "         &%####(##     "+f"> Total Candi: {tempdata.len_candi}".ljust(36, " ")+"     ###%&%###        ", # Menampilkan total candi dari panjang data candi
        "         &%###(((#     "+f"> Total Pasir Yang Digunakan: {function_candi.countbahan('pasir')}".ljust(36, " ")+"      ##&%####        ", # Menghitung bahan pasir dari data
        "         &%%##((#      "+f"> Total Batu Yang Digunakan: {function_candi.countbahan('batu')}".ljust(36, " ")+"       #%%#(##        ", # Menghitung bahan batu dari data
        "         &%###((       "+f"> Total Air Yang Digunakan: {function_candi.countbahan('air')}".ljust(36, " ")+"       #&%#(##        ", # Menghitung bahan air dari data
        "         &%###((#      "+f"> ID Candi Termahal: {ter_mahal} ({harga_mahal})".ljust(36, " ")+"       #&%#((#        ", # Menampilkan ID Candi termahal dengan harganya
        "         %%#%#((##     "+f"> ID Candi Termurah: {ter_murah} ({harga_murah})".ljust(36, " ")+"      #&&%####        ", # Menampilkan ID Candi termurah dengan harganya
        "        &&%#%(((##                                             %##&&%###%        ",
        "        &%%##(((##%%                                         %%%%#&&%####        ",
        "        &&###/((###%%%                                     #######&&%####        ",
        "        &%###//(####%##%%###%%%%#################################%&%####(        ",
        "        &%##*//(((#################################         ##(((%&%#((((        ",
        "        ,*//(                                                    .**/.,,         ",
        "         ,,,                                                        ,...         ",
        "",
        "Tekan \"Enter\" setelah selesai membaca laporan"]

        return [laporan3, laporan2,laporancandi] # Mengembalikan array berisi laporan candi
    
    elif type == "jin": # Ketika user ingin menampilkan laporan jin
        '''-------------------- Cari Jin Terajin --------------------'''
        jin_terajin = function_jin.jinter(True) # Mencari jin terajin
        '''-------------------- Cari Jin Terajin --------------------'''

        '''-------------------- Validasi Panjang Nama Jin Terajin --------------------'''
        if util_function.length(jin_terajin + ".", '.') > 20: # Jika panjang nama jin terajin lebih dari 20 huruf
            jin_terajin1 = '' # Temporary variable untuk menyimpan nama jin yang sudah divalidasi
            for i in range(20): # Loop untuk mengisi temporary variable
                if i < 17: # Ketika index nama jin masih dibawah 17
                    jin_terajin1 += jin_terajin[i]
                else: # Ketika index nama jin sudah 17 keatas
                    jin_terajin1 += '.' # Menambahkan ... ke akhir dari nama jin
            jin_terajin = jin_terajin1 # Update nama jin terajin
        '''-------------------- Validasi Panjang Nama Jin Terajin --------------------'''
        

        '''-------------------- Cari Jin Termalas --------------------'''
        jin_termalas = function_jin.jinter(False) # Mencari jin termalas
        '''-------------------- Cari Jin Termalas --------------------'''

        '''-------------------- Validasi Panjang Nama Jin Termalas --------------------'''
        if util_function.length(jin_termalas + ".", '.') > 20:
            jin_termalas1 = '' # Temporary variable untuk menyimpan nama jin yang sudah divalidasi
            for i in range(20): # Loop untuk mengisi temporary variable
                if i < 17: # Ketika index nama jin masih dibawah 17
                    jin_termalas1 += jin_termalas[i] 
                else: # Ketika index nama jin sudah 17 keatas
                    jin_termalas1 += '.' # Menambahkan ... ke akhir dari nama jin
            jin_termalas = jin_termalas1 # Update nama jin termalas
        '''-------------------- Validasi Panjang Nama Jin Termalas --------------------'''

        laporanjin = [
        "       ..,,,*                                                     ,.,.           ",
        "         ,*,,,                                                       .,,         ",
        "         &%%((##*/((###############(######(#(((((((###((((#(###(#(((%##(#        ",
        "        &&&%####//((#####%#%###%#%#%%%##########################((((%%#(#        ",
        "        &&&%##%/(((##%                                     %#####(((&%((#        ",
        "         &&%#%%(/(#%                                          ######&%#(#        ",
        "         &&##%%((##    "+f"> Total Jin: {tempdata.len_user-2}".ljust(36," ")+"    %####&%###        ",  # Menampilkan total jin dari panjang data jin
        "         &%####(##     "+f"> Total Jin Pengumpul: {function_jin.count_jin('jin_pengumpul')}".ljust(36," ")+"     ###%&%###        ", # Menghitung jumlah jin dengan role pengumpul
        "         &%###(((#     "+f"> Total Jin Pembangun: {function_jin.count_jin('jin_pembangun')}".ljust(36," ")+"      ##&%####        ", # Menghitung jumlah jin dengan role pembangun
        "         &%%##((#      "+f"> Jin Terajin: {jin_terajin}".ljust(36," ")+"       #%%#(##        ", # Mencari jin dengan jumlah candi yang dibuat terbanyak
        "         &%###((       "+f"> Jin Termalas: {jin_termalas}".ljust(36," ")+"       #&%#(##        ", # Mencari jin dengan jumlah candi yang dibuat tersedikit
        "         &%###((#      "+f"> Jumlah Pasir: {data_bahan[0][0]} unit".ljust(36," ")+"       #&%#((#        ", # Menghitung banyak pasir yang sudah digunakan 
        "         %%#%#((##     "+f"> Jumlah Air: {data_bahan[0][1]} unit".ljust(36," ")+"      #&&%####        ", # Menghitung banyak batu yang sudah digunakan
        "        &&%#%(((##     "+f"> Jumlah Batu: {data_bahan[0][2]} unit".ljust(36," ")+"    %##&&%###%        ", # Menghitung banyak batu yang sudah digunakan
        "        &%%##(((##%%                                         %%%%#&&%####        ",
        "        &&###/((###%%%                                     #######&&%####        ",
        "        &%###//(####%##%%###%%%%#################################%&%####(        ",
        "        &%##*//(((#################################         ##(((%&%#((((        ",
        "        ,*//(                                                    .**/.,,         ",
        "         ,,,                                                        ,...         ",
        "",
        "Tekan \"Enter\" setelah selesai membaca laporan"]

        return [laporan3, laporan2,laporanjin] # Mengembalikan array berisi laporan jin

animasi = 3 # Jumlah animasi
length = 22 # Tinggi animasi
