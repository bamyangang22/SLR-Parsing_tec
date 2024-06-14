import sys

slr_table = {
    0: {'vtype': ('s', 4), '$': ('r', 3), 'CODE': ('goto', 1), 'VDECL': ('goto', 2), 'FDECL': ('goto', 3)},
    1: {'$': ('acc', 0)},
    2: {'vtype': ('s', 4), '$': ('r', 3), 'CODE': ('goto', 5), 'VDECL': ('goto', 2), 'FDECL': ('goto', 3)},
    3: {'vtype': ('s', 4), '$': ('r', 3), 'CODE': ('goto', 6), 'VDECL': ('goto', 2), 'FDECL': ('goto', 3)},
    4: {'id': ('s', 7), 'ASSIGN': ('goto', 8)},
    5: {'$': ('r', 1)},
    6: {'$': ('r', 2)},
    7: {'semi': ('s', 9), 'assign': ('s', 11), 'lparen': ('s', 10)},
    8: {'semi': ('s', 12)},
    9: {'vtype': ('r', 4), 'id': ('r', 4), 'rbrace': ('r', 4), 'if': ('r', 4), 'while': ('r', 4), 'return': ('r', 4),
        '$': ('r', 4)},
    10: {'vtype': ('s', 14), 'rparen': ('r', 20), 'ARG': ('goto', 13)},
    11: {'id': ('s', 23), 'literal': ('s', 17), 'character': ('s', 18), 'boolstr': ('s', 19), 'lparen': ('s', 22),
         'num': ('s', 24),
         'RHS': ('goto', 15), 'EXPR': ('goto', 16), 'EXPR1': ('goto', 20), 'EXPR2': ('goto', 21)},
    12: {'vtype': ('r', 5), 'id': ('r', 5), 'rbrace': ('r', 5), 'if': ('r', 5), 'while': ('r', 5), 'return': ('r', 5),
         '$': ('r', 5)},
    13: {'rparen': ('s', 25)},
    14: {'id': ('s', 26)},
    15: {'semi': ('r', 6)},
    16: {'semi': ('r', 7), 'addsub': ('s', 27)},
    17: {'semi': ('r', 8)},
    18: {'semi': ('r', 9)},
    19: {'semi': ('r', 10)},
    20: {'semi': ('r', 12), 'addsub': ('r', 12), 'multdiv': ('s', 28), 'rparen': ('r', 12)},
    21: {'semi': ('r', 14), 'addsub': ('r', 14), 'multdiv': ('r', 14), 'rparen': ('r', 14)},
    22: {'id': ('s', 23), 'lparen': ('s', 22), 'num': ('s', 24), 'EXPR': ('goto', 29), 'EXPR1': ('goto', 20),
         'EXPR2': ('goto', 21)},
    23: {'semi': ('r', 16), 'addsub': ('r', 16), 'multdiv': ('r', 16), 'rparen': ('r', 16)},
    24: {'semi': ('r', 17), 'addsub': ('r', 17), 'multdiv': ('r', 17), 'rparen': ('r', 17)},
    25: {'lbrace': ('s', 30)},
    26: {'rparen': ('r', 22), 'comma': ('s', 32), 'MOREARGS': ('goto', 31)},
    27: {'id': ('s', 23), 'lparen': ('s', 22), 'num': ('s', 24), 'EXPR1': ('goto', 33), 'EXPR2': ('goto', 21)},
    28: {'id': ('s', 23), 'lparen': ('s', 22), 'num': ('s', 24), 'EXPR2': ('goto', 34)},
    29: {'addsub': ('s', 27), 'rparen': ('s', 35)},
    30: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41),
         'return': ('r', 24),
         'VDECL': ('goto', 38), 'ASSIGN': ('goto', 39), 'BLOCK': ('goto', 36), 'STMT': ('goto', 37)},
    31: {'rparen': ('r', 19)},
    32: {'vtype': ('s', 44)},
    33: {'semi': ('r', 11), 'addsub': ('r', 11), 'multdiv': ('s', 28), 'rparen': ('r', 11)},
    34: {'semi': ('r', 13), 'addsub': ('r', 13), 'multdiv': ('r', 13), 'rparen': ('r', 13)},
    35: {'semi': ('r', 15), 'addsub': ('r', 15), 'multdiv': ('r', 15), 'rparen': ('r', 15)},
    36: {'return': ('s', 46), 'RETURN': ('goto', 45)},
    37: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41),
         'return': ('r', 24), 'VDECL': ('goto', 38), 'ASSIGN': ('goto', 39), 'BLOCK': ('goto', 47),
         'STMT': ('goto', 37)},
    38: {'vtype': ('r', 25), 'id': ('r', 25), 'rbrace': ('r', 25), 'if': ('r', 25), 'while': ('r', 25),
         'return': ('r', 25)},
    39: {'semi': ('s', 48)},
    40: {'lparen': ('s', 49)},
    41: {'lparen': ('s', 50)},
    42: {'id': ('s', 51), 'ASSIGN': ('goto', 8)},
    43: {'assign': ('s', 11)},
    44: {'id': ('s', 52)},
    45: {'rbrace': ('s', 53)},
    46: {'id': ('s', 23), 'literal': ('s', 17), 'character': ('s', 18), 'boolstr': ('s', 19), 'lparen': ('s', 22),
         'num': ('s', 24),
         'RHS': ('goto', 54), 'EXPR': ('goto', 16), 'EXPR1': ('goto', 20), 'EXPR2': ('goto', 21)},
    47: {'rbrace': ('r', 23), 'return': ('r', 23)},
    48: {'vtype': ('r', 26), 'id': ('r', 26), 'rbrace': ('r', 26), 'if': ('r', 26), 'while': ('r', 26),
         'return': ('r', 26)},
    49: {'boolstr': ('s', 57), 'COND': ('goto', 55), 'COND1': ('goto', 56)},
    50: {'boolstr': ('s', 57), 'COND': ('goto', 58), 'COND1': ('goto', 56)},
    51: {'semi': ('s', 9), 'assign': ('s', 11), },
    52: {'rparen': ('r', 22), 'comma': ('s', 32), 'MOREARGS': ('goto', 59)},
    53: {'vtype': ('r', 18), '$': ('r', 18)},
    54: {'semi': ('s', 60)},
    55: {'rparen': ('s', 61), 'comp': ('s', 62)},
    56: {'rparen': ('r', 30), 'comp': ('r', 30)},
    57: {'rparen': ('r', 31), 'comp': ('r', 31)},
    58: {'rparen': ('s', 63), 'comp': ('s', 62)},
    59: {'rparen': ('r', 21)},
    60: {'rbrace': ('r', 34)},
    61: {'lbrace': ('s', 64)},
    62: {'boolstr': ('s', 57), 'COND1': ('goto', 65)},
    63: {'lbrace': ('s', 66)},
    64: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41),
         'return': ('r', 24), 'VDECL': ('goto', 38), 'ASSIGN': ('goto', 39), 'BLOCK': ('goto', 67),
         'STMT': ('goto', 37)},
    65: {'rparen': ('r', 29), 'comp': ('r', 29)},
    66: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41),
         'return': ('r', 24), 'VDECL': ('goto', 38), 'ASSIGN': ('goto', 39), 'BLOCK': ('goto', 68),
         'STMT': ('goto', 37)},
    67: {'rbrace': ('s', 69)},
    68: {'rbrace': ('s', 70)},
    69: {'vtype': ('r', 33), 'id': ('r', 33), 'rbrace': ('r', 33), 'if': ('r', 33), 'while': ('r', 33),
         'else': ('s', 72), 'return': ('r', 33), 'ELSE': ('goto', 71)},
    70: {'vtype': ('r', 28), 'id': ('r', 28), 'rbrace': ('r', 28), 'if': ('r', 28), 'while': ('r', 28),
         'return': ('r', 28)},
    71: {'vtype': ('r', 27), 'id': ('r', 27), 'rbrace': ('r', 27), 'if': ('r', 27), 'while': ('r', 27),
         'return': ('r', 27)},
    72: {'lbrace': ('s', 73)},
    73: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41),
         'return': ('r', 24), 'VDECL': ('goto', 38), 'ASSIGN': ('goto', 39),
         'BLOCK': ('goto', 74), 'STMT': ('goto', 37)},
    74: {'rbrace': ('s', 75)},
    75: {'vtype': ('r', 32), 'id': ('r', 32), 'rbrace': ('r', 32), 'if': ('r', 32), 'while': ('r', 32),
         'return': ('r', 32)}
}

