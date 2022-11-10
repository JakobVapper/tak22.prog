import random

kasutaja = input("Sisesta valik(kivi, paber, käärid): ")
possible_actions = ["kivi", "paber", "käärid"]
arvuti = random.choice(possible_actions)
print(f"\nSina valisid {kasutaja}, arvuti valis {arvuti}.\n")

if kasutaja == arvuti:
    print(f"Mõlemad valisid {kasutaja}. Viik!")
elif kasutaja == "kivi":
    if arvuti == "käärid":
        print("Sina võidad!")
    else:
        print("Sina kaotad.")
elif kasutaja == "paber":
    if arvuti == "käärid":
        print("Sina võidad!")
    else:
        print("Sina kaotad.")
elif kasutaja == "käärid":
    if arvuti == "paber":
        print("Sina võidad!")
    else:
        print("Sina kaotad.")