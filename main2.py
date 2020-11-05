from main1 import Handbook


class Check:
    aaa = Handbook('Справочник')
    print(aaa.name)
    aaa.registration_person('Никита', 'Самсоненков', '123', 'Екатеринбург', 'nikitka123@gmail.com')
    aaa.handbook[0].data_print()
    pers = aaa.data_change()
    pers.data_print()
