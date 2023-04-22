import Main_Function, time, load_only

if __name__ == "__main__":
    load_only.load()
    while load_only.start:
        menu = input(">>> ")
        if menu == "login" and not Main_Function.logins:
            Main_Function.login()
        elif menu == "login" and Main_Function.logins:
            print("Login gagal!")
            time.sleep(0.1)
            print(f"Anda telah login dengan username {Main_Function.user}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        elif menu == "logout" and Main_Function.logins:
            Main_Function.logout()
        elif menu == "logout" and not Main_Function.logins:
            print("Logout gagal!")
            time.sleep(0.1)
            print(f"Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        elif menu == "summonjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.summonJin()
        elif menu == "hapusjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.hapusJin()
        elif menu == "ubahjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.ubahJin()
        elif menu == "bangun" and Main_Function.access == "Pembangun":
            Main_Function.bangun(Main_Function.user)
        elif menu == "kumpul" and Main_Function.access == "Pengumpul":
            Main_Function.kumpul(False)
        elif menu == "batchkumpul" and Main_Function.access == "bandung_bondowoso":
            Main_Function.batchkumpul()
        elif menu == "batchbangun" and Main_Function.access == "bandung_bondowoso":
            Main_Function.batchbangun()
        elif menu == "laporanjin" and Main_Function.access == "bandung_bondowoso":
            Main_Function.laporanjin()
        elif menu == "laporancandi" and Main_Function.access == "bandung_bondowoso":
            Main_Function.laporancandi()
        elif menu == "hancurkancandi" and Main_Function.access == "roro_jonggrang":
            Main_Function.hancurkancandi()
        elif menu == "ayamberkokok" and Main_Function.access == "roro_jonggrang":
            Main_Function.ayamberkokok()
        elif menu == "exit":
            Main_Function.keluar()
            load_only.start = False
        elif menu == "help":
            Main_Function.help()
        elif menu == "save":
            Main_Function.save()
        elif Main_Function.logins:
            import Visual
            Visual.render_screen(["Access Denied"],1)
            time.sleep(1.5)
            Visual.printascii(Main_Function.access,Main_Function.access)
        elif not Main_Function.logins:
            import Visual
            Visual.render_screen(["Access Denied"],1)
            time.sleep(1.5)
            Visual.printascii("home",Main_Function.access)