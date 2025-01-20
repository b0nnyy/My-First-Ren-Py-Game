################################################################################
## Inicjalizacja
################################################################################

init offset = -1


################################################################################
## Style
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Sceny podczas gry
################################################################################


## Scena rozmowy ###############################################################
##
## Ekran rozmowy jest używany do wyświetlania dialogu. Wymagane są dwa
## parametry, kto i co, które są odpowiednio nazwą postaci mówiącej i
## tekstem, który ma być wyświetlany. Parametr "who" (kto) może mieć wartość
## "None" (brak), jeśli nie podano nazwy. 
##
## Ten ekran musi tworzyć tekst do wyświetlenia z id "what" (co), ponieważ
## Ren'Py używa go do zarządzania wyświetlaniem tekstu. Może również tworzyć
## elementy do wyświetlania z id "who" (kto) i id "window" (okno), aby
## zastosować właściwości stylu.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Jeśli jest obraz boczny, wyświetl go nad tekstem. Nie wyświetlaj w
    ## wariancie telefonu - nie ma miejsca
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Udostępnij pole nazwy do stylizacji za pomocą obiektu Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Scena wprowadzenia ##########################################################
##
## Ten ekran służy do wyświetlania renpy.input. Parametr monitu służy do
## przekazywania monitu tekstowego.
##
## Ten ekran musi utworzyć dane wejściowe wyświetlane z identyfikatorem "input",
## aby zaakceptować różne parametry wejściowe.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Ekran wyboru ################################################################
##
## Ten ekran służy do wyświetlania wyborów w grze przedstawionych w instrukcji
## menu. Jeden parametr, items, to lista obiektów, każdy z polami podpisu i
## akcji.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Szybkie menu ################################################################
##
## Szybkie menu jest wyświetlane w grze, aby zapewnić łatwy dostęp do menu poza
## grą.

screen quick_menu():

    ## Upewnij się, że pojawia się nad innymi scenami.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Powrót") action Rollback()
            textbutton _("Historia") action ShowMenu('history')
            textbutton _("Pomiń") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Zapis") action ShowMenu('save')
            textbutton _("S.Zapis") action QuickSave()
            textbutton _("S.Wczytaj") action QuickLoad()
            textbutton _("Opcje") action ShowMenu('preferences')


## Ten kod zapewnia, że ekran quick_menu jest wyświetlany w grze, gdy gracz nie
## ukrył jawnie interfejsu.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Ekrany główne i menu gry
################################################################################

## Ekran nawigacji #############################################################
##
## Ten ekran jest zawarty w menu głównym i menu gry i zapewnia nawigację do
## innych menu oraz rozpoczęcie gry.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("Historia") action ShowMenu("history")

            textbutton _("Zapis") action ShowMenu("save")

        textbutton _("Wczytaj") action ShowMenu("load")

        textbutton _("Preferencje") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Zakończ powtórkę") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu główne") action MainMenu()

        textbutton _("Informacje") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Pomoc nie jest potrzebna ani nie dotyczy urządzeń mobilnych.
            textbutton _("Pomoc") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Przycisk zamknij (quit) jest zabroniony w iOS, niepotrzebny w
            ## Androidzie i przeglądarkach.
            textbutton _("Zamknij") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Ekran głównego menu #########################################################
##
## Służy do wyświetlania menu głównego po uruchomieniu Ren'Py
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    # Tło menu
    window:
        style "main_menu"
        add "menug.png"  # Dodaj grafikę tła

    # Logo gry
    add "logo.png" align (0.5, 0.2)  # Logo gry wyśrodkowane u góry

# Przyciski menu
    vbox:
        align (0.5, 0.6)  # Wyśrodkowanie przycisków
        spacing 20  # Odstępy między przyciskami

        # Przycisk "Nowa Gra"
        textbutton "Nowa Gra" action Start() style "menu_button"

        # Przycisk "Załaduj grę"
        textbutton "Załaduj grę" action ShowMenu("load") style "menu_button"

        # Przycisk "Ustawienia"
        textbutton "Ustawienia" action ShowMenu("preferences") style "menu_button"

        # Przycisk "Wyjście"
        textbutton "Wyjście" action Quit(confirm=True) style "menu_button"

    # Stopka z wersją gry
    text "Tajemnica Biblioteki - Wersja 1.0" size 14 color "#FFFFFF" align (0.98, 0.98)