terminals = [
    'vtype', 'id', 'semi', 'assign', 'literal', 'character', 'boolstr', 'num',
    'addsub', 'multdiv', 'lparen', 'rparen', 'lbrace', 'rbrace', 'if', 'else', 'while', 'return', 'comp', '$'
]

non_terminals = [
    'CODE', 'VDECL', 'ASSIGN', 'RHS', 'EXPR', 'EXPR1', 'EXPR2', 'FDECL', 'ARG', 'MOREARGS', 'BLOCK', 'STMT', 'COND',
    'COND1', 'ELSE', 'RETURN'
]

productions = [
    ("S'", ['CODE']),
    ('CODE', ['VDECL', 'CODE']),
    ('CODE', ['FDECL', 'CODE']),
    ('CODE', ['']),
    ('VDECL', ['vtype', 'id', 'semi']),
    ('VDECL', ['vtype', 'ASSIGN', 'semi']),
    ('ASSIGN', ['id', 'assign', 'RHS']),
    ('RHS', ['EXPR']),
    ('RHS', ['literal']),
    ('RHS', ['character']),
    ('RHS', ['boolstr']),
    ('EXPR', ['EXPR', 'addsub', 'EXPR1']),
    ('EXPR', ['EXPR1']),
    ('EXPR1', ['EXPR1', 'multdiv', 'EXPR2']),
    ('EXPR1', ['EXPR2']),
    ('EXPR2', ['lparen', 'EXPR', 'rparen']),
    ('EXPR2', ['id']),
    ('EXPR2', ['num']),
    ('FDECL', ['vtype', 'id', 'lparen', 'ARG', 'rparen', 'lbrace', 'BLOCK', 'RETURN', 'rbrace']),
    ('ARG', ['vtype', 'id', 'MOREARGS']),
    ('ARG', ['']),
    ('MOREARGS', ['comma', 'vtype', 'id', 'MOREARGS']),
    ('MOREARGS', ['']),
    ('BLOCK', ['STMT', 'BLOCK']),
    ('BLOCK', ['']),
    ('STMT', ['VDECL']),
    ('STMT', ['ASSIGN', 'semi']),
    ('STMT', ['if', 'lparen', 'COND', 'rparen', 'lbrace', 'BLOCK', 'rbrace', 'ELSE']),
    ('STMT', ['while', 'lparen', 'COND', 'rparen', 'lbrace', 'BLOCK', 'rbrace']),
    ('COND', ['COND', 'comp', 'COND1']),
    ('COND', ['COND1']),
    ('COND1', ['boolstr']),
    ('ELSE', ['else', 'lbrace', 'BLOCK', 'rbrace']),
    ('ELSE', ['']),
    ('RETURN', ['return', 'RHS', 'semi']),
]


