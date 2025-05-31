menu = [
    ("今日の刺身定食", "和食", 1200),
    ("あじフライ定食", "和食", 1000),
    ("天ぷらうどん", "和食", 900),
    ("八宝菜定食", "中華", 900),
    ("天津丼", "中華", 1200),
    ("ラーメン", "中華", 700),
    ("カルボナーラ", "洋食", 950),
    ("ミネストローネ", "洋食", 1000),
    ("ビーフステーキ", "洋食", 1400)
]

from collections import deque
import random

class MenuPicker:
    def __init__(self, menu):
        self.menu = menu
        self.history = deque(maxlen=3)

    def pick(self):
        while True:
            choice = random.choice(self.menu)
            if choice not in self.history:
                break
        self.print_history()
        self.history.appendleft(choice)
        return choice
    
    def print_history(self):
        if len(self.history) != 0:
            print("最近の選択:")
        recent = list(enumerate(self.history, start=1))
        recent.reverse()
        for i, v in recent:
            print(f"{i}日前",v[0])

menu_picker = MenuPicker(menu)
print(menu_picker.pick())
print(menu_picker.pick())
print(menu_picker.pick())
print(menu_picker.pick())
print(menu_picker.pick())
print(menu_picker.pick())
print(menu_picker.pick())


   