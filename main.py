# Mengqi Li 92059150
# ICS 32

import tkinter
import Othello

DEFAULT_FONT = ('Helvetica', 14)

class settingDialog:
    def __init__(self):
        
        # Default
        self._row = int(4)
        self._col = int(4)
        self._who = 'B'
        self._win = 'M'
        
        self._dialog_window = tkinter.Toplevel()
        
        setting_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Setting',
            font = ('Helvetica', 20))
        setting_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How many rows?\n(even number between 4-16)',
            font = DEFAULT_FONT)
        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = DEFAULT_FONT)
        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        col_label = tkinter.Label(
            master = self._dialog_window,
            text = 'How many columns?\n(even number between 4-16)',
            font = DEFAULT_FONT)
        col_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = DEFAULT_FONT)
        self._col_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        who_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Who goes first?\n(B)lack or (W)hite',
            font = DEFAULT_FONT)
        who_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._who_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = DEFAULT_FONT)
        self._who_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        win_label = tkinter.Label(
            master = self._dialog_window,
            text = 'Choose winning style.\n(M)ost disc or (F)ewest disc',
            font = DEFAULT_FONT)
        win_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._win_entry = tkinter.Entry(
            master = self._dialog_window, width = 20,
            font = DEFAULT_FONT)
        self._win_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK',
            font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def get_row(self) -> int:
        return int(self._row)

    def get_col(self) -> int:
        return int(self._col)
    
    def get_who(self) -> str:
        return self._who

    def get_win(self) -> str:
        return self._win
        
    def _on_ok_button(self) -> None:
        self._row = self._row_entry.get()
        self._col = self._col_entry.get()
        self._who = self._who_entry.get()
        self._win = self._win_entry.get()
        if self._is_valid_number(self._row) and\
           self._is_valid_number(self._col) and\
           (self._who.upper() == 'B' or self._who.upper() == 'W') and\
           (self._win.upper() == 'M' or self._win.upper() == 'F'):
            self._dialog_window.destroy()

    def _is_valid_number(self, num: str) -> bool:
        try:
            if 4 <= int(num) <= 16 and int(num)%2 == 0:
                return True
        except:
            pass
        return False
            

class OthelloGui:
    def __init__(self):
        self._root_window = tkinter.Tk()
        
        dialog = settingDialog()
        dialog.show()
        
        self._row = dialog.get_row()
        self._col = dialog.get_col()
        self._who = dialog.get_who()
        self._win = dialog.get_win()
        
        self._game = Othello.Othello(self._row, self._col, self._who, self._win)
        
        self._score_text = tkinter.StringVar()
        self._score_text.set('Balck: \nWhite:')

        self._canvas = []

        for i in range(self._row):
            canvas_col = []
            for i in range(self._col):
                canvas_col.append(
                    tkinter.Canvas(
                        master = self._root_window,
                        width = 100, height = 100,
                        background = '#324F17'))
            self._canvas.append(canvas_col)
        
        for i in range(self._row):
            for j in range(self._col):
                self._canvas[i][j].grid(
                    row = i, column = j, padx = 0, pady = 0,
                    sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                self._canvas[i][j].bind('<Button-1>', self._on_canvas_clicked)

        score_label = tkinter.Label(
            master = self._root_window, textvariable = self._score_text,
            font = DEFAULT_FONT)
        score_label.grid(
            row = self._row+1, column = 0,
            sticky = tkinter.W)

        self._root_window.bind('<Configure>', self._on_resized)
        
        for i in range(self._row):
            self._root_window.rowconfigure(i, weight = 1)
        for i in range(self._col):
            self._root_window.columnconfigure(i, weight = 1)

    def start(self):
        self._root_window.mainloop()

    def _on_canvas_clicked(self, event: tkinter.Event):
        for i in range(len(self._canvas)):
            for j in range(len(self._canvas[i])):
                if self._canvas[i][j] == event.widget:
                    row, col = i, j
        if self._game.isMoveValid(row, col):
            width = event.widget.winfo_width()
            height = event.widget.winfo_height()
            event.widget.create_oval(0,0,width,height,fill='black',outline='black')

        self._redraw_all()

    def _on_resized(self, event: tkinter.Event) -> None:
        self._redraw_all()
        
    def _redraw_all(self) -> None:
        for i in range(len(self._canvas)):
            for j in range(len(self._canvas[i])):
                if not self._game._board[i][j] == '.':
                    self._canvas[i][j].delete(tkinter.ALL)
                    width = self._canvas[i][j].winfo_width()
                    height = self._canvas[i][j].winfo_height()
                    if self._game._board[i][j] == 'B':
                        self._canvas[i][j].create_oval(0,0,width,height,fill='black',outline='black')
                    else:
                        self._canvas[i][j].create_oval(0,0,width,height,fill='white',outline='black')

if __name__ == '__main__':
    OthelloGui().start()
