# enpotasyon de kelke fonksyon
import pickle
import random

# kreye yon epsedo
while True:
        epsedo = input("Bonjou, antre yon epsedo stp : ")
        if ' ' in epsedo:
            print("Ere, epsedo a pa dwe gen espas")
        elif epsedo.isnumeric():
            print("Ere, epsedo a pa dwe nimerik")
        elif any(char.isupper() for char in epsedo):
            print("Ere, epsedo a pa dwe gen majiskil")
        else:
            print( F"            ***Byenvini {epsedo}, nan jwet LAWOULET***            ")
            break

#Chwa aleatwa odinate a
enteval = random.randint(10, 200)

#Ouvri baz de done an (mod lekti)
try:
     with open('baz_Done.pkl', 'rb') as fichier:
                baz_Done = pickle.load(fichier)
except (FileNotFoundError,EOFError):
            baz_Done = {}  # Kreyasyon de yon baz de done vid

# deklarasyon kek varyab
kantiteChans = 5
total_sko=baz_Done.get(epsedo,0)

# Mesaj pou itilizate a chwazi yon nonb nan enteval [10-200]
while kantiteChans > 0:
        chwa_nonb = input("Chwazi yon nonb ant [10-200] : ")
        nonb = int(chwa_nonb)

        if nonb < 10 or nonb > 200:
            print("Ere, nonb ou rentre a dwe nan enteval 10 a 200.")
            continue

# Si nonb itilizate a pi piti
        if nonb < enteval:
            print(f"Ou pedi ! Nonb ou chwazi an se : {chwa_nonb}. Li pi piti ke nonb sekre an.")
            kantiteChans -= 1
            print(f"Ou rete : {kantiteChans} chans")

# Si nonb itilizate a pi gran
        elif nonb > enteval:
            print(f"Ou pedi ! Nonb ou chwazi an se : {chwa_nonb}. Li pi gran ke nonb sekre an.")
            print(f"enteval la se:{enteval}")
            kantiteChans -= 1
            print(f"Ou rete : {kantiteChans} chans")

# Si itilizate  a gen genyen
        else:
            print("BRAVO, ou genyen")
            total_sko += 30 * kantiteChans
            print(f"Sko ou an se: {total_sko} ")
            enteval = random.randint(10, 200)
                   
# kanpe jwet lan oubyen rejwe
if kantiteChans == 0:
    print(f" Malerezman {epsedo}, ou pa gen chans anko ! Nonb sekre a se: {enteval}")
    baz_Done[epsedo] = total_sko
    with open("baz_Done.pk1", "wb") as fichier:
        pickle.dump(baz_Done, fichier)

    rejwe = {}
    while True:
        kanpe = input(" *** Peze ninpot lot touch pouw rejwe et peze 'K' pou'w kanpe jwet la : ")
        if kanpe == 'K' or kanpe == 'k':
            break
        else:
            enteval = random.randint(10, 200)
            kantiteChans = 5
           

    #if epsedo in baz_Done:
        #print(F"*** Byenvini a nouvo nan jwet LAWOULET la {epsedo}! ***")
        #ansyen_sko = rejwe.get(epsedo, 0)

    # ajou de sko an nan baz de done an
    #rejwe[epsedo] = total_sko
    #with open("baz_Done.pk1", "wb") as fichier:
        #pickle.dump(rejwe, fichier)

    #print(f"Sko ou anvan se: {total_sko}")
    #print(f"Sko ou jwenn nan pati sa a se: {total_sko + ansyen_sko}")

               