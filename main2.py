import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name          # Имя питомца
        self.species = species    # Вид (котик или собака)
        self.hunger = 5           # Уровень голода 0 - сыт  10 - очень голоден
        self.energy = 5           # Уровень энергии 0 - устал  10 - полон сил
        self.happiness = 5        # Уровень счастья 0 - грустит  10 - очень счастлив
        self.health = 10          # Уровень здоровья 0 - больной  10 - здоров

    def status(self):
        """Вывод состояния питомца."""
        print(f"{self.name}'s статус:")
        print(f"  - Уровень голода: {self.hunger}/10")
        print(f"  - Энергия: {self.energy}/10")
        print(f"  - Счастье: {self.happiness}/10")
        print(f"  - Здоровье: {self.health}/10")
        print()

    def feed(self):
        """Покормить питомца, уменьшает голод."""
        if self.hunger > 0:
            self.hunger -= 1
            self.happiness += 1
            print(f"{self.name} поел и теперь менее голоден!")
        else:
            print(f"{self.name} не голоден.")
        self.status()

    def play(self):
        """Поиграть с питомцем, увеличивает счастье и уменьшает энергию."""
        if self.energy > 1:
            self.energy -= 2
            self.happiness += 2
            print(f"{self.name} рад поиграть!")
        else:
            print(f"{self.name} слишком устал, чтобы играть.")
        self.status()

    def sleep(self):
        """Питомец отдыхает, восстанавливает энергию."""
        print(f"{self.name} отдыхает и набирается сил...")
        time.sleep(1)  # Задержка для реалистичности
        self.energy = min(10, self.energy + 4)
        self.hunger += 1
        self.status()

    def visit_vet(self):
        """Посещение ветеринара для восстановления здоровья."""
        print(f"{self.name} отправляется к ветеринару для проверки здоровья.")
        time.sleep(1)  # Задержка для реалистичности
        self.health = min(10, self.health + 3)
        self.happiness -= 1
        self.status()

    def pass_time(self):
        """Проходит некоторое время, питомец становится голоднее и устаёт."""
        print(f"Проходит время...")
        time.sleep(1)
        self.hunger = min(10, self.hunger + 1)
        self.energy = max(0, self.energy - 1)
        self.happiness = max(0, self.happiness - 1 if self.hunger > 7 else self.happiness)
        self.health = max(0, self.health - 1 if self.hunger >= 10 else self.health)
        self.status()


if __name__ == "__main__":
    my_pet = Pet("Барсик", "котик")
    my_pet.status()


    my_pet.feed()
    my_pet.play()
    my_pet.sleep()
    my_pet.visit_vet()
    my_pet.pass_time()
