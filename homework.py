import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date() \
            if date else dt.datetime.today().date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        for record in self.records:
            if record.date == dt.date.today():
                total += record.amount
        return total

    def get_today_remainder(self):
        return self.limit - self.get_today_stats()

    def get_week_stats(self):
        today = dt.datetime.today().date()
        week = dt.timedelta(days=7)
        total = 0
        for record in self.records:
            if (today - record.date) < week:
                total += record.amount
        return total


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        rem = self.get_today_remainder()
        if rem > 0:
            return f'Сегодня можно съесть что-нибудь ещё, ' \
                   f'но с общей калорийностью не более {rem} кКал'
        else:
            return 'Хватит есть!'


def convert(currency):
    if currency == 'rub':
        return 'руб'
    elif currency == 'usd':
        return 'USD'
    else:
        return 'Euro'


class CashCalculator(Calculator):
    USD_RATE = float(80)
    EURO_RATE = float(80)

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            remainder = self.get_today_remainder()
        elif currency == 'usd':
            remainder = self.get_today_remainder() / CashCalculator.USD_RATE
        else:
            remainder = self.get_today_remainder() / CashCalculator.EURO_RATE

        if remainder > 0:
            return f'На сегодня осталось {round(float(remainder), 2)} ' \
                   f'{convert(currency)}'
        elif remainder < 0:
            return f'Денег нет, держись: твой долг - ' \
                   f'{round(float(remainder), 2) * -1} {convert(currency)}'
        else:
            return 'Денег нет, держись'
