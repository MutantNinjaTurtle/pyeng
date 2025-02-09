# -*- coding: utf-8 -*-
"""
Задание 5.1c

Переделать скрипт из задания 5.1b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.
Задание относится только к параметрам устройств, не к самим устройствам.

> Попробуйте набрать неправильное имя параметра  или несуществующий параметр,
> чтобы увидеть какой будет результат. А затем выполняйте задание.

Если выбран существующий параметр, вывести информацию о соответствующем параметре,
указанного устройства.

Пример выполнения скрипта:
$ python task_5_1c.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ips
Такого параметра нет

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

name_sw = input("Введите имя устройства: ")
list_key = tuple(london_co.get(name_sw).keys())
key_sw = input("Введите имя параметра " + str(list_key) + ": ")
print((london_co.get(name_sw)).get(key_sw, "Такого параметра нет"))