class ToolBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def remove_tool(self, tool):
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    def __init__(self, size="5cm"):
        self.size = size

    def tighten(self, screw):
        screw.tighten()

    def loosen(self, screw):
        screw.loosen()

    def __repr__(self):
        return f"{self.size} screwdriver"


class Hammer:
    def __init__(self, colour="red"):
        self.colour = colour

    def remove(self, nail):
        nail.remove()

    def hammer_in(self, nail):
        nail.nail_in()

    def paint(self, colour):
        self.colour = colour

    def __repr__(self):
        return f"{self.colour} hammer"


class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        return f"Screw tightness = {self.tightness}"


class Nail:
    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        wall_state = "in the wall" if self.in_wall else "out of the wall"
        return f"Nail {wall_state}."


toolbox1 = ToolBox()
screwdriver1 = Screwdriver()
hammer1 = Hammer()
toolbox1.add_tool(screwdriver1)
toolbox1.add_tool(hammer1)
print(toolbox1.tools)
screw1 = Screw()
print(screw1)
screwdriver1.tighten(screw1)
print(screw1)
nail1 = Nail()
print(nail1)
hammer1.hammer_in(nail1)
print(nail1)
