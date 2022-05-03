from tkinter import ttk, constants
from services.game_service import game_service
from ui.game_ui import Main


class StatsView:
    '''pelitilastojen näyttämisestä vastaava luokka'''
    def __init__(self, root, handle_logout):
        """Luokan konstruktori. Luo uuden tehtävälistausnäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_log_out:
                kutsuttava-arvo, joka kirjaa käyttäjän ulos
        """
        self._root = root
        self._handle_logout = handle_logout
        self._user = game_service.get_current_user()
        self._frame = None
        self.run_game = Main()
        self._initialize()

    def pack(self):
        '''näyttää näkymän'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''tuhoaa näkymän'''
        self._frame.destroy()

    def _logout_handler(self):
        '''kirjaa käyttäjän ulos'''
        game_service.logout()
        self._handle_logout()

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

    def _handle_run_game(self):
        '''avaa pelinäkymän'''
        self.run_game.start_menu()

    def _initialize_footer(self):

        create_start_game_button = ttk.Button(
            master=self._frame,
            text='Play',
            command=self._handle_run_game
        )

        create_start_game_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._todo_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_footer()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
