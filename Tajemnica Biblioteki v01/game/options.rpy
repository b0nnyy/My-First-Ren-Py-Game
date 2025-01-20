## Ten plik zawiera opcję, które można zmienić, aby dostosować grę.
##
## Linie zaczynające się od dwóch znaków '#' są komentarzami i nie należy ich
## odkomentować. Wiersze zaczynające się od pojedynczego znaku '#' są kodem
## zakomentowanym i możesz chcieć je odkomentować, gdy jest to właściwe. 


## Podstawy ####################################################################

## Czytelna dla człowieka nazwa gry. Służy do ustawiania domyślnego tytułu okna
## i pojawia się w interfejsie oraz raportach o błędach.
##
## Znak _() otaczający ciąg znaków oznacza go jako kwalifikujący się do
## tłumaczenia.

define config.name = _("Tajemnica Biblioteki v01")


## Określa, czy tytuł podany powyżej jest wyświetlany na ekranie menu głównego.
## Ustaw to na 'False', aby ukryć tytuł.

define gui.show_name = True


## Wersja gry.

define config.version = "1.0"


## Tekst, który jest umieszczony na ekranie, w sekcji o grze. Umieść tekst
## między potrójnymi cudzysłowami i zostaw pustą linię między akapitami.

define gui.about = _p("""
""")


## Krótka nazwa gry używana dla plików wykonywalnych i katalogów w zbudowanej
## dystrybucji. Musi zawierać tylko ASCII i nie może zawierać spacji, dwukropków
## ani średników.

define build.name = "TajemnicaBibliotekiv01"


## Dźwięki i muzyka ############################################################

## Te trzy zmienne kontrolują między innymi to, które miksery są domyślnie
## pokazywane graczowi. Ustawienie jednej z nich na False spowoduje ukrycie
## odpowiedniego miksera.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Aby umożliwić użytkownikowi odtworzenie dźwięku testowego na kanale
## dźwiękowym lub głosowym, odkomentuj poniższą linię i użyj jej do ustawienia
## przykładowego dźwięku do odtworzenia.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Odkomentuj następującą linię, aby ustawić plik audio, który będzie
## odtwarzany, gdy odtwarzacz jest w menu głównym. Ten plik będzie odtwarzany w
## grze, dopóki nie zostanie zatrzymany lub odtworzony inny plik.

# define config.main_menu_music = "main-menu-theme.ogg"


## Przejście ###################################################################
##
## Te zmienne ustawiają przejścia, które są używane w przypadku wystąpienia
## określonych zdarzeń. Każda zmienna powinna być ustawiona na przejście lub
## brak (None), aby wskazać, że żadne przejście nie powinno być używane.

## Menu gry - wejście/wyjście

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Menu gry - między scenami

define config.intra_transition = dissolve


## Przejście używane po wczytaniu gry.

define config.after_load_transition = None


## Przejście do menu głównego po zakończeniu gry.

define config.end_game_transition = None


## Zmienna do ustawienia przejścia używanego podczas uruchamiania gry nie
## istnieje. Zamiast tego po pokazaniu początkowej sceny użyj wyrażenia z (use a
## with statement).


## Zarządzanie oknem ###########################################################
##
## Opcja odpowiada za okno dialogowe. Jeżeli ustawiono "show" (pokaż), to będzie
## zawsze wyświetlone. Jeżeli ustawiono "hide" (ukryj), to zostanie wyświetlone
## kiedy będzie dialog. Jeżeli ustawiono "auto" to okno jest ukrywane przed
## wypowiedziami scen i ponownie wyświetlane po wyświetleniu dialogu.
##
## Po uruchomieniu gry, ustawienie te można zmienić za pomocą komend "window
## show", "window hide" oraz "window auto". 

define config.window = "auto"


## Przejścia używane do pokazywania i ukrywania okna dialogowego

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Ustawienia domyślne #########################################################

## Opcja odpowiada za domyślną szybkość tekstu. Wartość domyślna, 0, jest
## nieskończona, podczas gdy każda inna liczba to liczba znaków na sekundę do
## wpisania. 

default preferences.text_cps = 0


## Domyślne opóźnienie automatycznego przewijania. Większe liczby prowadzą do
## dłuższych czasów oczekiwania, przy czym prawidłowym zakresem jest od 0 do 30

default preferences.afm_time = 15


## Katalog zapisu ##############################################################
##
## Ustawienie katalogu, w którym Ren'Py umieści pliki zapisu dla tej gry. Pliki
## zapisu zostaną umieszczone w:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Opcji tej zazwyczaj nie należy zmieniać. Jeżeli jest zmiana, to należy
## zastosować dosłowny ciąg, a nie wyrażenie.

define config.save_directory = "TajemnicaBibliotekiv01-1736186032"


## Ikona #######################################################################
##
## Ikona wyświetlana na pasku zadań lub doku

define config.window_icon = "gui/window_icon.png"


## Konfiguracja kompilacji  ####################################################
##
## Sekcja odpoaiwada za sposób w jaki Ren'Py zamienia Twój projekt w pliki
## dystrybucyjne.

init python:

    ## Poniższe funkcje przyjmują wzorce plików. Wzorce plików nie uwzględniają
    ## wielkości liter i są dopasowywane do ścieżki względem katalogu bazowego,
    ## z wiodącymi lub bez /. Jeśli pasuje wiele wzorów, używany jest pierwszy.
    ##
    ## Wzór:
    ##
    ## znak / jest separatorem katalogów.
    ##
    ## * uwzględnia wszystkie znaki, z wyjątkiem separatora katalogu.
    ##
    ## ** uwzględnia wszystkie znaki, łącznie z separatorem katalogu.
    ##
    ## Na przykład "*.txt" dopasowuje pliki txt w katalogu podstawowym,
    ## "game/**.ogg" dopasowuje pliki ogg w katalogu gry lub dowolnym z jego
    ## podkatalogów, a "**.psd" dopasowuje pliki psd w dowolnym miejscu
    ## projektu.

    ## Klasyfikuj pliki jako Brak (None), aby wykluczyć je ze zbudowanych
    ## dystrybucji

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Aby zarchiwizować pliki, sklasyfikuj je jako 'archive' (archiwum).

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Pliki pasujące do wzorców dokumentacji są duplikowane w kompilacji
    ## aplikacji na komputery Mac, więc pojawiają się zarówno w aplikacji, jak i
    ## pliku zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Klucz licencyjny Google Play jest wymagany do wykonywania zakupów w
## aplikacji. Można go znaleźć w konsoli deweloperskiej Google Play, w zakładce
## "Monetyzuj" > "Konfiguracja monetyzacji" > "Licencjonowanie".

# define build.google_play_key = "..."


## Nazwa użytkownika i nazwa projektu powiązane z projektem itch.io, oddzielone
## ukośnikiem

# define build.itch_project = "renpytom/test-project"
