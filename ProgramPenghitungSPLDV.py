def solve_equations():
    
    print("===================================================================================================")
    print("||                   Program untuk Menyelesaikan Sistem Persamaan Dua Variabel                   ||")
    print("===================================================================================================")
    print("===================================================================================================")
    print("|| Panduan dan Contoh Masukkan Koefisien dan Konstanta:                                          ||")
    print("||                                                                                               ||")
    print("|| Contoh Persamaan 1: 2x + 3y = 5                                                               ||")
    print("||                                                                                               ||")
    print("|| Masukkan koefisien x pada persamaan 1 : 2                                                     ||")
    print("|| Masukkan koefisien y pada persamaan 1 : 3                                                     ||")
    print("|| Masukkan konstanta   pada persamaan 1 : 5                                                     ||")
    print("||                                                                                               ||")
    print("|| Contoh Persamaan 2: 4x - 2y = 8                                                               ||")
    print("||                                                                                               ||")
    print("|| Masukkan koefisien x pada persamaan 2 : 4                                                     ||")
    print("|| Masukkan koefisien y pada persamaan 2 : -2                                                    ||")
    print("|| Masukkan konstanta   pada persamaan 2 : 8                                                     ||")
    print("===================================================================================================")
    print("---------------------------------------------------------------------------------------------------")
    a = float(input("| Masukkan koefisien x pada persamaan 1 : "))
    b = float(input("| Masukkan koefisien y pada persamaan 1 : "))
    c = float(input("| Masukkan konstanta pada persamaan 1   : "))
    print("--------------------------------------------")
    d = float(input("| Masukkan koefisien x pada persamaan 2 : "))
    e = float(input("| Masukkan koefisien y pada persamaan 2 : "))
    f = float(input("| Masukkan konstanta pada persamaan 2   : "))
    print("---------------------------------------------------------------------------------------------------")
    
    det = a * e - b * d
    
    if det == 0:

        print("\nSistem persamaan tidak memiliki solusi unik.")

    else:

        x = (c * e - b * f) / det
        y = (a * f - c * d) / det
        
        # Menampilkan persamaan 1 yang diinput oleh user
        print("Persamaan 1: ", end="")
        
        # Menangani koefisien x
        if a != 0:
            if abs(a) != 1:
                print(a, end="")
            if a < 0 and a > -2:
                print("-", end="")
            print("x", end="")
        
        # Menangani tanda dan koefisien y
        if b != 0:
            if a != 0:
                if b > 0:
                    print(" + ", end="")
                elif b < 0:
                    print(" ", end="")
            if abs(b) != 1:
                print(b, end="")
            if b < 0 and b > -2:
                print("-", end="")
            print("y", end="")
        
        print(" =", c)
        
        # Menampilkan persamaan 2 yang diinput oleh user
        print("Persamaan 2: ", end="")
        
        # Menangani koefisien x
        if d != 0:
            if abs(d) != 1:
                print(d, end="")
            if d < 0 and d > -2:
                print("-", end="")
            print("x", end="")
        
        # Menangani tanda dan koefisien y
        if e != 0:
            if d != 0:
                if e > 0:
                    print(" + ", end="")
                elif e < 0:
                    print(" ", end="")
            if abs(e) != 1:
                print(e, end="")
            if e < 0 and e > -2:
                print("-", end="")
            print("y", end="")
        
        print(" =", f)
        print()
        print("Nilai x:", x)
        print("Nilai y:", y)
    
    print()
    pilihan = input("Ingin Menghitung Ulang? (Y/N) : ")
    print()

    if pilihan == 'Y' or pilihan == 'y':
        solve_equations() # kembali ke awal

    elif pilihan == 'N' or pilihan == 'n':
        print("Terimakasih !")
        print()
        exit(0) # mengakhiri program

solve_equations()
