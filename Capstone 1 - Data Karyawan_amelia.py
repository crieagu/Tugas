# Full Program
# Import Library
import os

# Define Global Variable
# ------------
list_index = [] # index untuk show filtered data
del_EmployeeID = '' # untuk passing ke def lain

# Define Initial Data
EmployeeID = ['ISA001','ISA002','ISA003','ISA004','ISA005','ISA006','ISA007','ISA008','ISA009','ISA010']
Name = ['Agus Putra', 'Aditi Mutiara', 'Bagas Putra', 'Juan Apinya', 'Isal Hamali', 'Citra Renata','Poppy Mercury','Yasmina Amari', 'Budiarto Agus','Filantya Dwi']
Departement = ['Engineering','Accounting', 'Maintenance', 'Operation', 'Sales', 'Sales', 'Engineering', 'Accounting', 'Operation', 'Operation']
Position = ['Engineer', 'Manager', 'Supervisor', 'Operator', 'Staff', 'Staff', 'Engineer', 'Staff', 'Operator', 'Manager']
Status = ['Active','Active','Active','Active','Active','Active','Active','Active','Active','Active']

#EmployeeID sebagai key

# Function to clear screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

# Function to display message
def show_message(message):
    print(f'\n{message}\n')
      
# Menu 1 - View
# Bikin Tabular Frame
kolom1, kolom2, kolom3, kolom4, kolom5 = 'EmployeeID', 'Name', 'Departement', 'Position', 'Status'
LK = 20 # lebar kolom
k1s = ((LK-len(kolom1))//2)
k2s = ((LK-len(kolom2))//2)
k3s = ((LK-len(kolom3))//2)
k4s = ((LK-len(kolom4))//2)
k5s = ((LK-len(kolom5))//2)
k1a = ((LK-len(kolom1))-k1s)
k2a = ((LK-len(kolom2))-k2s)
k3a = ((LK-len(kolom3))-k3s)
k4a = ((LK-len(kolom4))-k4s)
k5a = ((LK-len(kolom5))-k5s)

#Show table header
def table_header():
    print(f"+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+")
    print(f"|{' '*(k1s)}EmployeeID{' '*(k1a)}|{' '*(k2s)}Name{' '*(k2a)}|{' '*(k3s)}Departement{' '*(k3a)}|{' '*(k4s)}Position{' '*(k4a)}|{' '*(k5s)}Status{' '*(k5a)}|")
    print(f"+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+")

# show table end
def table_end():
    print(f"+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+{'-'*LK}+")
    
# Show all data
def show_all_data():
    table_header()
    for i in range(len(EmployeeID)): # 0,1
        print(f'|{EmployeeID[i]}{' '*(LK-len(EmployeeID[i]))}|{Name[i]}{' '*(LK-len(Name[i]))}|{Departement[i]}{' '*(LK-len(Departement[i]))}|{Position[i]}{' '*(LK-len(Position[i]))}|{Status[i]}{' '*(LK-len(Status[i]))}|')
    table_end()

# Show Filter Data    
def find_index():
    global list_index
    list_index.clear() #hapus hasil sebelumnya
    f_name = input(f'Masukan Filter Nama maximum 2 kata: ').split()
    
    if len(f_name) < 1:
        show_message('Masukan nama yang ingin dicari')
        return
    
    y = f_name[0].upper()
    cari_nama = ' '.join(f.upper() for f in f_name)
    
    for index, name in enumerate(Name):
        if (len(f_name) == 1 and y in name.upper()) or (len(f_name) > 1 and cari_nama in name.upper()):
            list_index.append(index)

    if len(list_index) == 0:
        show_message('Data tidak ditemukan')
    
def show_filter_data():
    global list_index
    find_index()
    table_header()
    if len(list_index) == 0:
        show_message('Data tidak ditemukan')
    else :
        for i in list_index: # 1,2,3,4
            print(f'|{EmployeeID[i]}{' '*(LK-len(EmployeeID[i]))}|{Name[i]}{' '*(LK-len(Name[i]))}|{Departement[i]}{' '*(LK-len(Departement[i]))}|{Position[i]}{' '*(LK-len(Position[i]))}|{Status[i]}{' '*(LK-len(Status[i]))}|')
    table_end()   

# Menu 2 - Create New Data
def create_new_data():
    show_message('Silahkan masukan data karyawan baru')
    new_name = str(input(f'Masukkan Nama Lengkap (max 3 kata): ')).title()
    # check duplicate
    if new_name.upper() in [name.upper() for name in Name]:
        show_message('Nama sudah ada. Silakan masukkan nama yang berbeda.')
        return  # Exit the function if the name already exists
    
    new_dept = str(input(f'Masukkan Nama Departement: ')).title()
    new_pos = str(input(f'Masukkan Nama Posisi: ')).title()
    new_status = str(input(f'Masukkan Employee status: ')).title()
    
    try:
        save_new_data = str(input(f'Apakah anda ingin menyimpan data baru? (Y/N)'))
    
        if save_new_data.lower() == 'y':
            new_index = len(EmployeeID) + 1
            if new_index < 10:
                New_EmployeeID = f'ISA00{new_index}'
            elif new_index < 100:
                New_EmployeeID = f'ISA0{new_index}'
            else:
                New_EmployeeID = f'ISA{new_index}'
        
            print(New_EmployeeID)
            EmployeeID.append(New_EmployeeID)
            Name.append(new_name)
            Departement.append(new_dept)
            Position.append(new_pos)
            Status.append(new_status)

            show_message('Data berhasil ditambahkan')
            show_all_data()
        
        elif save_new_data.lower() == 'n':
            show_message('Data tidak disimpan')

    except:
        show_message('Masukan Y atau N')  

# Menu 3 - Update Data
def find_data_to_update():
    global list_index
    global del_EmployeeID
    list_index.clear() #hapus hasil sebelumnya
    try:
        upd_EmployeeID = input(f'Masukan EmployeeID yang ingin diupdate: ').strip()
    
        if len(upd_EmployeeID) < 1:
            show_message('Masukan EmployeeID yang ingin dihapus')
            return
        else:
            for index in range(len(EmployeeID)):
                if upd_EmployeeID.upper() == EmployeeID[index]:
                    list_index.append(index)
    
        table_header()
        if len(list_index) == 0:
            show_message('Data tidak ditemukan')
        else :
            for i in list_index:
                print(f'|{EmployeeID[i]}{' '*(LK-len(EmployeeID[i]))}|{Name[i]}{' '*(LK-len(Name[i]))}|{Departement[i]}{' '*(LK-len(Departement[i]))}|{Position[i]}{' '*(LK-len(Position[i]))}|{Status[i]}{' '*(LK-len(Status[i]))}|')
        table_end()
    except:
        show_message('Masukan EmployeeID yang ingin dirubah')
        find_data_to_update()
          
def update_data():
    global list_index
    find_data_to_update()
    
    print(list_index)
    if len(list_index) == 0:
        return
    
    upd_usr_inp = int(input(f'Data apa yang ingin dirubah (1.Nama,2.Departement,3.Posisi,4.Status) : '))
    for i in list_index:
        if upd_usr_inp == 1:
            upd_name = input(f'Masukan Nama baru : ').title()
            Name[i] = upd_name
        elif upd_usr_inp == 2:
            upd_dept = input(f'Masukan Departement baru : ').title()
            Departement[i] = upd_dept
        elif upd_usr_inp == 3:
            upd_pos = input(f'Masukan Posisi baru : ').title()
            Position[i] = upd_pos
        elif upd_usr_inp == 4:
            upd_status = input(f'Masukan Status baru : ').title()
            Status[i] = upd_status
        show_message('Data berhasil dirubah!!!')
        table_header()
        for i in list_index:
            print(f'|{EmployeeID[i]}{' '*(LK-len(EmployeeID[i]))}|{Name[i]}{' '*(LK-len(Name[i]))}|{Departement[i]}{' '*(LK-len(Departement[i]))}|{Position[i]}{' '*(LK-len(Position[i]))}|{Status[i]}{' '*(LK-len(Status[i]))}|')
        table_end()
  
# Menu 4 - Delete Data

def find_data_to_del():
    global list_index
    global del_EmployeeID
    list_index.clear() #hapus hasil sebelumnya
    del_EmployeeID = input(f'Masukan EmployeeID yang ingin dihapus: ').strip()
    
    if len(del_EmployeeID) < 1:
        show_message('Masukan EmployeeID yang ingin dihapus')
        return

    for index in range(len(EmployeeID)):
        if del_EmployeeID == EmployeeID[index]:
            list_index.append(index)
    
    table_header()
    if len(list_index) == 0:
        show_message('Data tidak ditemukan')
    else :
        for i in list_index:
            print(f'|{EmployeeID[i]}{' '*(LK-len(EmployeeID[i]))}|{Name[i]}{' '*(LK-len(Name[i]))}|{Departement[i]}{' '*(LK-len(Departement[i]))}|{Position[i]}{' '*(LK-len(Position[i]))}|{Status[i]}{' '*(LK-len(Status[i]))}|')
    table_end()

# Delete data function
def delete_data():
    global list_index
    del_usr_inp = input(f'Apakah ingin Cek Employee ID data yang akan dihapus?(Y/N) : ')
    if del_usr_inp.upper() in ('Y','N') :
        if del_usr_inp.upper() == 'Y':
            show_all_data()
    
    find_data_to_del()
    print(list_index)
    if len(list_index) == 0:
        return
    
    print(f'\nApakah anda yakin akan menghapus data: {del_EmployeeID}?')
    del_confirm = input(f'Apakah anda yakin (Y/N)? ')
    if del_confirm.upper() == 'Y':
        for i in list_index:
            del EmployeeID[i]
            del Name[i]
            del Departement[i]
            del Position[i]
            del Status[i]
            show_message('Data berhasil dihapus!!!')
    elif del_confirm.upper() == 'N':
            show_message('Data tidak jadi dihapus')
            
# Main Menu Function

def main_menu():
      
    print(f''' 
      Main Menu Data Karyawan PT. Inovasi Sejahtera Abadi
      {'='*60}
      Untuk Melihat Data Karyawan{'.'*(60-42)}Masukan angka 1
      Untuk Membuat Data Karyawan Baru{'.'*(60-47)}Masukan angka 2
      Untuk Merubah Data Karyawan{'.'*(60-42)}Masukan angka 3
      Untuk Menghapus Data Karyawan{'.'*(60-44)}Masukan angka 4
      Untuk Exit Program{'.'*(60-33)}Masukan angka 5
      {'='*60}
      ''')

    try:
        usr_option0 = int(input(f'Masukan Pilihan Main Menu yang diinginkan: '))
        print(f'Main Menu yang dipilih: {usr_option0}')
    
        if usr_option0 == 1:
            clear_screen()
            sub_menu1()
        elif usr_option0 == 2:
            clear_screen()
            sub_menu2()
        elif usr_option0 == 3:
            clear_screen()
            sub_menu3()
        elif usr_option0 == 4:
            clear_screen()
            sub_menu4()
        elif usr_option0 == 5:
            exit_menu()
        else:
            show_message('Masukan Pilihan Sub-Menu yang benar!!!')
            main_menu()
    except:
        show_message('Masukan Pilihan Sub-Menu yang benar!!!')
        main_menu()
       
def sub_menu1():
    print(f''' 
      Sub-Menu Melihat Data Karyawan PT. Inovasi Sejahtera
      {'='*60}
      Untuk Melihat Semua Data Karyawan{'.'*(60-48)}Masukan angka 1
      Untuk Melihat Data Karyawan{'.'*(60-42)}Masukan angka 2
      Untuk Kembali ke Menu Utama{'.'*(60-42)}Masukan angka 3
      {'='*60}
      ''')
    try:
        usr_option1 = int(input(f'Masukan Pilihan Sub-Menu yang diinginkan: '))
        print(f'Sub-Menu yang dipilih: {usr_option1}')
    
        if usr_option1 == 1:
            print('\nSemua Data Karyawan sbb:\n')
            show_all_data()
            sub_menu1()
        elif usr_option1 == 2:
            print('Data Karyawan yang dicari sbb:')
            show_filter_data()
            sub_menu1()
        elif usr_option1 == 3:
            clear_screen()
            main_menu()
        else:
            show_message('Masukan Pilihan Sub-Menu yang benar!!!')
            sub_menu1()
    except:
        show_message('Masukan Pilihan Sub-Menu yang benar!!!')
        sub_menu1()
        
def sub_menu2():
    print(f''' 
      Sub-Menu Membuat Data Karyawan Baru PT. Inovasi Sejahtera
      {'='*60}
      Untuk Membuat Data Karyawan Baru{'.'*(60-47)}Masukan angka 1
      Untuk Kembali ke Menu Utama{'.'*(60-42)}Masukan angka 2
      {'='*60}
      ''')
   
    try:
        usr_option2 = int(input(f'Masukan Pilihan Sub-Menu yang diinginkan: '))
        print(f'Sub-Menu yang dipilih: {usr_option2}')
        
        if usr_option2 == 1:
            create_new_data()
            sub_menu2()
        elif usr_option2 == 2:
            clear_screen()
            main_menu()
        else:
            show_message('Masukan Pilihan Sub-Menu yang benar!!!')
            sub_menu2()
    except:
        show_message('Masukan Pilihan Sub-Menu yang benar!!!')
        sub_menu2()

def sub_menu3():
    print(f''' 
      Sub-Menu Merubah Data Karyawan PT. Inovasi Sejahtera
      {'='*60}
      Untuk Merubah Data Karyawan{'.'*(60-42)}Masukan angka 1
      Untuk Kembali ke Menu Utama{'.'*(60-42)}Masukan angka 2
      {'='*60}
      ''')
    try:
        usr_option3 = int(input(f'Masukan Pilihan Sub-Menu yang diinginkan: '))
        print(f'Sub-Menu yang dipilih: {usr_option3}')
        if usr_option3 == 1:
            print('Modify Data Karyawan')
            update_data()
            sub_menu3()
        elif usr_option3 == 2:
            clear_screen()
            main_menu()
        else:
            show_message('Masukan Pilihan Sub-Menu yang benar!!!')
            sub_menu3()
    except:
        show_message('Masukan Pilihan Sub-Menu yang benar!!!')
        sub_menu3()
        
def sub_menu4():
    print(f''' 
      Sub-Menu Menghapus Data Karyawan PT. Inovasi Sejahtera
      {'='*60}
      Untuk Menghapus Data Karyawan{'.'*(60-44)}Masukan angka 1
      Untuk Kembali ke Menu Utama{'.'*(60-42)}Masukan angka 2
      {'='*60}
      ''')
    try:
        usr_option4 = int(input(f'Masukan Pilihan Sub-Menu yang diinginkan: '))
        print(f'Sub-Menu yang dipilih: {usr_option4}')
        if usr_option4 == 1:
            print('Delete Data Karyawan')
            delete_data()
            sub_menu4()
        elif usr_option4 == 2:
            clear_screen()
            main_menu()
        else:
            show_message('Masukan Pilihan Sub-Menu yang benar!!!')
            sub_menu4()
    except:
        show_message('Masukan Pilihan Sub-Menu yang benar!!!')
        sub_menu4()

def exit_menu():
    clear_screen()
    print('Exit Program')

# Program Start
clear_screen()

try:
    print(f'\nSelamat Datang - Ini adalah Capstone Project Module 1')
    print(f'Data Karyawan PT. Inovasi Sejahtera Abadi')
    print(f'{'-'*len('Selamat Datang - Ini adalah Capstone Project Module 1')}\n')
    main_menu()
except:
    clear_screen()
    print(f'Masukan Pilihan Main Menu yang benar: 1-5 \n')