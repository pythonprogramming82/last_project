 def create_superuser(self, username, password):
        if username in self.superusers:
            return "Username already exists!"
        else:
            self.superusers[username] = password
            return "Superuser created successfully!"
         i