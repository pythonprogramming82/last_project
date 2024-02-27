import logging
import functools




class Metro:
    def __init__(self,name):
        self.name=name
        logging.info(f"Created a new metro system: {self.name}")

    def open_gate(self,station):
        logging.info(f"Gate opened at station {station}")
    

    def close_gate(self,station):
        logging.info(f"Gate closed at station {station}")
    

    def run_train(self, train_id, origin, destination):
        logging.info(f"Train {train_id} is running from {origin} to {destination}")


metro_system = Metro("City Metro")
metro_system.open_gate("Station A")
metro_system.run_train(1, "Station A", "Station B")
metro_system.close_gate("Station A")
    
