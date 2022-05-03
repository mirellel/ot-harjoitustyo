from ui.login_view import LoginView
from ui.stats_view import StatsView
from ui.create_user_view import CreateUserView


class UI:
    '''Sovelluksen käyttöliittymästä vastaava luokka'''

    def __init__(self, root):
        '''Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        Args:
            root:
                TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        '''
        self._root = root
        self._current_view = None

    def start(self):
        '''käynnistää käyttöliittymän'''
        self._show_login_view()

    def _hide_current_view(self):
        '''tuhoaa nykyisen näkymän'''
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _hande_login(self):
        self._show_login_view()

    def _handle_create_user(self):
        self._show_create_user_view()

    def _show_login_view(self):
        '''näyttää login näkymän'''
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_stats_view, self._show_create_user_view)

        self._current_view.pack()

    def _show_stats_view(self):
        '''näyttää käyttäjänäkymän'''
        self._hide_current_view()

        self._current_view = StatsView(self._root, self._show_login_view)

        self._current_view.pack()

    def _show_create_user_view(self):
        '''näyttää create user näkymän'''
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_stats_view,
            self._show_login_view
        )

        self._current_view.pack()
