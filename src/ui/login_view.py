from tkinter import ttk, StringVar, constants
from services.game_service import game_service, InvalidCredentialsError


class LoginView:
    '''Luokka joka vastaa login käyttöliittymän luonnista'''

    def __init__(self, root, handle_login, handle_show_create_user_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        '''näyttää näkymän'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''tuhoaa näkymän'''
        self._frame.destroy()

    def _login_handler(self):
        '''hakee ja tarkastaa käyttäjätunnuksen'''
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            game_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error('Invalid username or password')

    def _show_error(self, message):
        '''näyttää virheimoituksen'''
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        '''piilotta virheilmoituksen'''
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        '''luo käyttäjänimen syöttökentän'''
        username_label = ttk.Label(master=self._frame, text='Username')

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        '''luo salasanan syöttökentän'''
        password_label = ttk.Label(master=self._frame, text='Password')

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        '''luo login näkymän ja napit'''
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red'
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create user",
            command=self._handle_show_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
