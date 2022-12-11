'''
- cls
    클래스 변수
    클래스를 기반으로 만든 모든 인스턴스가 공유할 수 있는 변수
    클래스 정의문 바로 아래 대입된 변수
    클래스 객채로 부터 참고 가능
    인스턴스 객체로 부터 참고 가능
    변경 - 모든 모든 인스턴스가 변경



    인스턴스변수
    그 인스턴스만 사용하는 값
    함수 정의문 바로 아래 대입된 self의 속성 변수
    클래스 객채로 부터 참고 불가능
    인스턴스 객체로 부터 참고 가능
    변경- 그 해당 인스턴스의 속성만 변경

    클래스메소드
    인스턴스가 없어도 클래스를 이용해 호출 할 수 있으며
    cls를 이용해 클래스 변수를 사용할 수 있다
'''

class Bag:
    count = 0 # 클래스 변수

    def __init__(self):
        Bag.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def remain_bag(cls):
        return cls.count

    @staticmethod
    def slogan():
        print("명품 주인을 찾습니다")


print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()

print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1.sell()
bag3.sell()

print('현재 가방: {}개'.format(Bag.remain_bag()))

Bag.slogan()







