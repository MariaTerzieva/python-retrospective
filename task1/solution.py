def what_is_my_sign(day, month):
    signs = {1: ('Козирог', 'Водолей'),
             2: ('Водолей', 'Риби'),
             3: ('Риби', 'Овен'),
             4: ('Овен', 'Телец'),
             5: ('Телец', 'Близнаци'),
             6: ('Близнаци', 'Рак'),
             7: ('Рак', 'Лъв'),
             8: ('Лъв', 'Дева'),
             9: ('Дева', 'Везни'),
             10: ('Везни', 'Скорпион'),
             11: ('Скорпион', 'Стрелец'),
             12: ('Стрелец', 'Козирог')}

    def what_to_return(limit):
        if day < limit:
            return sign_tuple[0]
        else:
            return sign_tuple[1]

    for month_number, sign_tuple in signs.items():
        if month_number == month and month_number in [3, 4, 5, 6]:
            return what_to_return(21)
        elif month_number == month and month_number in [7, 11, 12]:
            return what_to_return(22)
        elif month_number == month and month_number in [8, 9, 10]:
            return what_to_return(23)
        elif month_number == month == 1:
            return what_to_return(20)
        elif month_number == month == 2:
            return what_to_return(19)
