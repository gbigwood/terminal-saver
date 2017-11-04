import curses
from curses import wrapper
import random
import time
import string

def main(stdscr):

    # Clear screen
    hiragana = ''.join(chr(i) for i in range(0x3040, 0x30a0))
    katakana = ''.join(chr(i) for i in range(0x30a0, 0x3100))
    latin_1_supplement = ''.join(chr(i) for i in range(0x00c0, 0x0100))
    chars_to_use = string.digits+ string.ascii_letters + string.punctuation+ latin_1_supplement # + hiragana + katakana
    #chars_to_use = string.hexdigits
    def fill_screen():
        for y_pos in range(1, curses.LINES-1):
            for x_pos in range(1, curses.COLS-1):
                if x_pos %3 != 0:
                    stdscr.addch(y_pos, x_pos, random.choice(chars_to_use))
        stdscr.refresh()

    def normalize_characters(normalisation_chance = 0.001):
        for y_pos in range(1, curses.LINES-1):
            for x_pos in range(1, curses.COLS-1):
                if normalisation_chance == 1 or random.random() < normalisation_chance:
                    stdscr.chgat(y_pos, x_pos, 1, curses.A_NORMAL)
        stdscr.refresh()

    def age_characters():
        num_chars_to_update = round(curses.LINES * curses.COLS * 0.1)
        for i in range(num_chars_to_update):
            y_pos = random.randint(1, curses.LINES-2)
            x_pos = random.randint(1, curses.COLS-2)
            if (x_pos %3 != 0):
                ch_got = stdscr.inch(y_pos, x_pos)
                attrs = ch_got & curses.A_ATTRIBUTES

                if bool(attrs & curses.A_REVERSE):
                    attr_to_set = curses.A_BOLD
                elif bool(attrs & curses.A_BOLD):
                    attr_to_set = curses.A_UNDERLINE
                elif bool(attrs & curses.A_UNDERLINE):
                    attr_to_set = curses.A_NORMAL
                elif bool(attrs & curses.A_NORMAL):
                    attr_to_set = curses.A_DIM
                else:
                    attr_to_set = curses.A_DIM
                stdscr.chgat(y_pos, x_pos, 1, attr_to_set)
        stdscr.refresh()

    def periodic_update():
        num_chars_to_update = round(curses.LINES * curses.COLS * 0.02)
        for i in range(num_chars_to_update):
            y_pos = random.randint(1, curses.LINES-2)
            x_pos = random.randint(1, curses.COLS-2)
            if x_pos %3 != 0:
                stdscr.addch(
                        y_pos,
                        x_pos,
                        random.choice(chars_to_use),
                        random.choice([
                            curses.A_NORMAL,
                            curses.A_BOLD,
                            curses.A_DIM,
                            curses.A_REVERSE,
                            curses.A_UNDERLINE,
                            ]))
        stdscr.refresh()

    stdscr.clear()
    fill_screen()
    while True:
        age_characters()
        periodic_update()
        time.sleep(0.1)
        # normalize_characters()

    stdscr.getkey() # wait for user input

wrapper(main)
