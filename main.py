from utils import *
from grid import Grid
from searching_algorithms import *
from button import Button

PANEL_WIDTH = 200
WINDOW_WIDTH = WIDTH + PANEL_WIDTH
WINDOW_HEIGHT = HEIGHT


# Panel background
PANEL_COLOR = (19, 42, 19)      # darkest green

# Standard algorithm buttons
BUTTON_COLOR = (49, 87, 44)    # dark green
BUTTON_HOVER = (79, 119, 45)     # medium green
BUTTON_TEXT_COLOR = (236, 243, 158)  # lightest yellow-green

# Reset button
RESET_COLOR = (144, 169, 85)     # muted pistachio
RESET_HOVER = (236, 243, 158)  # lightest Yellow-Green
RESET_TEXT_COLOR = (19, 42, 19) #darkest green

if __name__ == "__main__":
    pygame.init()
    # setting up how big will be the display window
    WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # set a caption for the window
    pygame.display.set_caption("Path Visualizing Algorithm")

    ROWS = 50  # number of rows
    COLS = 50  # number of columns
    grid = Grid(WIN, ROWS, COLS, WIDTH, HEIGHT)

    start = None
    end = None

    # flags for running the main loop
    run = True
    started = False

    button_y = 20
    button_spacing = 60
    button_width = 180
    button_height = 50

    buttons = []
    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "BFS",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "DFS",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing


    buttons.append(Button(WIDTH + 10, button_y, button_width, button_height, "A* (Manhattan)",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR))
    button_y += button_spacing

    buttons.append(
        Button(WIDTH + 10, button_y, button_width, button_height, "A* (Euclidean)",
               BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR))
    button_y += button_spacing

    buttons.append(
        Button(WIDTH + 10, button_y, button_width, button_height, "UCS",
               BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "DLS",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "IDS",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "Dijkstra",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "Greedy BFS",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    buttons.append(Button(
        WIDTH + 10, button_y, button_width, button_height, "IDA*",
        BUTTON_COLOR, BUTTON_HOVER, BUTTON_TEXT_COLOR
    ))
    button_y += button_spacing

    reset_button = Button(
        WIDTH + 10, WINDOW_HEIGHT - button_height - 20, button_width, button_height,
        "Reset Grid", RESET_COLOR, RESET_HOVER, RESET_TEXT_COLOR
    )
    buttons.append(reset_button)


    def draw_all():
        grid.draw()


        pygame.draw.rect(WIN, PANEL_COLOR, (WIDTH, 0, PANEL_WIDTH, WINDOW_HEIGHT))

        for button in buttons:
            button.draw(WIN)


        pygame.display.update()

    while run:
        draw_all()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                # do not allow any other interaction if the algorithm has started
                continue

            pos = pygame.mouse.get_pos()

            #click inside grid
            if pos[0] < WIDTH:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = grid.get_clicked_pos(pos)

                    if row >= ROWS or row < 0 or col >= COLS or col < 0:
                        continue

                    spot = grid.grid[row][col]

                    if event.button == 1:  # LEFT CLICK (Draw)
                        if not start and spot != end:
                            start = spot
                            start.make_start()
                        elif not end and spot != start:
                            end = spot
                            end.make_end()
                        elif spot != end and spot != start:
                            spot.make_barrier()

                    elif event.button == 3:  # RIGHT CLICK (Erase)
                        spot.reset()
                        if spot == start:
                            start = None
                        elif spot == end:
                            end = None


            else:
                # left clicks for buttons
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    if reset_button.handle_event(event):
                        start = None
                        end = None
                        grid.reset()
                        started = False
                        continue

                    if start and end:
                        for row in grid.grid:
                            for spot in row:
                                spot.update_neighbors(grid.grid)


                        run_lambda = lambda: draw_all()

                        if buttons[0].handle_event(event):  # BFS
                            started = True
                            bfs(run_lambda, grid, start, end)
                            started = False

                        elif buttons[1].handle_event(event):  # DFS
                            started = True
                            dfs(run_lambda, grid, start, end)
                            started = False

                        elif buttons[2].handle_event(event):  # A* manh
                            started = True
                            astar(run_lambda, grid, start, end, h_manhattan_distance)
                            started = False

                        elif buttons[3].handle_event(event):  # A* euclid
                            started = True
                            astar(run_lambda, grid, start, end, h_euclidian_distance)
                            started = False

                        elif buttons[4].handle_event(event):  # UCS
                            started = True
                            ucs(run_lambda, grid, start, end)
                            started = False

                        elif buttons[5].handle_event(event):  # DLS
                            started = True
                            dls(run_lambda, start, end, 30)
                            started = False

                        elif buttons[6].handle_event(event):  # IDS
                            started = True
                            ids(run_lambda, start, end)
                            started = False

                        elif buttons[7].handle_event(event):  # Dijkstra
                            started = True
                            dijkstra(run_lambda, grid, start, end)
                            started = False

                        elif buttons[8].handle_event(event):  # Greedy best fisrt search
                            started = True
                            greedy_best_first_search(run_lambda, grid, start, end)
                            started = False

                        elif buttons[9].handle_event(event):  # IDA
                            started = True
                            ida(run_lambda, grid, start, end)
                            started = False

    pygame.quit()
