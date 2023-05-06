import Main_Function, time, load_only

'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''
if __name__ == "__main__":

    load_only.load() # Melakukan load folder

    while load_only.start: # Saat status start = True
        import Visual
        
        menu = input(">>> ") # Meminta input user
        if menu == "login" and not Main_Function.logins: # Saat user memasukan command login dan user belum login  
            Main_Function.login()

        elif menu == "login" and Main_Function.logins: # Saat user memasukan command login namun user sudah login
            Visual.render_screen(["Login gagal!",f"Anda telah login dengan username {Main_Function.user}, silahkan lakukan “logout” sebelum melakukan login kembali."],2) # Pesan Kesalahan
            time.sleep(2)

        elif menu == "logout" and Main_Function.logins: # Saat user memasukan command logout dan user sudah login
            Main_Function.logout()
            Visual.printascii("home",None) # Tampilan Home Awal

        elif menu == "logout" and not Main_Function.logins: # Saat user memasukan command logout namun user belum login
            Visual.render_screen(["Logout gagal!",f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout"],2)
            time.sleep(2)
            Visual.printascii("home",None) # Tampilan Home Awal 

        elif menu == "summonjin" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command summonjin dan memiliki akses Bondowoso
            Main_Function.summonJin()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "hapusjin" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command hapusjin dan memiliki akses Bondowoso
            Main_Function.hapusJin()
            Main_Function.update_stack("hapus")
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "ubahjin" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command ubahjin dan memiliki akses Bondowoso
            Main_Function.ubahJin()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "bangun" and Main_Function.access == "jin_pembangun": # Saat user memasukan command bangun dan memiliki akses jin_pembangun
            Main_Function.bangun(Main_Function.user)
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "kumpul" and Main_Function.access == "jin_pengumpul": # Saat user memasukan command kumpul dan memiliki akses jin_pengumpul
            Main_Function.kumpul(False)
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "batchkumpul" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command batchkumpul dan memiliki akses Bondowoso
            Main_Function.batchkumpul()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "batchbangun" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command batchbangun dan memiliki akses Bondowoso
            Main_Function.batchbangun()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "laporanjin" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command laporanjin dan memiliki akses Bondowoso
            Main_Function.laporanjin()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "laporancandi" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command laporancandi dan memiliki akses Bondowoso
            Main_Function.laporancandi()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role
            
        elif menu == "undo" and Main_Function.access == "bandung_bondowoso": # Saat user memasukan command undo dan memiliki akses Bondowoso
            Main_Function.undo()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "hancurkancandi" and Main_Function.access == "roro_jonggrang": # Saat user memasukan command hancurkancandi dan memiliki akses Roro
            Main_Function.hancurkancandi()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role

        elif menu == "ayamberkokok" and Main_Function.access == "roro_jonggrang": # Saat user memasukan command ayamberkokok dan memiliki akses Roro
            Main_Function.ayamberkokok()
            load_only.start = False

        elif menu == "exit": # Saat user memasukan command exit
            Main_Function.keluar()
            load_only.start = False

        elif menu == "help": # Saat user memasukan command help
            Main_Function.help()

        elif menu == "save": # Saat user memasukan command save
            Main_Function.save()
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role 
            Main_Function.update_stack("save")

        elif Main_Function.logins: # Validasi saat user sudah login namun salah menginputkan command yang tidak sesuai dengan akses user
            Visual.render_screen(["ACCESS DENIED",'Command yang dimasukan salah!'],2) # Pesan Kesalahan
            time.sleep(1.5)
            Visual.printascii(Main_Function.access,Main_Function.access) # Tampilan Karakter sesuai dengan role 

        elif not Main_Function.logins: # Validasi saat user belum login dan menginputkan command yang memerlukan akses
            Visual.render_screen(["ACCESS DENIED","Anda Belum Login!"],2) # Pesan Kesalahan
            time.sleep(1.5)
            Visual.printascii("home",None) # Tampilan Home Awal


'''---------------------------------------------------------- Starting Point ----------------------------------------------------------'''