# Styl przycisków
style menu_button:
    size 32  # Rozmiar tekstu
    font "font.ttf"  # Nazwa niestandardowej czcionki (umieść w folderze 'game')
    background Frame("przycisk.png", 10, 10)  # Obraz przycisku w stanie spoczynku
    hover_background Frame("przycisk.png", 10, 10)  # Obraz przycisku po najechaniu
    xalign 0.5
    yalign 0.5



## Ekran menu gry ##############################################################
##
## Podstawową wspólna struktura ekranu menu gry. Jest wywoływany z razem z
## ekranem tytułowym, wyświetla tło, tytuł i nawigację.
##
## Parametr przewijania może mieć wartość "None" (Brak) lub "viewport" albo
## "vpgrid". Ten ekran ma być używany z jednym lub większą liczbą dzieci, które
## są transkludowane (umieszczane) wewnątrz niego.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Zarezerwowane miejsce na sekcję nawigacji
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Powrót"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Ekran o (np. o grze) ########################################################
##
## Ten ekran zawiera informacje (podziękowania - creditsy), prawach autorskich
## dotyczących gry i Ren'Py
##
## Nie ma nic specjalnego w tym ekranie, dlatego służy on również jako przykład,
## jak zrobić niestandardowy ekran.

screen about():

    tag menu

    ## Wyrażenie use zawiera ekran game_menu wewnątrz tego. Potomek vbox jest
    ## następnie dołączany do okna widoku na ekranie menu gry.
    use game_menu(_("Informacje"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Wersja [config.version!t]\n")

            ## gui.about zazwyczaj jest ustawiony w options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Wykonano przy pomocy {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Ekran wczytania i zapisu ####################################################
##
## Ekrany te są odpowiedzialne za umożliwienie graczowi zapisania gry i
## ponownego jej wczytania. Ponieważ mają prawie wszystko wspólne, oba są
## zaimplementowane w postaci trzeciego ekranu, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Zapis"))


screen load():

    tag menu

    use file_slots(_("Wczytaj"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Strona {}"), auto=_("Automatyczny zapis"), quick=_("Szybki zapis"))

    use game_menu(title):

        fixed:

            ## Opcja zapewnie wejście zdarzeniu wprowadzającemu, zanim to zrobi
            ## którykolwiek z przycisków.
            order_reverse True

            ## Nazwa strony, którą można edytować, klikając przycisk.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Siatka plików zapisów (file slots).
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Puste miejsce")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Przyciski dostępu do innych stron.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10), zasięg zwraca liczby od 1 do 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Synchronizacja wysyłania"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Pobierz Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Ekran preferencji ###########################################################
##
## Ekran preferencji pozwala graczowi skonfigurować grę, by grało się wygodniej.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferencje"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Wyświetlenie")
                        textbutton _("Okno") action Preference("display", "window")
                        textbutton _("Pełny ekran") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Pomiń")
                    textbutton _("Tekst niewidoczny") action Preference("skip", "toggle")
                    textbutton _("Tekst po wyborze") action Preference("after choices", "toggle")
                    textbutton _("Przejścia") action InvertSelected(Preference("transitions", "toggle"))

                ## Miejsce na dodatkowe vboksy typu "radio_pref" lub
                ## "check_pref", aby dodać dodatkowe preferencje zdefiniowane
                ## przez twórcę

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Szybkość tekstu")

                    bar value Preference("text speed")

                    label _("Czas automatycznego przewijania")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Głośność muzyki")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Głośność dźwięku")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Głośność głosu")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Wycisz wszystko"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Ekran historii ##############################################################
##
## Jest to ekran, który wyświetla graczowi historię dialogów. Chociaż nie ma
## nic specjalnego w tym ekranie, musi on mieć dostęp do historii dialogów
## przechowywanej w _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Unikaj przewidywania tego ekranu, ponieważ może być bardzo duży.
    predict False

    use game_menu(_("Historia"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Wszystko jest wyświetlone poprawnie jeżeli history_height
                ## jest ustawione na None
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Pobranie koloru dla who postaci, jeżeli jest
                        ## ustawione.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Historia dialogu jest pusta.")


## Określa to, jakie tagi mogą być wyświetlane na ekranie historii.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Ekran pomocy ################################################################
##
## Ekran wyświetlający informacje o ustawieniach klawiatury i myszy. Używa
## innych ekranów (keyboard_help, mouse_help i gamepad_help) do wyświetlania
## aktualnej pomocy.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Pomoc"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Klawiatura") action SetScreenVariable("device", "keyboard")
                textbutton _("Mysz") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Wejdź na stronę")
        text _("Rozwija dialog i aktywuje interfejs")

    hbox:
        label _("Spacja")
        text _("Rozwija dialog bez wybierania opcji.")

    hbox:
        label _("Strzałki")
        text _("Poruszanie się po interfejsie.")

    hbox:
        label _("Ucieczka")
        text _("Uruchomienie menu gry.")

    hbox:
        label _("Ctrl")
        text _("Pomija dialog, gdy jest wciśnięty.")

    hbox:
        label _("Tab")
        text _("Przełącza pomijanie dialogów.")

    hbox:
        label _("Strona w górę")
        text _("Wraca do wcześniejszego dialogu.")

    hbox:
        label _("Strona w dół")
        text _("Przechodzi do późniejszego dialogu.")

    hbox:
        label "H"
        text _("Ukrywa interfejs użytkownika.")

    hbox:
        label "S"
        text _("Wykonanie zrzutu ekranu.")

    hbox:
        label "V"
        text _("Przełącza wspomaganie {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Otwiera menu dostępności.")


screen mouse_help():

    hbox:
        label _("Lewy przycisk")
        text _("Rozwija dialog i aktywuje interfejs")

    hbox:
        label _("Środkowy przycisk")
        text _("Ukrywa interfejs użytkownika.")

    hbox:
        label _("Prawy przycisk")
        text _("Uruchomienie menu gry.")

    hbox:
        label _("Kółko myszy w górę")
        text _("Wraca do wcześniejszego dialogu.")

    hbox:
        label _("Kółko myszy w dół")
        text _("Przechodzi do późniejszego dialogu.")


screen gamepad_help():

    hbox:
        label _("Prawy spust\nA/dolny przycisk")
        text _("Rozwija dialog i aktywuje interfejs")

    hbox:
        label _("Lewy spust\nLewe ramię (L)")
        text _("Wraca do wcześniejszego dialogu.")

    hbox:
        label _("Prawe ramię (R)")
        text _("Przechodzi do późniejszego dialogu.")

    hbox:
        label _("D-Pad, Gałka")
        text _("Poruszanie się po interfejsie.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Uruchomienie menu gry.")

    hbox:
        label _("Y/górny przycisk")
        text _("Ukrywa interfejs użytkownika.")

    textbutton _("Kalibracja") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Dodatkowe ekrany
################################################################################


## Ekran potwierdzenia #########################################################
##
## Ekran potwierdzenia jest wywoływany, gdy Ren'Py chce zadać graczowi pytanie
## tak lub nie.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Upewnienie, że inne ekrany nie otrzymają danych wejściowych, podczas
    ## wyświetlenia tego ekranu.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Tak") action yes_action
                textbutton _("Nie") action no_action

    ## Prawy przycisk i Escape wybiera odpowiedź "Nie".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pomiń ekran wskaźnika #######################################################
##
## Wyświetlany jest ekran skip_indicator, który wskazuje, że pomijanie jest w
## toku.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Pomijanie")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Transformacja służy do migania strzałek jedna po drugiej
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Należy użyć czcionki, która zawiera mały czarny trójkącik (BLACK RIGHT-
    ## POINTING SMALL TRIANGLE glyph).
    font "DejaVuSans.ttf"


## Ekran powiadomień ###########################################################
##
## Ekran powiadomień służy do pokazywania graczowi wiadomości. (Na przykład, gdy
## gra została szybko zapisana lub zrobiono zrzut ekranu).
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Ekran NVL ###################################################################
##
## Ten ekran jest używany do dialogów i menu w trybie NVL
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Wyświetla dialog w vpgrid lub vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Wyświetli menu, jeżeli jest podane. Menu może być wyświetlone
        ## nieprawidłowo, jeżeli config.narrator_menu jest ustawione na True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Kontrola maksymalnej liczbę wpisów w trybie NVL, które można wyświetlić
## jednocześnie.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## Ekran bąbelkowy jest używany do wyświetlania graczowi dialogu, gdy używa się
## bąbelków mowy. Ekran bąbelkowy przyjmuje te same parametry co ekran say,
## musi tworzyć displayable o id "what", oraz może tworzyć displayable o id
## "namebox", "who", oraz "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Warianty mobilne
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Ponieważ mysz może nie być obecna, zastępujemy szybkie menu wersją, która
## używa mniejszej liczby i większych przycisków, które są łatwiejsze w dotyku.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Powrót") action Rollback()
            textbutton _("Pomiń") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
