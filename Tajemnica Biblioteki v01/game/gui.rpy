################################################################################
## Inicjalizacja
################################################################################

## Wyrażenie przesunięcia początkowego powoduje, że wyrażenie inicjalizajci w
## tym pliku są uruchamiane przed instrukcjami w jakimkolwiek innym pliku.
init offset = -2

## Wywołanie gui.init zresetuje style do rozsądnych wartości domyślnych oraz
## ustawia szerokość i wysokość gry.
init python:
    gui.init(1920, 1080)

## Włącz sprawdzanie niepoprawnych lub niestabilnych właściwości w ekranach lub
## transformacjach
define config.check_conflicting_properties = True


################################################################################
## Zmienne konfiguracyjne GUI
################################################################################


## Kolory ######################################################################
##
## Kolory tekstu w interfejsie.

## Kolor akcentujący używany w całym interfejsie do oznaczania i wyróżniania
## tekstu.
define gui.accent_color = '#99ccff'

## Kolor używany dla przycisku tekstowego, gdy nie jest on zaznaczony ani
## najechany.
define gui.idle_color = '#888888'

## Mały kolor jest używany do małego tekstu, który musi być jaśniejszy/
## ciemniejszy, aby osiągnąć ten sam efekt.
define gui.idle_small_color = '#aaaaaa'

## Kolor używany dla przycisków i pasków, które są zaznaczone (najechane).
define gui.hover_color = '#c1e0ff'

## Kolor używany dla przycisku tekstowego, gdy jest on zaznaczony, ale nie
## skupiony. Przycisk jest wybrany, jeśli jest to bieżący ekran lub wartość
## preferencji.
define gui.selected_color = '#ffffff'

## Kolor używany do przycisku tekstowego, gdy nie można go wybrać.
define gui.insensitive_color = '#8888887f'

## Kolory używane dla części pasków, które nie są wypełnione. Nie są używane
## bezpośrednio, ale są używane podczas ponownego generowania plików obrazów
## pasków.
define gui.muted_color = '#3d5166'
define gui.hover_muted_color = '#5b7a99'

## Kolory używane w tekstach dialogów i menu wyboru.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Czcionki i ich rozmiary #####################################################

## Czcionka używana do tekstu w grze.
define gui.text_font = "DejaVuSans.ttf"

## Czcionka używana do nazw postaci.
define gui.name_text_font = "DejaVuSans.ttf"

## Czcionka używana w tekście poza grą.
define gui.interface_text_font = "DejaVuSans.ttf"

## Rozmiar normalnego tekstu dialogowego.
define gui.text_size = 33

## Rozmiar imion postaci.
define gui.name_text_size = 45

## Rozmiar tekstu w interfejsie użytkownika gry.
define gui.interface_text_size = 33

## Rozmiar etykiet w interfejsie użytkownika gry.
define gui.label_text_size = 36

## Rozmiar tekstu na ekranie powiadomień.
define gui.notify_text_size = 24

## Rozmiar tytułu gry
define gui.title_text_size = 75


## Menu główna oraz menu gry   #################################################

## Obrazy używane w menu głównym i menu gry.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialog ######################################################################
##
## Zmienne te kontrolują sposób wyświetlania dialogu na ekranie, wiersz po
## wierszu.

## Wysokość pola tekstowego zawierającego dialog.
define gui.textbox_height = 278

## Umieszczenie pola tekstowego pionowo na ekranie. 0.0 to góra, 0.5 to środek,
## a 1.0 to dół.
define gui.textbox_yalign = 1.0


## Umieszczenie nazwy postaci mówiącej w stosunku do pola tekstowego. Może to
## być cała liczba pikseli od lewej lub od góry albo 0,5 do środka.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Poziome wyrównanie imienia postaci. Może to być 0,0 dla wyrównania do lewej,
## 0,5 do wyśrodkowania i 1,0 do wyrównania do prawej.
define gui.name_xalign = 0.0

## Szerokość, wysokość i krawędzie pola zawierającego nazwę postaci lub Brak,
## aby automatycznie zmienić jej rozmiar.
define gui.namebox_width = None
define gui.namebox_height = None

