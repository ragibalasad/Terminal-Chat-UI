import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

NICKNAME = "@ragibalasad"
msg_list = []


def main(stdscr):
    # Settingup screen
    inp = 0
    y, x = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.nodelay(True)

    # Defining UI theme and color pairs
    # -1 refers to the default system theme color
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(6, curses.COLOR_BLUE, -1)

    CYAN_DEFAULT = curses.color_pair(1)
    MAGENTA_DEFAULT = curses.color_pair(2)
    GREEN_DEFAULT = curses.color_pair(3)
    WHITE_GREEN = curses.color_pair(4)
    WHITE_RED = curses.color_pair(5)
    BLUE_DEFAULT = curses.color_pair(6)

    # Actual UI starts from here
    side_win = curses.newwin(y - 2, 18, 1, 2)
    rectangle(stdscr, 0, 0, y - 1, 20)
    stdscr.addstr(0, 2, f" {NICKNAME} ", CYAN_DEFAULT)

    # Connection status and Commands
    # blinks when connecting, green wehn connectde and red when disconnected
    #side_win.addstr(" Connecting... \n", WHITE_GREEN | curses.A_BLINK | curses.A_STANDOUT)
    #side_win.addstr(" Connected! \n", WHITE_GREEN)
    side_win.addstr("\n Disonnected! \n", WHITE_RED)

    side_win.addstr("\nServer: null\n", MAGENTA_DEFAULT)
    side_win.addstr("\nServer: \n192.168.0.103\n", GREEN_DEFAULT)

    side_win.addstr(7, 2, "\nto connect with a server type: ")
    side_win.addstr("\n$ cn <server_ip>\n", BLUE_DEFAULT)
    side_win.addstr("\nto disconnect: ")
    side_win.addstr("\n$ dsc\n", BLUE_DEFAULT)
    side_win.addstr("\nto exit: ")
    side_win.addstr("$ exit", BLUE_DEFAULT)

    container_win = curses.newwin(y - 5, x - 25, 2, 23)
    rectangle(stdscr, 0, 21, y - 1, x - 2)
    stdscr.addstr(0, 23, f" ChatRoom - Terminal UI ", CYAN_DEFAULT)

    text_win = curses.newwin(1, x - 26, y - 2, 23)
    box = Textbox(text_win)
    rectangle(stdscr, y - 3, 22, y - 1, x - 3)

    while True:
        text_win.clear()
        stdscr.refresh()
        container_win.refresh()
        side_win.refresh()
        box.edit()

        text = f"{NICKNAME}: {box.gather()}"
        cmdchk = text.split()

        try:
            if cmdchk[1] == '$':
                pass
            else:
                msg_list.append(text)
                container_win.clear()
        except:
            pass

        msg_row = 0
        for msg in msg_list[-9:]:
            container_win.addstr(msg_row, 0, msg)
            msg_row += 2

    stdscr.getch()


wrapper(main)