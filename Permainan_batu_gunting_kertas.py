import random

print('PERMAINAN BATU GUNTING KERTAS')
print('1.Batu')
print('2.Gunting')
print('3.Kertas')
print('')

pilihan = int(input('Pilih jagoan anda(1/2/3): '))
musuh = random.choice(['Batu','Gunting','Kertas'])

if pilihan == 1:
    print('Anda     : Batu')
    print('Musuh    :',musuh)
    if musuh == 'Batu':
        print('Hasil seimbang')
    elif musuh == 'Gunting':
        print('Anda menang')
    elif musuh == 'Kertas':
        print('Anda kalah')

elif pilihan == 2:
    print('Anda     : Gunting')
    print('Musuh    :',musuh)
    if musuh == 'Batu':
        print('Anda kalah')
    elif musuh == 'Gunting':
        print('Hasil seimbang')
    elif musuh == 'Kertas':
        print('Anda menang')

elif pilihan == 3:
    print('Anda     : Kertas')
    print('Musuh    :',musuh)
    if musuh == 'Batu':
        print('Anda menang')
    elif musuh == 'Gunting':
        print('Anda kalah')
    elif musuh == 'Kertas':
        print('Hasil seimbang')

else:
    print('Pilihan salah')