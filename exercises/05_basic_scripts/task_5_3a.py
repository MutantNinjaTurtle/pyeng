# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


template = {"access" : access_template, "trunk" : trunk_template}
quest = {"access" : 'Введите номер VLAN: ', "trunk" : 'Введите разрешенные VLANы: '}

mode_int = input("Введите режим работы интерфейса (access/trunk): ")
type_int = input("Введите тип и номер интерфейса: ")
vlan_list = input(quest[mode_int])

print("interface " + str(type_int))
print("\n".join(template[mode_int]).format(vlan_list))