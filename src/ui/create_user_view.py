'''importataan tarvittavat kirjastot ja luokat'''
from tkinter import ttk, StringVar, constants,messagebox
from services.game_service import game_service, UsernameExistsError

class CreateUserView: #pylint: disable=too-many-instance-attributes
    '''Luokka joka vastaa create user käyttöliittymän luonnista'''

    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Luokan konstruktori. Luo uuden rekisteröitymisnäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_create_user:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä luodaan.
                Saa argumentteina käyttäjätunnuksen ja salasanan.
            handle_show_login_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään kirjautumisnäkymään.
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _create_user_handler(self):
        '''luo ja tarkastaa luodun käyttäjätunnuksen'''
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            messagebox.showerror('Username and password is required')
            return

        try:
            game_service.create(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f'Username {username} already exists')

    def _show_error(self, message):
        '''näyttää virheilmoituksen'''
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        '''piilottaa virheilmoituksen'''
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
        '''luo create user näkymän ja napit'''
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

        create_user_button = ttk.Button(
            master=self._frame,
            text='Create',
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text='Login',
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
