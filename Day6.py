from Point import Point

player = "^>v<"

guard_moves = {
    "^": Point(0, -1),
    "v": Point(0, 1),
    "<": Point(-1, 0),
    ">": Point(1, 0),
}


class Map:
    def __init__(self, map):
        self.map = map
        self.map_size = len(self.map)

    def find_guard_position(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[0])):
                if self.map[i][j] in player:
                    return Point(j, i), player.find(self.map[i][j])
        return None

    def print_map(self):
        for y in self.map:
            for x in y:
                print(x, end="")
            print()
        print("")

    def get(self, x, y):
        return self.map[y][x]

    def try_move_guard_forward(self, guard):
        point_to_go = guard.get_current_position() + guard.get_next_move()
        # print(guard.get_current_position(), guard.get_next_move(), point_to_go)
        if not point_to_go.is_out_of_bounds(0, self.map_size-1):
            if self.map[point_to_go.y][point_to_go.x] in ".X":
                old_position = guard.get_current_position()
                self.map[old_position.y][old_position.x] = "X"
                guard.move_to(point_to_go)
                self.map[point_to_go.y][point_to_go.x] = guard.rotate_pos
            else:
                guard.rotate()
            return True
        else:
            old_position = guard.get_current_position()
            self.map[old_position.y][old_position.x] = "X"
            return False

    def move_guard_until_blocked(self, guard):
        while self.try_move_guard_forward(guard):
            pass

    def count_X(self):
        counter_X = 0
        for y in self.map:
            for x in y:
                if x == "X":
                    counter_X += 1
        return counter_X


class Guard:
    def __init__(self, position: Point, rotate_pos):
        self.current_position = position
        self.rotate_pos = rotate_pos

    def get_current_position(self):
        return self.current_position

    def print_position(self):
        print("Guard position: ", self.get_current_position())

    def get_next_move(self):
        return guard_moves[self.rotate_pos]

    def move_forward(self):
        point_go_to = self.get_next_move()
        self.current_position.move(point_go_to.x, point_go_to.y)

    def move_to(self, new_position):
        self.current_position = new_position

    def get_next_rotate(self):
        return player[(player.find(self.rotate_pos) + 1) % 4]

    def rotate(self):
        self.rotate_pos = self.get_next_rotate()


if __name__ == "__main__":
    map_init = []
    with open("data/example.txt") as f:
        for line in f:
            map_init.append([x for x in line.strip()])

    map = Map(map_init)

    temp_point, temp_rotate = map.find_guard_position()
    guard = Guard(temp_point, player[temp_rotate])

    map.move_guard_until_blocked(guard)

    counter_X = map.count_X()
    print(f"The guard will visit {counter_X} distinct positions on your map")
