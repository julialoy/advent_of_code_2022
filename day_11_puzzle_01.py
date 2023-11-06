# Advent of Code 2022 Day 11 Puzzle 1
with open('day_11_puzzle_01_input.txt') as f:
    monkey_info = f.read().split('\n\n')


class Monkey:
    def __init__(self, monkey_num, items, operation, operand2, test_val,
                 valid_test_throw, invalid_test_throw):
        self.monkey_num = monkey_num
        self.items = items
        self.human_worry = self.items[0] if len(self.items) > 0 else 0
        self.operand_2_is_worry = True if operand2 == 'old' else False
        self.operand2 = int(operand2) if operand2 != 'old' else self.human_worry
        self.test_val = test_val
        self.is_test = valid_test_throw
        self.is_invalid_test = invalid_test_throw
        self.curr_item = self.items[0] if len(self.items) > 0 else None
        self.operation = operation
        self.times_inspected_items = 0

    def update_human_worry(self, value):
        self.human_worry = value
        if self.operand_2_is_worry:
            self.operand2 = value

    def multiply_op(self):
        self.human_worry = self.human_worry * self.operand2

    def add_op(self):
        self.human_worry = self.human_worry + self.operand2

    def mod_test(self):
        if self.curr_item % self.test_val == 0:
            return True
        return False


monkeys = []
for info_block in monkey_info:
    monk = info_block.split('\n')
    monk_num = int(monk[0].split(' ')[1][0])
    items = monk[1].split(': ')[1].split(', ')
    monk_items = [int(item) for item in items]
    monk_operation = monk[2].split(': ')[1].split(' ')[3]
    monk_operand2 = monk[2].split(': ')[1].split(' ')[4]
    monk_test_val = int(monk[3].split(': ')[1].split(' ')[-1])
    monk_valid_test_val = int(monk[4].split(': ')[1].split(' ')[-1])
    monk_invalid_test_val = int(monk[5].split(': ')[1].split(' ')[-1])
    new_monkey = Monkey(monk_num, monk_items, monk_operation, monk_operand2, monk_test_val, monk_valid_test_val, monk_invalid_test_val)
    monkeys.append(new_monkey)


round_num = 1
while round_num <= 20:
    for m in monkeys:
        while m.items:
            item_to_throw = m.items.pop(0)
            # print(
            #     f"Monkey {m.monkey_num} inspects item with worry level {item_to_throw}")
            m.update_human_worry(item_to_throw)
            m.times_inspected_items += 1
            # print(f"Worry level is now {m.human_worry}")
            if m.operation == '*':
                m.multiply_op()
            else:
                m.add_op()
            # print(f"Worry level is {m.operation} by {m.operand2} = {m.human_worry}")
            m.update_human_worry(int(m.human_worry // 3))
            # print(f"Monkey gets bored with item. Worry level now {m.human_worry}")
            item_to_throw = m.human_worry
            test_result = m.human_worry % m.test_val
            if test_result == 0:
                # print(f"Current worry level is divisible by {m.test_val}")
                monkey_to_receive = m.is_test
            else:
                monkey_to_receive = m.is_invalid_test
                # print(f"Current worry level is not divisible by {m.test_val}")
            # print(f"Throw item with worry level {item_to_throw} to {monkeys[monkey_to_receive].monkey_num}")
            monkeys[monkey_to_receive].items.append(item_to_throw)

    round_num += 1

monkey_activity = []
for monk in monkeys:
    monkey_activity.append(monk.times_inspected_items)

max_active = max(monkey_activity)
monkey_activity.remove(max_active)
second_max = max(monkey_activity)
print(max_active * second_max)

