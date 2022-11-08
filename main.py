class Route:

    def __init__(self, count_stops, distance, price):
        self.count_stops = count_stops
        self.distance = distance
        self.price = price

    def middle_distance(self):
        return self.distance / self.count_stops

    def __add__(self, other):
        count_stops = self.count_stops - other.count_stops
        distance = self.distance - other.distance
        price = self.price - other.price
        return f'Разница в количесве остановок - {count_stops}\n' \
               f'Разница в дистанции - {distance}\n' \
               f'Разница в стоимомти - {price}'


class InCityRoute(Route):

    def __init__(self, count_stops, distance, price):
        super().__init__(count_stops, distance, price)

    def middle_price(self):
        return int(self.price) / int(self.count_stops)


class OutCityRoute(Route):

    def __init__(self, count_stops, distance, price):
        super().__init__(count_stops, distance, price)

    def middle_price(self):
        return int(self.price) / int(self.count_stops)


class InsideCityRoute(Route):

    def __init__(self, count_stops, distance, price):
        super().__init__(count_stops, distance, price)

    def middle_price(self):
        return int(self.price) / int(self.count_stops)

