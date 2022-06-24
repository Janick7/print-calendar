
def date_to_days(y, m, d):
    """A Gergely-naptár szerinti időszámítás nulladik napjától a paraméterben megadott dátumig visszaadja a napok számát.
    Returns the number of days from the zero day of the Gregorian calendar to the date specified in the parameter."""
    m = (m + 9) % 12
    y = y - m // 10
    return 365 * y + y // 4 - y // 100 + y // 400 + (m * 306 + 5) // 10 + d - 1

def days_of_month(y, m):
    """A hónapokhoz tartozó napok számát adja vissza. Februárban figyelembe veszi a szökőéveket is.
    Returns the number of days in the month. In February, the leap years are also taken into account."""
    dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    feb = 28
    if y % 4 == 0:
        feb = 29
        if y % 100 == 0:
            feb = 28
            if y % 400 == 0:
                feb = 29
    dom[1] = feb
    return dom[m % 12]


class Month:

    # header_week = 'hétf kedd szer csüt pént szom vasn'
    # header_week = 'hét ked sze csü pén szo vas'
    header_week = 'hé ke sz cs pé sz va'
    fam_day = '1848-03-15, 2' # A 19. századi magyar forradalom, mint minden menő projekt, a hét közepén, szerdán kedődött. The 19th century Hungarian revolution, like all cool projects, began on Wednesday in the middle of the week.
    months = [
        'január', 'február', 'március',
        'április', 'május', 'június',
        'július', 'augusztus', 'szeptember',
        'október', 'november', 'december']

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return self.month_view()

    def month_view(self):
        h = self.lhw()
        days_list = [self.strd(d) for d in self.days_numb()]
        days_str  = (h // 7 + 1) * self.firs_day_ident( )* ' '
        days_str += (h // 7 - 2) * ' '
        days_str += ((h // 7 - 1) * ' ').join(days_list)
        days_str += (h * 6 - len(days_str) + 5) * ' '
        month_str = (str(self.year) + '. ' + self.months[(self.month - 1) % 12]).center(h) + '\n'
        month_str +=(self.header_week) + '\n'
        for i in range(len(days_str) // h + 2):
            month_str += days_str[(h + 1) * i:(h + 1) * (i + 1) - 1] + '\n'
        return month_str

    def strd(self, d):
        """Az egyjegyű napsorszámokat jobbra igazítja.
        Aligns single-digit day numbers to the right."""
        return str(d) if d > 9 else ' ' + str(d)

    def firs_day_ident(self):
        """Megadja a napsorszámokat tartalmazó karakterlánc első sorának behúzását.
        Specifies to indent the first line of the string containing the date numbers."""
        return (date_to_days(self.year, self.month, 1) - self.days_of_fam_day())%7

    def days_numb(self):
        """Az aktuális hónap napsorszámokat tartalmazó listáját adja vissza.
        Returns with the list of date numbers of the current month."""
        return [d for d in range(1, days_of_month(self.year, (self.month - 1) % 12) + 1)]

    @classmethod
    def lhw(cls):
        return len(cls.header_week)

    @classmethod
    def days_of_fam_day(cls):
        datum, weekday = [el for el in cls.fam_day.strip().split(',')]
        y, m, d = [int(el) for el in datum.split('-')]
        return date_to_days(y, m, d) - int(weekday)


class Calendar:

    def __init__(self, year, month=None):
        self.year = year
        self.month = month
        self.col = 4
        self.row = 3
        self.col_gap = 6
        self.months = [Month(year, m) for m in range(self.col * self.row + 1)]

    def __str__(self):
        return self.calendar_view()

    def calendar_view(self):
        if self.month is not None:
            m = Month(self.year, self.month)
            result = str(m)
        else:
            pm = [self.months[i] for i in range(1, self.col * self.row + 1)]
            result = ''
            for r in range(self.row):
                calstr = ['' for _ in range(10)]
                for c in range(self.col):
                    for i in range(10):
                        calstr[i] += str(pm[r * self.col + c]).splitlines()[i] + ' ' * self.col_gap
                for l in calstr:
                    result += l + '\n'
        return '\n\n' + result


if __name__ == '__main__':
    a = Calendar(2020,2)
    print(a)
