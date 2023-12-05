class Item:
    def __init__(self,worry_level):
        self.worry_level=worry_level


class Monkey:
    Monkeys=list()
    def __init__(self,Op_func,Test_func,id,Initial_queue):
        self.queue=Initial_queue
        self.operation_fn=Op_func
        self.test_fn=Test_func
        self.id=id
        self.operations=0
        

    def operation(self,Monkeys,divprod):
        if len(self.queue)!=0:
            for i in range(len(self.queue)):
                self.queue[0].worry_level=self.operation_fn(self.queue[0].worry_level)
                if self.queue[0].worry_level>divprod:
                    self.queue[0].worry_level=self.queue[0].worry_level%divprod
                dest=self.test()
                self.throw_item(Monkeys[dest])
                self.operations += 1

    def test(self):
        return self.test_fn(self.queue[0].worry_level)

    def throw_item(self,dest_monkey):
        dest_monkey.queue.append(self.queue[0])
        self.queue=self.queue[1:]

Monkeys=list()    

Monkeys.append( Monkey( Op_func=lambda old: old*5,
                        Test_func=lambda new: 4 if new%17==0 else 7,
                        id=0,
                        Initial_queue=[Item(89),Item(74)] ))

Monkeys.append( Monkey( Op_func=lambda old: old+3,
                        Test_func=lambda new: 3 if new%7==0 else 2,
                        id=1,
                        Initial_queue=[Item(75),Item(69),Item(87),Item(57),Item(84),Item(90),Item(66),Item(50)] ))

Monkeys.append( Monkey( Op_func=lambda old: old+7,
                        Test_func=lambda new: 0 if new%13==0 else 7,
                        id=2,
                        Initial_queue=[Item(55)]))

Monkeys.append( Monkey( Op_func=lambda old: old+5,
                        Test_func=lambda new: 0 if new%2==0 else 2,
                        id=3,
                        Initial_queue=[Item(69),Item(82),Item(69),Item(56),Item(68)]))

Monkeys.append( Monkey( Op_func=lambda old: old+2,
                        Test_func=lambda new: 6 if new%19==0 else 5,
                        id=4,
                        Initial_queue=[Item(72),Item(97),Item(50)]))

Monkeys.append( Monkey( Op_func=lambda old: old*19,
                        Test_func=lambda new: 6 if new%3==0 else 1,
                        id=5,
                        Initial_queue=[Item(90),Item(84),Item(56),Item(92),Item(91),Item(91)]))

Monkeys.append( Monkey( Op_func=lambda old: old*old,
                        Test_func=lambda new: 3 if new%5==0 else 1,
                        id=6,
                        Initial_queue=[Item(63),Item(93),Item(55),Item(53)]))

Monkeys.append( Monkey( Op_func=lambda old: old+4,
                        Test_func=lambda new: 5 if new%11==0 else 4,
                        id=7,
                        Initial_queue=[Item(50),Item(61),Item(52),Item(58),Item(86),Item(68),Item(97)]))

test_divisor_product=17*7*13*2*19*3*5*11

for run in range(10000):
    for monkey in Monkeys:
        monkey.operation(Monkeys,test_divisor_product)
    if run%1000==0:
        print(f"{run} complete")

Op_scores=list()
for monkey in Monkeys:
    Op_scores.append(monkey.operations)

print(sorted(Op_scores))