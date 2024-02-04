class Trip:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.end_time = None
        self.cost = None

    def calculate_cost(self, cost_matrix):
        if self.origin in cost_matrix and self.destination in cost_matrix[self.origin]:
            self.cost = cost_matrix[self.origin][self.destination]
        else:
            raise ValueError(f"No cost found for the trip from {self.origin} to {self.destination}")

    def deactivate(self, end_time):
        self.end_time = end_time


cost_matrix = {
    "a": {"b": 5000, "star_time":10, "end_time":11},
    "b": {"a": 10000, "star_time":10.30, "end_time":11.10},
    "c": {"b": 8000, "star_time":11, "end_time":11.30},
    "d": {"a":20000, "star_time":11.10, "end_time":12},
}

trip = Trip("a", "b")
trip.calculate_cost(cost_matrix)

