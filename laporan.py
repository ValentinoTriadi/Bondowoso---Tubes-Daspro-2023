def lapor(type:str)->list:
    import tempdata, function_jin, function_candi
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
        jin_terajin = function_jin.jinter(True) # Mencari jin terajin
        jin_termalas = function_jin.jinter(False) # Mencari jin termalas

        laporanjin = [
        "       ..,,,*                                                     ,.,.           ",
        "         ,*,,,                                                       .,,         ",
        "         &%%((##*/((###############(######(#(((((((###((((#(###(#(((%##(#        ",
        "        &&&%####//((#####%#%###%#%#%%%##########################((((%%#(#        ",
        "        &&&%##%/(((##%                                     %#####(((&%((#        ",
        "         &&%#%%(/(#%                                          ######&%#(#        ",
        "         &&##%%((##    "+f"> Total Jin: {tempdata.len_user-2}".ljust(36," ")+"    %####&%###        ",  # Menampilkan total jin dari panjang data jin
        "         &%####(##     "+f"> Total Jin Pengumpul: {function_jin.count_jin('Pengumpul')}".ljust(36," ")+"     ###%&%###        ", # Menghitung jumlah jin dengan role pengumpul
        "         &%###(((#     "+f"> Total Jin Pembangun: {function_jin.count_jin('Pembangun')}".ljust(36," ")+"      ##&%####        ", # Menghitung jumlah jin dengan role pembangun
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
