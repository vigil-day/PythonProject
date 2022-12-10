'''

'''

class Calculastor:
    def input_expr(self):
        expr = input('수식을 입력하세요 >>>')
        self.expr = expr


    def calculastor(self):
        return eval(self.expr)

calc = Calculastor()
calc.input_expr()

print('수식결과는 {}입니다'.format(calc.calculastor()))








