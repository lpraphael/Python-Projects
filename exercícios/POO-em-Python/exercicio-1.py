class Refrigerator:
    def __init__(self, color, potency, voltage, price) -> None:
        self.price = price
        self.color = color
        self.potency = potency
        self.voltage = voltage
        self.on = False
        self.current_motor_amperage = 0

        # Getter
        @property
        def color(self):
            return self.__color

        # Setter
        @color.setter
        def color(self, new_color):
            self.color = new_color


blue_refrigerator = Refrigerator('blue', '110', '127', 350)


class Person:
    def __init__(self, name, account_balance) -> None:
        self.name = name
        self.account_balance = account_balance
        self.refrigerator = None

    def buy_refrigerator(self, refrigerator: Refrigerator):
        if refrigerator.price <= self.account_balance:
            self.account_balance -= int(refrigerator.price)
            self.refrigerator = refrigerator

    def __str__(self) -> str:
        return f'''
            {self.name} - has ${self.account_balance} in his account
        '''


cook_person = Person('Gordon Ramsey', 1000)
cook_person.buy_refrigerator(blue_refrigerator)

print(cook_person)
