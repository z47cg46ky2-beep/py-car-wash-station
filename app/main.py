class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center,
        clean_power,
        average_rating,
        count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def can_wash_car(self, car):
        return self.clean_power > car.clean_mark

    def calculate_washing_price(self, car):
        if not self.can_wash_car(car):
            return 0.0
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car):
        if self.can_wash_car(car):
            car.clean_mark = self.clean_power

    def serve_cars(self, cars):
        total_income = 0
        for car in cars:
            if self.can_wash_car(car):
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, mark):
        total = (
            self.average_rating * self.count_of_ratings
            + mark
        )
        self.count_of_ratings += 1
        self.average_rating = round(
            total / self.count_of_ratings,
            1
        )
