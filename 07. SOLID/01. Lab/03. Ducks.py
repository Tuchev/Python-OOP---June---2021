from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class LiveDuck(Duck):
    def eat(self):
        pass


class StatickDuck(Duck):
    def stey_still(self):
        pass


class RubberDuck(StatickDuck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(StatickDuck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
