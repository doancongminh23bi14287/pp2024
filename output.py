import curses

def display_menu(stdscr, menu, current_row):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr("Student Mark Management System\n", curses.A_BOLD)
    for idx, item in enumerate(menu):
        if idx == current_row:
            stdscr.addstr(f"> {item}\n", curses.color_pair(1))
        else:
            stdscr.addstr(f"  {item}\n")
    stdscr.refresh()

def get_key_input(stdscr):
    return stdscr.getch()