# tokenize는 input_s을 토큰으로 바꾸는 함수이다.
def tokenize(input_s):
    tokens = input_s.split()
    return tokens + ['$']


# pre_check는 토큰 중에 형식에 맞지 않는 토큰이 존재하는지 미리 확인하는 함수이다.
def pre_check(tokens):
    for token in tokens:
        if not token in terminals:
            print(f"에러 발생: 토큰 중에 terminal이 아닌 '{token}' 존재 프로그램을 종료합니다.")
            sys.exit(1)


class Node:  # 노드 클래스 선언 (parse tree 저장하기 위함)
    def __init__(self, symbol, children=None):
        self.symbol = symbol
        self.children = children if children else []

    def __str__(self, level=0, is_last=True, prefix=""):
        ret = prefix
        if level > 0:
            ret += "└── " if is_last else "├── "
        ret += repr(self.symbol) + "\n"

        if self.children:
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, child in enumerate(self.children):
                is_last_child = (i == len(self.children) - 1)
                ret += child.__str__(level + 1, is_last_child, new_prefix)
        return ret

    def __repr__(self):
        return self.__str__()


# parsing 시행
def parse(tokens):
    stack = [0]  # token의 state를 저장하는 스택 - 초기값을 1로 둔다
    n_stack = []  # node를 저장하는 스택 ( 결과로 나온 parse tree를 저장할 stack )
    index = 0

    while True:
        state = stack[-1]  # 스택 맨 위에 있는
        token = tokens[index]

        if token not in slr_table[state]:
            print(f"에러 발생: input file에서 {index + 1}번째 위치의 토큰 '{token}'에서 문제 발생")  # input file에서 어느 토큰에서 에러가 발생했는지 출력
            # 위치는 첫 번째 토큰이 1, 두 번째 토큰이 2 ... 순서이다.
            print(
                f"SLR 테이블 상에서 state : {state}, token : '{token}'에 해당하는 Action 존재하지 않음")  # SLR table 상으로 어디에서 에러가 발생했는지 출력
            return False

        action, value = slr_table[state][token]

        if action == 's':  # shift 연산
            stack.append(value)
            n_stack.append(Node(token))
            index += 1
        elif action == 'r':  # reduce 연산
            production = productions[value]
            descendant = production[1]  # descendant는 피생성자에 해당한다
            if descendant != ['']:  # 빈 문자열이 아닌 경우
                children = []  # children 노드들을 저장할 리스트 선 언
                for _ in descendant:  # 피생성자의 토큰 개수만큼 반복문을 시행한다
                    stack.pop()  # 피생성자의 토큰 개수만큼 stack 에서 pop연산을 진행한다.
                    children.append(n_stack.pop())  # 스택에서 나온 토큰들을 children 리스트에 추가해준다.
                children.reverse()  # 자식 노드를 역순으로 해서 원래 순서 맞춘다.
                n_stack.append(Node(production[0], children))
            else:
                n_stack.append(Node(production[0]))  # 빈 문자열인 경우

            cur_state = stack[-1]
            constructor = production[0]  # 생성자 값
            goto_state = slr_table[cur_state][constructor][1]
            stack.append(goto_state)
        elif action == 'acc':  # accept
            print("SLR Parsing 성공 : accepted!")
            if n_stack:
                print("Parse tree 출력:")
                print(n_stack[-1])
            return True


if __name__ == '__main__':
    if len(sys.argv) != 2:  # 명령 줄 인수가 두개가 아닐 경우( 프로그램 실행 입력 형식에 맞지 않는 경우 ) 시스템 종료
        print("프로그램 실행 방법: 터미널에 SLRparser.py input.txt")
        sys.exit(1)

    input_f = sys.argv[1]  # 명령 줄의 두 번쨰 인수 ( <input file> )

    with open(input_f, 'r') as file:
        input_s = file.read().strip()

    tokens = tokenize(input_s)
    pre_check(tokens)
    parse(tokens)