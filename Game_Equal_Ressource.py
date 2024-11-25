import random
import time
import os

cpu_usage = 40
ram_usage = 50
disk_usage = 30

MAX_CPU = 100
MAX_RAM = 100
MAX_DISK = 100

BONUS_THRESHOLD = 5  # Fréquence des bonus en nombre de cycles

def display_resources():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== État des Ressources ===")
    print(f"CPU: {cpu_usage}%")
    print(f"RAM: {ram_usage}%")
    print(f"Disque: {disk_usage}%")
    print("===========================\n")

def generate_task():
    tasks = [
        {"name": "Calcul intensif", "cpu": 20, "ram": 10, "disk": 5},
        {"name": "Téléchargement de fichiers", "cpu": 10, "ram": 5, "disk": 20},
        {"name": "Compression de fichiers", "cpu": 15, "ram": 20, "disk": 10},
        {"name": "Lecture vidéo", "cpu": 10, "ram": 15, "disk": 5},
        {"name": "Sauvegarde", "cpu": 5, "ram": 10, "disk": 25},
    ]
    return random.choice(tasks)

def apply_task(task):
    global cpu_usage, ram_usage, disk_usage
    cpu_usage += task["cpu"]
    ram_usage += task["ram"]
    disk_usage += task["disk"]

def ignore_task():
    global cpu_usage, ram_usage, disk_usage
    cpu_usage -= random.randint(1, 5)
    ram_usage -= random.randint(1, 5)
    disk_usage -= random.randint(1, 5)

def apply_bonus():
    global cpu_usage, ram_usage, disk_usage
    bonus_type = random.choice(["cpu", "ram", "disk"])
    bonus_value = random.randint(5, 15)
    if bonus_type == "cpu":
        cpu_usage = max(0, cpu_usage - bonus_value)
        print(f"BONUS: Réduction de {bonus_value}% sur le CPU !")
    elif bonus_type == "ram":
        ram_usage = max(0, ram_usage - bonus_value)
        print(f"BONUS: Réduction de {bonus_value}% sur la RAM !")
    elif bonus_type == "disk":
        disk_usage = max(0, disk_usage - bonus_value)
        print(f"BONUS: Réduction de {bonus_value}% sur le Disque !")
    time.sleep(2)

def check_limits():
    if cpu_usage > MAX_CPU or ram_usage > MAX_RAM or disk_usage > MAX_DISK:
        return False
    return True

def game_loop():
    global cpu_usage, ram_usage, disk_usage
    score = 0
    cycles = 0

    print("Bienvenue dans le jeu d'optimisation des performances !")
    input("Appuyez sur Entrée pour commencer...")

    while True:
        display_resources()
        task = generate_task()
        print(f"Tâche générée : {task['name']}")
        print(f"Impact - CPU: {task['cpu']}%, RAM: {task['ram']}%, Disque: {task['disk']}%\n")

        print("1. Accomplir la tâche")
        print("2. Ignorer la tâche")
        choice = input("\nVotre choix (1/2) : ")

        if choice == "1":
            apply_task(task)
            score += 1
        elif choice == "2":
            ignore_task()
        else:
            print("Choix invalide. La tâche a été ignorée par défaut.")
            ignore_task()

        cpu_usage = max(0, cpu_usage - random.randint(1, 3))
        ram_usage = max(0, ram_usage - random.randint(1, 3))
        disk_usage = max(0, disk_usage - random.randint(1, 3))

        cycles += 1
        if cycles % BONUS_THRESHOLD == 0:
            apply_bonus()

        if not check_limits():
            display_resources()
            print("\nVous avez dépassé les limites de ressources !")
            print(f"Score final : {score}")
            break

        time.sleep(1)

if __name__ == "__main__":
    game_loop()
