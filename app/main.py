class Car:
    def __init__(self, clean_mark: int) -> None:
        self.clean_mark = clean_mark


class CarWash:
    def __init__(str, clean_power: int, diamond_price: int, ordinary_price: int) -> None:
        # або поточна ініціалізація, яка у вас вже є для класу CarWash
        pass

    def calculate_washing_price(self, car: Car) -> float:
        # Ваш поточний розрахунок ціни (якщо він вже є)
        pass

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)
