class Car:
    def __init__(self, brand, model, year):
        self.brand = brand    # марка автомобиля
        self.model = model    # модель автомобиля
        self.year = year      # год выпуска
        self.mileage = 0      # пробег (начальное значение 0)

    def drive(self, distance):
        """Увеличивает пробег автомобиля на заданное расстояние."""
        if distance > 0:
            self.mileage += distance
            print(f"Машина проехала {distance} км. Общий пробег: {self.mileage} км.")
        else:
            print("Расстояние должно быть положительным!")

    def get_info(self):
        """Возвращает информацию об автомобиле."""
        return f"{self.brand} {self.model} ({self.year}), пробег: {self.mileage} км"

# Создаем экземпляр класса Car
my_car = Car("Toyota", "Camry", 2020)

# Используем методы класса
print(my_car.get_info())  # Выведет: Toyota Camry (2020), пробег: 0 км

my_car.drive(150)        # Машина проехала 150 км. Общий пробег: 150 км.
my_car.drive(50)         # Машина проехала 50 км. Общий пробег: 200 км.

print(my_car.get_info())  # Выведет: Toyota Camry (2020), пробег: 200 км