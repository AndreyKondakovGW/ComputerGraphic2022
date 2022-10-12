from l_system import LSystem

class LSystemFactory:
    def __init__(self, drawer):
        self.drawer = drawer

    def build(self, filename):
        with open(filename, 'r') as f:
            lines = [line[:-1] for line in f.readlines()]
            print(lines)
            self.process_heading(lines[0])
            self.axiom = lines[1]
            l_system = LSystem(self.atom, self.rotation, self.axiom, self.starting_direction)
            rules = {}
            for line in lines[2:]:
                key, value = LSystemFactory.parse_rule(line)
                rules[key] = value
            l_system.set_rules(rules)
            l_system.set_drawer(self.drawer)
            return l_system

    def process_heading(self, line):
        tokens = line.split(' ')
        self.atom = tokens[0]
        self.rotation = int(tokens[1])
        direction_description = tokens[2]
        self.starting_direction = LSystemFactory.direction_from_description(direction_description)
        if self.starting_direction is None:
            raise ValueError("unknown direction")

    def direction_from_description(description):
        print(description)
        if description == "right":
            direction = (1, 0)
        elif description == "left":
            direction = (-1, 0)
        elif description == "up":
            direction = (0, 1)
        elif description == "down":
            direction = (0, -1)
        else:
            direction = None
        return direction

    def parse_rule(rule_line):
        key, value = rule_line.split("->")
        return (key, value)