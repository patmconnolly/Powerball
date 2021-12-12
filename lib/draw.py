class pull:
    def __init__(self, Month, Day, Year, White1, White2, White3, White4, White5, Powerball, PowerPlay=1):
        self.White1 = White1
        self.White2 = White2
        self.White3 = White3
        self.White4 = White4
        self.White5 = White5
        self.Powerball = Powerball
        return None

    def white(self):
        return [self.White1, self.White2, self.White3, self.White4, self.White5]
    
    def powerball(self):
        return int(self.Powerball)