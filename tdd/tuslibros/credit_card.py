from datetime import date


class CreditCard(object):
    def __init__(self, expiration_date=date.today()):
        self.expiration_date = expiration_date.strftime('%m%Y')

    def _is_credit_card_expired(self, date_benchmark=date.today()):
        month, year = self.expiration_date[:2], self.expiration_date[2:]
        if (int(year) < int(date_benchmark.year)
            or (int(year) == int(date_benchmark.year)
                and int(month) < int(date_benchmark.month))):
            return True

        return False
