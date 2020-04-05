from datetime import date as dt
import datetime


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = datetime.datetime.strptime(date, '%d.%m.%Y').date() if date else dt.today()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        for record in self.records:
            if record.date == dt.today():
                total += record.amount
        return total

    def get_today_remainder(self):
        return self.limit - self.get_today_stats()

    def get_week_stats(self):
        d = dt.today()
        q = datetime.timedelta
        week = [d, d - q(days=1), d - q(days=2), d - q(days=3), d - q(days=4), d - q(days=5), d - q(days=6),
                d - q(days=7)]
        total = 0
        for record in self.records:
            if record.date in week:
                total += record.amount
        return total


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        rem = self.get_today_remainder()
        if rem > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {rem} кКал'
        else:
            return f'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(80)
    EURO_RATE = float(80)

    def get_today_cash_remained(self, currency):
        rub_rem = self.get_today_remainder()
        usd_rem = self.get_today_remainder() / CashCalculator.USD_RATE
        eur_rem = self.get_today_remainder() / CashCalculator.EURO_RATE

        if currency == 'rub' and rub_rem > 0:
            return f'На сегодня осталось {round(float(rub_rem), 2)} руб'
        elif currency == 'rub' and rub_rem < 0:
            return f'Денег нет, держись: твой долг - {round(float(rub_rem), 2) * -1} руб'
        if currency == 'usd' and usd_rem > 0:
            return f'На сегодня осталось {round(float(usd_rem), 2)} USD'
        elif currency == 'usd' and usd_rem < 0:
            return f'Денег нет, держись: твой долг - {round(float(usd_rem), 2) * -1} USD'
        if currency == 'eur' and eur_rem > 0:
            return f'На сегодня осталось {round(float(eur_rem), 2)} Euro'
        elif currency == 'eur' and eur_rem < 0:
            return f'Денег нет, держись: твой долг - {round(float(eur_rem), 2) * -1} Euro'
        else:
            return f"Денег нет, держись"