## Obramowanie pola zawierającego imię postaci w kolejności od lewej, od góry,
## od prawej, od dołu.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Jeśli 'True' (prawda), tło pola nazwy zostanie ułożone sąsiadująco, jeśli
## 'False' (fałsz), tło pola nazwy zostanie przeskalowane.
define gui.namebox_tile = False


## Umieszczenie dialogu względem pola tekstowego. Może to być całkowita liczba
## pikseli względem lewej lub górnej części pola tekstowego lub 0,5 względem
## środka.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Maksymalna szerokość tekstu dialogowego w pikselach
define gui.dialogue_width = 1116

## Poziome wyrównanie tekstu dialogu. Może to być 0,0 dla wyrównanego do lewej,
## 0,5 dla wyśrodkowanego i 1,0 dla wyrównanego do prawej.
define gui.dialogue_text_xalign = 0.0


## PRzyciski ###################################################################
##
## Te zmienne, wraz z plikami graficznymi w gui/button, kontrolują aspekty
## wyświetlania przycisków.

## Szerokość i wysokość przycisku w pikselach. Jeśli brak, Ren'Py oblicza
## rozmiar.
define gui.button_width = None
define gui.button_height = None

## Ramki po każdej stronie przycisku, w kolejności lewej, górnej, prawej,
## dolnej.
define gui.button_borders = Borders(6, 6, 6, 6)

## Jeśli 'True' (prawda), obraz tła zostanie ułożony sąsiadująco. Jeśli
## 'False' (fałsz), obraz tła będzie skalowany liniowo
define gui.button_tile = False

## Czcionka używana przez przycisk.
define gui.button_text_font = gui.interface_text_font

## Rozmiar tekstu używanego przez przycisk.
define gui.button_text_size = gui.interface_text_size

## Kolor tekstu przycisku w różnych stanach.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Poziome wyrównanie tekstu przycisku. (0.0 to lewe, 0.5 to środek, 1.0 to
## prawy).
define gui.button_text_xalign = 0.0


## Zmienne zastępują ustawienia dla różnych rodzajów przycisków. Zapoznaj się z
## dokumentacją gui, aby dowiedzieć się, jakie rodzaje przycisków są dostępne i
## do czego służą.
##
## Poniższe ustawienia są używane przez domyślny interfejs:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Możesz także dodać własne dostosowania, dodając odpowiednio nazwane zmienne.
## Na przykład możesz odkomentować następujący wiersz, aby ustawić szerokość
## przycisku nawigacyjnego.

# define gui.navigation_button_width = 250


## Przyciski wyboru ############################################################
##
## Przyciski wyboru są używane w menu w grze.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Przycisk pliku zapisu #######################################################
##
## Przycisk na pliki zapisu (slot) jest specjalnym rodzejem przycisku. Zawiera
## obraz miniatury oraz tekst opisujący zawartość slotu zapisu. Slot zapisu
## wykorzystuje pliki graficzne w gui/button, podobnie jak inne rodzaje
## przycisków.

## Przycisk zapisu 
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Szerokość i wysokość miniatur używanych przez sloty zapisu.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Liczba kolumn i wierszy w siatce slotów zapisu.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Pozycjonowanie i odstępy ####################################################
##
## Te zmienne kontrolują położenie i odstępy różnych elementów interfejsu
## użytkownika.

## Położenie lewej strony przycisków nawigacyjnych względem lewej strony
## ekranu..
define gui.navigation_xpos = 60

## Pozycja pionowa wskaźnika pominięcia.
define gui.skip_ypos = 15

## Pionowa pozycja ekranu powiadomień
define gui.notify_ypos = 68

## Odstępy między opcjami menu.
define gui.choice_spacing = 33

## Przyciski w sekcji nawigacji menu głównego i menu gry.
define gui.navigation_spacing = 6

## Kontroluje ilość odstępów między preferencjami.
define gui.pref_spacing = 15

## Steruje odległością między przyciskami preferencji.
define gui.pref_button_spacing = 0

