import random

user_action = input("Sisesta valik(kivi, paber, käärid): ")
possible_actions = ["kivi", "paber", "käärid"]
computer_action = random.choice(possible_actions)
print(f"\nSina valisid {user_action}, arvuti valis {computer_action}.\n")

if user_action == computer_action:
    print(f"Mõlemad valisid {user_action}. Viik!")
elif user_action == "kivi" and computer_action == "käärid":
    print("Sina võidad!")
elif user_action == "paber" and computer_action == "kivi":
    print("Sina võidad!")
elif user_action == "käärid" and computer_action == "paber":
    print("Sina võidad!")
else:
    print("Sina kaotad.")