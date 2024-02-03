def Record_trip(self,username,source,destination,fare):
    if username in self.users:
        user=self.users[username]
    if user.metro_card:
        metro_card=user.metro_card
        if metro_card.deduct_balance(fare):
            trip=Trip(source,destination,fare)
         

            trip.start_trip()
            trip.end_trip()
                return "Trip recorded successfully!"
    elif:
        return "Insufficient balance on the metro card!"
    elif:
        return "User does not have a metro card!"
    else:
        return "User not found"
print(metro_manager.Record_trip(user1.username,"A","B",5))