## Odstępy między przyciskami strony pliku.
define gui.page_spacing = 0

## Odstępy między plikami zapisu (slotami).
define gui.slot_spacing = 15

## Pozycja tekstu menu głównego.
define gui.main_menu_text_xalign = 1.0


## Klatki ######################################################################
##
## Te zmienne sterują wyglądem ramek, które mogą zawierać komponenty interfejsu
## użytkownika, gdy nie ma nakładki lub okna.

## Ramki ogólne.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Ramka używana jako część ekranu potwierdzenia.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Ramka używana jako część ekranu pomijania.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Ramka używana jako część ekranu powiadomień.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Czy tła ramek powinny być kafelkowe?
define gui.frame_tile = False


## Paski, paski przewijania i suwaki ###########################################
##
## Kontrolują one wygląd i rozmiar pasków, pasków przewijania i suwaków.
##
## Domyślny GUI używa tylko suwaków i pionowych pasków przewijania. Wszystkie
## pozostałe paski są używane tylko na ekranach napisanych przez twórców.

## Wysokość poziomych pasków, pasków przewijania i suwaków. Szerokość pionowych
## pasków, pasków przewijania i suwaków
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 'True' (prawda), jeśli obrazy pasków powinny być kafelkowane.
## 'False' (fałsz), jeśli powinny być skalowane liniowo.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Granice poziome.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Granice pionowe.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Ustawienie pasków GUI, które nie posiadają przewijania. Ustawienie
## "hide" (schowaj), ukryje owe paski, natomiast "None" (brak), wyświetli je.
define gui.unscrollable = "hide"


## Historia ####################################################################
##
## Ekran historii wyświetla dialog, który gracz już odrzucił.

## Liczba bloków historii dialogów, które Ren'Py zachowa.
define config.history_length = 250

## Wysokość wpisu na ekranie historii lub "None" (brak), aby wysokość była
## zmienna kosztem wydajności.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## Pozycja, szerokość i wyrównanie etykiety podającej nazwę postaci mówiącej.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Pozycja, szerokość i wyrównanie tekstu dialogu.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Opcja NVL-Mode ##############################################################
##
## Ekran trybu NVL wyświetla dialog wypowiadany przez postacie trybu NVL

## Granice tła okna tła trybu NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Wyświetlona zostanie maksymalna liczba wpisów trybu NVL Ren'Py. W przypadku
## wyświetlenia większej liczby wpisów, najstarszy wpis zostanie usunięty.
define gui.nvl_list_length = 6

## Wysokość wpisu trybu NVL. Ustaw to na Brak, aby wpisy dynamicznie
## dostosowywały wysokość.
define gui.nvl_height = 173

## Odstępy między wpisami trybu NVL, gdy gui.nvl_height ma wartość "None" (brak)
## oraz między wpisami trybu NVL a menu trybu NVL.
define gui.nvl_spacing = 15

## Pozycja, szerokość i wyrównanie etykiety podającej nazwę postaci mówiącej.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Pozycja, szerokość i wyrównanie tekstu dialogu.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Pozycja, szerokość i wyrównanie tekstu nvl_thought (tekst wypowiadany przez
## postać nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Pozycja przycisków menu nvl (menu_buttons).
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Lokalizacja #################################################################

## Kontroluje to, gdzie dozwolone jest łamanie wiersza. Ustawienie domyślne jest
## odpowiednie dla większości języków. Listę dostępnych wartości można znaleźć
## pod adresem https://www.renpy.org/doc/html/style_properties.html#style-
## property-language

define gui.language = "unicode"


################################################################################
## Urządzenia mobilne
################################################################################

init python:

    ## Zwiększa to rozmiar szybkich przycisków, aby ułatwić ich dotykanie na
    ## tabletach i telefonach.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Zmienia to rozmiar i odstępy różnych elementów GUI, aby były dobrze
    ## widoczne na telefonach.
    @gui.variant
    def small():

        ## Roozmiar czcionki
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Dostosuj położenie pola tekstowego.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Zmieniaj rozmiar i odstępy różnych rzeczy.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Układ przycisku pliku.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Opcja NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
