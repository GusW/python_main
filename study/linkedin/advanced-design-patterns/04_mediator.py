class Colleague:
    def __init__(self, mediator, id_):
        self._mediator = mediator
        self._id = id_

    def get_id(self):
        return self._id

    def send(self, msg):
        raise NotImplementedError('must be implemented by subclasses')

    def receive(self, msg):
        raise NotImplementedError('must be implemented by subclasses')


class ConcreteColleague(Colleague):
    def __init__(self, mediator, id_):
        super().__init__(mediator, id_)

    def send(self, msg):
        print("Message '" + msg + "' sent by Colleague " + str(self._id))
        self._mediator.distribute(self, msg)

    def receive(self, msg):
        print("Message '" + msg + "' received by Colleague " + str(self._id))


class Mediator:
    def add(self, colleague):
        raise NotImplementedError('must be implemented by subclasses')

    def distribute(self, sender, msg):
        raise NotImplementedError('must be implemented by subclasses')


class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleagues = []

    def add(self, colleague):
        self._colleagues.append(colleague)

    def distribute(self, sender, msg):
        for colleague in self._colleagues:
            if colleague.get_id() != sender.get_id():
                colleague.receive(msg)


def main():
    mediator = ConcreteMediator()

    c1 = ConcreteColleague(mediator, 1)
    c2 = ConcreteColleague(mediator, 2)
    c3 = ConcreteColleague(mediator, 3)

    mediator.add(c1)
    mediator.add(c2)
    mediator.add(c3)

    c1.send("Good Morning!")
    c2.send("Good afternoon!")


if __name__ == "__main__":
    main()
