class AtmState():

    name = "state"
    allowed = []

    def go_next(self, state):
        if state.name in self.allowed:
            print("Current State: ", self, " switched to: ", state.name)
            self.__class__ = state

        else:
            print("Current State: ", self, " switching to: ",
                  state.name, " not possible!")

    def __str__(self):
        return self.name


class Off(AtmState):

    name = "off"
    allowed = ['on']


class On(AtmState):

    name = "on"
    allowed = ['off']


class ATM():

    def __init__(self):
        self.current = Off()

    def set_state(self, state):
        self.current.go_next(state)


def main():
    atm = ATM()

    atm.set_state(On)
    atm.set_state(Off)
    atm.set_state(Off)


if __name__ == "__main__":
    main()
