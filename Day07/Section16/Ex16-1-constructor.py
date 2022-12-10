'''
- 생성자
    인스턴스를 생성할 때 생성자가 자동으로 호출된다.
    객체 초기화 용으로 사용한다.
'''

class USB:
    #생성자
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print("{}GB USB".format(self.capacity))

usb = USB(128)
usb.info()

