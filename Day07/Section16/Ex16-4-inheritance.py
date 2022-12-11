'''
- 상속
    어떤 클래스가 가지고 있는 기능을 그대로 물려
    받아 사용할 수 있는 클래스

    상속방법

    class 슈퍼클래스
        본문

    class 서브클래스(슈퍼클래스)
        본문
'''

# 슈퍼 클래스
class coffee:
    def __init__(self, been):
        self.been = been

    def coffee_info(self):
        print('원두 : {}'.format(self.been))

# 서브 클래스
class Espresso(coffee):
    def __init__(self, been, water):
        super().__init__(been)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))


coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()














