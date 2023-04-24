nama_folder = ""
start = False

'''------------------------------------------------------------F13------------------------------------------------------------'''
def load():
    global start, nama_folder # Merubah status start dan merubah data nama folder yang di load
    import argparse, os

    '''-------------------- Membuat Argument --------------------'''
    parser = argparse.ArgumentParser()
    parser.add_argument("name_folder", help="Nama Folder", nargs='?')
    '''-------------------- Membuat Argument --------------------'''


    '''-------------------- Mengambil Nama Folder --------------------'''
    name_folder = parser.parse_args().name_folder # Mengambil nama folder yang akan di load dari input user
    path_folder = f"./save/{name_folder}" # Membuat path directory tempat folder berada
    '''-------------------- Mengambil Nama Folder --------------------'''

    
    '''-------------------- Validasi Nama Folder --------------------'''
    if os.path.isdir(path_folder): # Saat nama folder yang diinput ditemukan dalam directory
        start = True # Merubah status jalannya program
        nama_folder = name_folder # Merubah nama folder yang sedang diload untuk keperluan mengambil/membaca data

        
        '''-------------------- Tampilan Animasi --------------------'''
        import Visual, time
        Visual.render_screen(["Loading.     "],1)
        time.sleep(1)
        Visual.render_screen(["Loading..    "],1)
        time.sleep(1)
        Visual.render_screen(["Loading...   "],1)
        time.sleep(1)
        Visual.printascii("home", None)
        '''-------------------- Tampilan Animasi --------------------'''

    elif name_folder == None: # Saat nama folder yang diinput kosong
        import Visual
        Visual.render_screen(['Tidak ada nama folder yang diberikan!',' ','Usage: python main.py <nama_folder>'],3) # Pesan kesalahan
    
    elif not os.path.isdir(path_folder): # Saat nama folder yang diinput tidak ada pada directory
        import Visual
        Visual.render_screen([f"Folder \"{name_folder}\" tidak ditemukan."],1) # Pesan kesalahan
    '''-------------------- Validasi Nama Folder --------------------'''

'''------------------------------------------------------------F13------------------------------------------------------------'''