class Memory:

    def __init__(self):
        self.history = []

    def add_user(self, text):
        self.history.append({
            "role": "user",
            "content": text
        })

    def add_assistant(self, text):
        self.history.append({
            "role": "assistant",
            "content": text
        })

    def add_preferences(self, info):
        self.preferences.append(info)

    def get_preferences(self)
        return self.preferences
        
    def get_history(self):
        return self.history

    def clear(self):
        self.history = []
