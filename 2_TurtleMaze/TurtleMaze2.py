import turtle

# Constants for maze characters
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self, maze_file_name):
        self.maze_list = []
        with open(maze_file_name, 'r') as maze_file:
            lines = [line.rstrip() for line in maze_file]  # Remove trailing spaces/newlines
        
        # Ensure all rows have the same width
        max_columns = max(len(line) for line in lines)
        self.rows_in_maze = len(lines)
        self.columns_in_maze = max_columns

        for row, line in enumerate(lines):
            row_list = list(line.ljust(max_columns))  # Make all rows equal length
            self.maze_list.append(row_list)

            # Find the start position (S)
            if 'S' in row_list:
                self.start_row = row
                self.start_col = row_list.index('S')

        # Turtle settings
        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(self.columns_in_maze - 1) / 2 - 0.5,
                                    -(self.rows_in_maze - 1) / 2 - 0.5,
                                    (self.columns_in_maze - 1) / 2 + 0.5,
                                    (self.rows_in_maze - 1) / 2 + 0.5)

    def draw_maze(self):
        """ Draws the maze based on the text file input. """
        self.t.speed(10)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, 'tan')

        self.t.color('black')
        self.t.fillcolor('blue')

    def draw_centered_box(self, x, y, color):
        """ Draws a colored box to represent obstacles. """
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        """ Moves the turtle to the specified (x, y) coordinate. """
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        """ Marks the current position with a dot of a specified color. """
        self.t.dot(10, color)

    def update_position(self, row, col, val=None):
        """ Updates the maze state and visually marks the path. """
        if val:
            self.maze_list[row][col] = val
            self.move_turtle(col, row)

        color_map = {
            PART_OF_PATH: 'green',
            OBSTACLE: 'red',
            TRIED: 'black',
            DEAD_END: 'red'
        }
        if val in color_map:
            self.drop_bread_crumb(color_map[val])

    def is_exit(self, row, col):
        """ Checks if the current position is an exit. """
        return row == 0 or row == self.rows_in_maze - 1 or col == 0 or col == self.columns_in_maze - 1

    def __getitem__(self, idx):
        return self.maze_list[idx]

def search_from(maze, start_row, start_column):
    """ Recursively searches for a way out of the maze. """
    maze.update_position(start_row, start_column)

    # Base cases
    if maze[start_row][start_column] == OBSTACLE:
        return False

    if maze[start_row][start_column] in (TRIED, DEAD_END):
        return False

    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    # Mark current square as tried
    maze.update_position(start_row, start_column, TRIED)

    # Try all four directions (Up, Down, Left, Right)
    found = (
        search_from(maze, start_row - 1, start_column) or
        search_from(maze, start_row + 1, start_column) or
        search_from(maze, start_row, start_column - 1) or
        search_from(maze, start_row, start_column + 1)
    )

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)

    return found

# Load the maze and solve it
my_maze = Maze("maze2.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)

# Keep the window open
turtle.done()