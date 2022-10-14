from typing import Dict, List
from points_scaler import PointsScaler

class LSystem:
    def __init__(self, atom, rotation, axiom, starting_direction, starting_point):
        self.atom = atom
        self.rotation = rotation
        self.axiom = axiom
        self.starting_direction = starting_direction
        self.starting_point = starting_point

    def set_drawer(self, drawer):
        self.drawer = drawer
        self.update_drawer()

    def set_points_scaler(self, screen_width, screen_height):
        self.points_scaler = PointsScaler(screen_width, screen_height)

    def update_drawer(self):
        self.drawer.set_direction(self.starting_direction)
        self.drawer.set_starting_point(self.starting_point[0], self.starting_point[1])

    def set_rules(self, rules: Dict[str, List[str]]):
        self.rules = rules

    def draw(self, generation):
        actions = self.get_actions(generation)
        for action in actions:
            self.process_action(action)
        self.draw_scaled()

    def process_action(self, action):
        if action == self.atom:
            self.drawer.step()
        elif action == "+":
            self.drawer.rotate(self.rotation)
        elif action == "-":
            self.drawer.rotate(-self.rotation)
        else:
            print("do nothing")

    def get_actions(self, generation: int):
        actions = [self.axiom]
        if generation != 0:
            actions = self.get_actions_for_gen(actions, generation)
        return actions

    def get_actions_for_gen(self, actions: List[str], generation: int):
        while generation > 0:
            new_actions = []
            for action in actions:
                if LSystem.is_recursive_action(action) and (action in self.rules.keys()):
                    for new_gen_action in self.rules[action]:
                        new_actions.append(new_gen_action)
                else:
                    new_actions.append(action)
            actions = new_actions
            generation -= 1
        return new_actions
        
    def is_recursive_action(action):
        if action == "+" or action == "-":
            return False
        if action == "@":
            return False
        if action == "[" or action == "]":
            return False
        return True
        
    def draw_scaled(self):
        self.points_scaler.scale_points(self.drawer)
        self.drawer.draw_from_points()
