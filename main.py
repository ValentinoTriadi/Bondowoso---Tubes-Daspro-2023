import Main_Function, time, load_only

if __name__ == "__main__":
    load_only.load()
    while load_only.start:
        menu = input(">>> ")
        import Visual
        if menu == "login" and not Main_Function.logins:
            Main_Function.login()

        elif menu == "login" and Main_Function.logins:
            Visual.render_screen(["Login gagal!",f"Anda telah login dengan username {Main_Function.user}, silahkan lakukan “logout” sebelum melakukan login kembali."],2)
            time.sleep(2)

        elif menu == "logout" and Main_Function.logins:
            Main_Function.logout()
            Visual.printascii("home",None)

        elif menu == "logout" and not Main_Function.logins:
            Visual.render_screen(["Logout gagal!",f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout"],2)
            time.sleep(2)
            Visual.printascii("home",None)

        elif menu == "summonjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.summonJin()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "hapusjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.hapusJin()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "ubahjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.ubahJin()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "bangun" and Main_Function.access == "Pembangun":
            Main_Function.bangun(Main_Function.user)
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "kumpul" and Main_Function.access == "Pengumpul":
            Main_Function.kumpul(False)
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "batchkumpul" and Main_Function.access == "bandung_bondowoso":
            Main_Function.batchkumpul()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "batchbangun" and Main_Function.access == "bandung_bondowoso":
            Main_Function.batchbangun()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "laporanjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.laporanjin()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "laporancandi" and Main_Function.access == "bandung_bondowoso":
            Main_Function.laporancandi()
            Visual.printascii(Main_Function.access,Main_Function.access)
            
        elif menu == "hancurkancandi" and Main_Function.access == "roro_jonggrang":
            Main_Function.hancurkancandi()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif menu == "ayamberkokok" and Main_Function.access == "roro_jonggrang":
            Main_Function.ayamberkokok()
            load_only.start = False

        elif menu == "exit":
            Main_Function.keluar()
            load_only.start = False

        elif menu == "help":
            Main_Function.help()
            
        elif menu == "save":
            Main_Function.save()
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif Main_Function.logins:
            Visual.render_screen(["Access Denied"],1)
            time.sleep(1.5)
            Visual.printascii(Main_Function.access,Main_Function.access)

        elif not Main_Function.logins:
            import Visual
            Visual.render_screen(["Access Denied","Anda Belum Login!"],2)
            time.sleep(1.5)
            Visual.printascii("home",Main_Function.access)