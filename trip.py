class Trip:
    def __init__(self, origin, destination, start_time):
        self.origin = origin
        self.destination = destination
        self.start_time = start_time
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
    "a": {"b": 5000, "c": 8000},
    "b": {"a": 5000, "c": 10000},
    "c": {"a": 8000, "b": 10000}
}

trip = Trip("a", "c", "2023-01-01 10:00:00")
trip.calculate_cost(cost_matrix)
trip.end_time("2023-01-01 11:00:00")

print(f"Trip from {trip.origin} to {trip.destination}, star trip: {trip.start_time} until the end trip: {trip.end_time}, cost: {trip.cost}")
