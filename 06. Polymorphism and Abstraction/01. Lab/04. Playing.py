def start_playing(obj):
    return obj.play()

class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
start_playing(guitar)
print(guitar.play())

class Children:
    def play(self):
        return "Children are playing"

piano = Children()
start_playing(piano)
print(piano.play())