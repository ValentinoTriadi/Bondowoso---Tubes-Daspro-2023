nama_folder = ""
start = False
def load():
    global start, nama_folder
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument("name_folder", help="Nama Folder", nargs='?')

    name_folder = parser.parse_args().name_folder
    # name_folder = "asdfasdfasdf"
    path_folder = f"./save/{name_folder}"
    if os.path.isdir(path_folder):
        start = True
        nama_folder = name_folder
        import Visual, time
        Visual.render_screen(["Loading.     "],1)
        time.sleep(1)
        Visual.render_screen(["Loading..    "],1)
        time.sleep(1)
        Visual.render_screen(["Loading...   "],1)
        time.sleep(1)
        Visual.printascii("home", None)
    elif name_folder == None:
        import Visual
        Visual.render_screen(['Tidak ada nama folder yang diberikan!',' ','Usage: python main.py <nama_folder>'],3)
    elif not os.path.isdir(path_folder):
        import Visual
        Visual.render_screen([f"Folder \"{name_folder}\" tidak ditemukan."],1)