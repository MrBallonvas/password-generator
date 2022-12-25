import random

def generate(lenght:int=8, let:bool=True, num:bool=True, symb:bool=True) -> str:
    a = 'A a B  b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z'.split(' ')
    b = '1 2 3 4 5 6 7 8 9 0'.split(' ')
    c = '! @ # $ % & * ( ) _ +'.split(' ')
    d = {'letters': a,
        'numbers':b,
        'symbols':c
    }

    res = ''

    i = lenght
    while i>0:
        e = random.randint(1,3)
        if e == 1:
            if let == True:
                r = random.randint(0,51)
                el = d['letters'][r]
                res += str(el)
            else:
                continue

        if e == 2:
            if num == True:
                r = random.randint(0,8)
                el = d['numbers'][r]
                res += str(el)
            else:
                continue
        
        if e == 3:
            if symb == True:
                r = random.randint(0,10)
                el = d['symbols'][r]
                res += str(el)
            else:
                continue

        i-=1
    
    return res

if __name__ == '__main__':
    a = generate()
    print(a)