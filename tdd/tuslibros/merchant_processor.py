
class MerchantProcessor(object):
    def __init__(self, message_builder=None):
        self._message_builder = message_builder

    @property
    def message_builder(self):
        return self._message_builder

    def debit(self, credit_card, amount):
        return self.message_builder.debit(credit_card, amount)
