import random

chance = int(input('Add meg a drop chance-et arányban (pl. "20" ami 1:20 vagyis 5% lesz): '))
mobPerMinute = 20
mobsKilled = 0
percentage = 1 / chance * 100

while True:
    mobsKilled += 1
    rng = random.randint(1, chance)
    if(rng == 1):
        break

print(f"({percentage:.5f}% esély a dropra mobonként)")
minutes = mobsKilled / mobPerMinute
hours = minutes / 60
print(f"\n{mobsKilled} Mobot kellett megölni")
print(f"Ha {mobPerMinute} mob/perc: {minutes} perc volt. ({hours:.2f} óra)")
