from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin N0.1", 20, 3)
    enemy2 = Character("Goblin No.2", 20, 3)

    enemies = [enemy1, enemy2]

    for enemy in enemies:
        print(f"{hero.name} fighting with {enemy.name}")
        print(hero)
        print(enemy)
        print()

        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            print(hero)
            print(enemy)
            print()

        if not hero.is_alive():
            break

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy1.name} and {enemy2.name} wins!")

if __name__ == "__main__":
    main()