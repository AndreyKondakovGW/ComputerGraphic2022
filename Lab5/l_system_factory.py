from l_system import LSystem

class LSystemFactory:
    def __init__(self, drawer, screen_width, screen_height):
        self.drawer = drawer
        self.screen_width = screen_width
        self.screen_height = screen_height

    def build(self, filename):
        with open(filename, 'r') as f:
            lines = [line[:-1] for line in f.readlines()]
            return self.build_from_lines(lines)

    def build_from_lines(self, lines):
        self.process_heading(lines[0])
        self.axiom = lines[1]
        l_system = LSystem(self.atom, self.rotation, self.axiom, self.starting_direction, self.starting_point)
        rules = LSystemFactory.get_rules(lines[2:])
        l_system.set_rules(rules)
        l_system.set_drawer(self.drawer)
        l_system.set_points_scaler(self.screen_width, self.screen_height)
        return l_system

    def get_rules(lines):
        rules = {}
        for line in lines:
            key, value = LSystemFactory.parse_rule(line)
            rules[key] = value
        return rules

    def process_heading(self, line):
        tokens = line.split(' ')
        self.atom = tokens[0]
        self.rotation = int(tokens[1])
        direction_description = tokens[2]
        self.starting_direction = LSystemFactory.direction_from_description(direction_description)
        #self.starting_point = self.starting_point_from_direction(self.starting_direction)
        self.starting_point = (0, 0)

    def starting_point_from_direction(self, direction):
        x, y = direction
        if abs(x) > 0:
            return (5, self.screen_height // 2)
        elif abs(y) > 0:
            return (self.screen_width // 2, 5)
        else:
            return (5, self.screen_height - 5)

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
            raise ValueError("unknown direction")
        return direction

    def parse_rule(rule_line):
        key, value = rule_line.split("->")
        return (key, value)