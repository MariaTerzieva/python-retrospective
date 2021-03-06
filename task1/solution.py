SIGNS = [{20: ('Козирог', 'Водолей')},
         {19: ('Водолей', 'Риби')},
         {21: ('Риби', 'Овен')},
         {21: ('Овен', 'Телец')},
         {21: ('Телец', 'Близнаци')},
         {21: ('Близнаци', 'Рак')},
         {22: ('Рак', 'Лъв')},
         {23: ('Лъв', 'Дева')},
         {23: ('Дева', 'Везни')},
         {23: ('Везни', 'Скорпион')},
         {22: ('Скорпион', 'Стрелец')},
         {22: ('Стрелец', 'Козирог')}]


def what_is_my_sign(day, month):
    for key, signs_tuple in SIGNS[month - 1].items():
        return signs_tuple[day >= key]
