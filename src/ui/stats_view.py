from tkinter import ttk, constants
from services.game_service import game_service

class StatsListView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

class StatsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = game_service.get_current_user()
        self._frame = None
        self._stats_list_view = None
        self._todo_list_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        game_service.logout()
        self._handle_logout()

    def _initialize_todo_list(self):
        if self._todo_list_view:
            self._todo_list_view.destroy()

        todos = game_service.get_undone_todos()

        self._todo_list_view = StatsListView(
            self._todo_list_frame)

        self._todo_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f'Logged in as {self._user.username}'
        )

        logout_button = ttk.Button(
            master=self._frame,
            text='Logout',
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._todo_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)