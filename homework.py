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


class CashCalculator(Calculator):
    USD_RATE = float(70)
    EURO_RATE = float(80)

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            remainder = self.get_today_remainder()
            currency = 'руб'
        elif currency == 'usd':
            remainder = self.get_today_remainder() / CashCalculator.USD_RATE
            currency = 'USD'
        else:
            remainder = self.get_today_remainder() / CashCalculator.EURO_RATE
            currency = 'Euro'

        if remainder > 0:
            return f'На сегодня осталось {round(float(remainder), 2)} ' \
                   f'{currency}'
        elif remainder < 0:
            return f'Денег нет, держись: твой долг - ' \
                   f'{abs(round(float(remainder), 2))} {currency}'
        else:
            return 'Денег нет, держись'




