#Program Mencari ISPU
#Mencari nilai ISPU berdasarkan 7 parameter pencemar udara

#KAMUS
#daftar_parameter: array string
#tabel_ispu: array dari array dari array int dan float 
#parameter_dihitung: array string
#konsentrasi_parameter, nilai_ispu_parameter: array bil. rill
#input_parameter: string
#konsentrasi: bil. rill
#nilai_ispu, nilai_ispu_acuan: int
#indeks, indeks_parameter, indeks_batas, indeks_acuan : int
#batas: array bil. rill
#konsentrasi_true, batas_ditemukan: bool
#kategori: string

#ALGORITMA

daftar_parameter = ["PM10", "PM2.5", "SO2", "CO", "O3", "NO2", "HC"]

#Format tabel = [Xb, Xa, Ib, Ia]
tabel_ispu = [[[0, 50, 0, 50], [51, 150, 51, 100], [151, 350, 101, 200], [351, 420, 201, 300], [421, 500, 301, 500]], #kolom PM10
               
               [[0, 15.5, 0, 50], [15.6, 55.4, 51, 100], [55.5, 150.4, 101, 200], [150.5, 250.4, 201, 300], [250.5, 500, 301, 500]], #kolom PM2.5
               
               [[0, 52, 0, 50], [53, 180, 51, 100], [181, 400, 101, 200], [401, 800, 201, 300], [801, 1200, 301,500]], #kolom SO2
               
               [[0, 4000, 0, 50], [4001,8000, 51, 100], [8001, 15000, 101, 200], [15001, 30000, 201, 300], [30001, 45000, 301, 500]], #kolom CO
               
               [[0, 120, 0, 50], [121, 235, 51, 100], [236, 400, 101, 200], [401, 800, 201, 300], [801, 1000, 301, 500]], #kolom O3
               
               [[0, 80, 0, 50], [81, 200, 51, 100], [201, 1130, 101, 200], [1131, 2260, 201, 300], [2261, 3000, 301, 500]], #kolom NO2
               
               [[0, 45, 0, 50], [46, 100, 51, 100], [101, 215, 101, 200], [216, 432, 201, 300], [433, 648, 301, 500]] #kolom HC
               ]

#Penyimpanan sementara hasil setiap parameter yang diukur
parameter_dihitung = [] #7 pararameter
konsentrasi_parameter = [] #nilai konsentrasi parameter pencemar
nilai_ispu_parameter = [] #ispu setiap parameter

#perhitungan ispu setiap parameter
while len(parameter_dihitung) < 7:
    print('\nParameter yang belum dihitung:\n')
    indeks = 0
    #parameter yang belum dihitung
    while indeks < 7:
        if daftar_parameter[indeks] not in parameter_dihitung:
            print(daftar_parameter[indeks])
        
        indeks = indeks + 1
    #penginputan parameter
    input_parameter = input('Masukkan parameter yang ingin diukur: ')
    indeks_parameter = 0 #mencari indeks parameter dari daftar_parameter
    while indeks_parameter < 7 and daftar_parameter[indeks_parameter] != input_parameter:
        indeks_parameter = indeks_parameter + 1

    #cek apakah parameter di dalam daftar_parameter
    if indeks_parameter == 7:
        print('\nParameter tidak dikenal.\n' \
                'Silakan ulangi penginputan parameter\n')
        
    #cek apabila input parameter dimasukkan 2x
    elif input_parameter in parameter_dihitung:
        print('\nParameter tersebut sudah dihitung.\n' \
                'Silakan ulangi penginputan parameter\n')
    else:
        #mencari input sesuai
        konsentrasi_true = False
        while konsentrasi_true == False:
            konsentrasi = float(input(f'Masukkan konsentrasi {input_parameter} (μ/m3 ): '))
            #nilai konsentrasi tidak sama dengan nol
            if konsentrasi < 0:
                print('\nKonsentrasi tidak boleh negatif.')
            else:
                indeks_batas = 0
                batas_ditemukan = False

                #mencari rentang konsentrasi yang sesuai berdasarkan input parameter
                while indeks_batas < 5 and batas_ditemukan == False:
                    batas = tabel_ispu[indeks_parameter][indeks_batas]
                    if batas[0] <= konsentrasi and konsentrasi <= batas[1]:
                        #rumus matematis mencari ispu
                        nilai_ispu = ((batas[3] - batas[2]) / (batas[1] - batas[0])) * (konsentrasi - batas[0]) + batas[2]
                        nilai_ispu = int(nilai_ispu + 0.5) #pembulatan nilai ispu
                        batas_ditemukan = True
                    else:
                        indeks_batas = indeks_batas + 1
                #penyimpanan hasil rentang pada array sebelumnya
                if batas_ditemukan == True:
                    parameter_dihitung.append(input_parameter)
                    konsentrasi_parameter.append(konsentrasi)
                    nilai_ispu_parameter.append(nilai_ispu)
                    konsentrasi_true = True
                else:
                    print('\nKonsentrasi di luar rentang nilai\n' \
                    'Silakan ulangi penginputan nilai konsentrasi.\n')

#Mencari parameter pencemar kritis
indeks_dominan = 0
indeks = 1
while indeks < 7:
    if nilai_ispu_parameter[indeks] > nilai_ispu_parameter[indeks_dominan]:
        indeks_dominan = indeks
    
    indeks = indeks + 1

nilai_ispu_resmi = nilai_ispu_parameter[indeks_dominan]

#penentuan kategori kualitas udara
if nilai_ispu_resmi <= 50:
    kategori = 'Baik'
elif nilai_ispu_resmi <= 100:
    kategori = 'Sedang'
elif nilai_ispu_resmi <=200:
    kategori = 'Tidak Sehat'
elif nilai_ispu_resmi <= 300:
    kategori = 'Sangat Tidak Sehat'
else:
    kategori = 'Berbahaya'

#hasil akhir
print('\n\nHasil Perhitungan ISPU:\n')
print(f'ISPU: {nilai_ispu_resmi}')
print(f'Parameter pencemar kritis: {parameter_dihitung[indeks_dominan]}')
print(f'Kategori kualitas udara: {kategori}')