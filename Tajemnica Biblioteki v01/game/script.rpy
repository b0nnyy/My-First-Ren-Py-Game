define librarian = Character("Hania", color="#a11d1d")
define a = Character("Alice")
define b = Character("adada", color="#8f2828")

label start:
    scene black with fade
    play music "start.mp3" fadein 2.0
    "Jest piątkowy wieczór. Po ciężkim dniu zajęć postanawiasz zostać w bibliotece uczelnianej trochę dłużej..."
    "Nie zauważasz, jak czas mija, aż nagle poczułeś chłód na karku..."
    scene glowny with dissolve

    "Biblioteka zamarła. Drzwi są zamknięte, a wokół panuje przerażająca cisza."
    "Twoim zadaniem jest znaleźć sposób na wydostanie się z biblioteki."

    jump game_intro
    default zagadka_rozwiazana = False  # Zmienna, która będzie przechowywać informację o rozwiązanej zagadce
    default magazyn_otwarty = False  # Domyślnie magazyn jest zamknięty
    default Sala_matematyczna = False  # Domyślnie magazyn jest zamknięty

    label game_intro:
        scene hol1 with fade
        "Znajdujesz się na głównym holu biblioteki. Przed Tobą kilka drzwi. prowadzących w różne strony."
        menu:
            "Przejdz do Magazynu":
                jump Magazyn

            "Sprawdz Sala nr 1":

                jump Sala101

            "Przejdź dalej ":
                jump schody
                
    label schody:
    scene schody1 with fade
    menu:
        "Idź na górne piętro" if magazyn_otwarty:
            jump piętro2

        "Idź na górne piętro (zablokowane)" if not magazyn_otwarty:
            "Nie możesz jeszcze przejść na górne piętro."
            jump schody

        "Wróć do głównego holu":
            jump game_intro


    label piętro2:

        scene black with fade
        play sound "kroki.mp3" volume 1.0
        "Ciemne, pustoszejące korytarze. Słychać odgłos kroków odbijających się echem w pustych przestrzeniach. Bohater wchodzi na piętro, gdy nagle zapada ciemność. Zatrzymuje się w miejscu, próbując złapać oddech."
        scene hol2 with fade
        "Ciemność powoli ustępuje, ukazując sylwetkę postaci stojącej w głębi korytarza"
        "Bohater" "(Myśli) Co się dzieje? Gdzie teraz jestem...? "
        show ghost at right
        "???" "Nie martw się, to tylko kolejna próba."

        "Bohater" "(Zaskoczony) Kim jesteś? Co się tutaj dzieje?"

        "????" "Nazywam się... To nie jest teraz ważne. Musisz znaleźć pokój numer 10. Tam czeka na ciebie kolejna zagadka."

        "Bohater" "(Niepewnie) Zagadka? Jak mam znaleźć ten pokój w tej ciemności?"

        "????" "Zaufaj sobie. Ciemność to tylko iluzja. Pamiętaj: to, co widzisz, nie zawsze jest tym, czym się wydaje."

        "????" "*Powoli zanika w ciemności, pozostawiając bohatera samego w mroku.*"

        "Bohater" "(Myśli) Muszę znaleźć ten pokój. Czas na rozwiązanie kolejnej zagadki... "

label pietro2:
        scene hol2 with fade

        menu:
            "Idź do pokoju nr 10":
                jump pietrodrzwi

            "Przejdź do Sali matematycznej" if Sala_matematyczna:
                jump Sala_matematyczna
            "Przejdź do Sali matematycznej (zablokowane)" if not Sala_matematyczna:
                "Nie możesz jeszcze przejść do sali matematycznej. Musisz rozwiązać zagadkę z pokoju nr 10."
                jump pietro2
        

label pietrodrzwi:
    scene pietrodrzwi with fade

    "Bohater" " To ten pokój.... Wchodzę!!!"

    scene ciemnasala with fade
    show ali1 at right
    a "Hejka!!!!"
    "Kim jesteś?"
    "Jestem emmm...... Alice!!!"
    "Co tutaj robisz?"
    a "Jakaś magiczna siła powiedziała, że nie wyjdę z tego pokoju, aż nie rozwiążę zagadki"
    a "Czy możesz mi pomóc..........?"
    "Pewnie, o co chodzi?"
    a "Spójrz na tę planszę"

    show plansza with fade

    call screen zagadkapietro

    if card_result == "correct":
        $ Sala_matematyczna = True  # Odblokowanie sali matematycznej
        jump correct_choice
    else:
        jump you_died



    if card_result == "correct":
        jump correct_choice
    else:
        jump you_died 

screen zagadkapietro:
    vbox:
        align (0.5, 0.5) 
        spacing 20

      
        text "Zagadka Tarota" size 34 bold True

        
        text "\"Tylko jedna karta wskaże Ci właściwą ścieżkę. Wybierz mądrze, bo nie wszystkie drogi prowadzą na wolność.\""

        
        hbox:
            spacing 50  
            align (0.5, 0.5)  

            
            imagebutton:
                idle Transform("tylkart.png", fit=(200, 300))
                hover Transform("karta1.jpg", fit=(200, 300))
                action [SetVariable("card_result", "wrong"), Jump("you_died")]

           
            imagebutton:
                idle Transform("tylkart.png", fit=(200, 300))
                hover Transform("karta2.jpg", fit=(200, 300))
                action [SetVariable("card_result", "correct"), Return()]

            
            imagebutton:
                idle Transform("tylkart.png", fit=(200, 300))
                hover Transform("karta3.jpg", fit=(200, 300))
                action [SetVariable("card_result", "wrong"), Jump("you_died")]

label you_died:
    scene bg black with fade
    play sound "umarles.mp3"
    $ renpy.pause(1.0)

    show text "YOU DIED" with fade 

    $ renpy.pause(3.0)

    "Spróbuj ponownie..."
    jump piętro2

label correct_choice:
    scene git with fade
    "Wybrałeś mądrze! Gratulacje!"
    jump dobrytarot
    
    label Magazyn:
        scene zamknietedrzwi with fade
        "Drzwi do magazynu są zamknięte na klucz."
        jump game_intro

label dobrytarot:
    scene ciemnasala with fade
    show ali2 at right
    
    a "UDAŁO NAM SIĘ!!!!!!!!"
    a "SPADAMY STĄD"
    jump pietro2

    label Sala101:
        scene sala1 with fade
        show adada at center
    librarian "Nie powinieneś tutaj być..."
    librarian "Jeśli chcesz się stąd wydostać, musisz rozwiązać zagadki skrywane w tej bibliotece."
    librarian  "Jedna z nich znajduje sie tutaj ! Powodzenia  "
    hide librarian
    " Ja " " Te ksiązki w oddali wygladaja trochę dziwnie, rzuce na nie okiem "
    menu:
        "Przyjrzyj sie bliżej ksiązkom":
            jump książki
        "Wróć do głownego holu":
            jump game_intro
    

    default selected_books = []

    label książki:
    scene ksiazki with fade
    if not persistent.books_described:
        "Na półce widzisz pięć książek z następującymi tytułami:"
        "1. 'Wiedźmin 3: Dziki Gon'"
        "2. 'Cyberpunk: Edgerunners'"
        "3. 'Baldur's Gate III'"
        "4. 'Solo Leveling'"
        "5. 'Monster'"
        "Może w tych tytułach kryje się wskazówka. Spróbuj znaleźć fragmenty kodu ukryte w książkach."
        $ persistent.books_described = True  # Oznacza, że opis półek został wyświetlony
    menu:
        "Przyjrzyj się książce 1 ('Wiedźmin 3: Dziki Gon')":
            if "W" not in selected_books:
                $ selected_books.append("W")
                "Znalazłeś fragment kodu: W."
            else:
                "Już sprawdziłeś tę książkę."
            jump książki

        "Przyjrzyj się książce 2 ('Cyberpunk: Edgerunners')":
            "W tej książce nie ma fragmentu kodu."
            jump książki

        "Przyjrzyj się książce 3 ('Baldur's Gate III')":
            if "B" not in selected_books:
                $ selected_books.append("B")
                "Znalazłeś fragment kodu: B."
            else:
                "Już sprawdziłeś tę książkę."
            jump książki

        "Przyjrzyj się książce 4 ('Solo Leveling')":
            if "S" not in selected_books:
                $ selected_books.append("S")
                "Znalazłeś fragment kodu: S."
            else:
                "Już sprawdziłeś tę książkę."
            jump książki

        "Przyjrzyj się książce 5 ('Monster')":
            "W tej książce nie ma fragmentu kodu."
            jump książki

        "Sprawdź kod z zebranych liter":
            jump check_code


label check_code:
    
    if len(selected_books) == 3:
        $ entered_code = "".join(selected_books)
        if entered_code == "WSB":
            "Wpisałeś poprawny kod! Zamek na drzwiach magazynu otwiera się."
            $ selected_books = []  
            jump Magazynotwarty
        else:
            "Kod jest niepoprawny. Spróbuj ponownie."
            $ selected_books = []  
            jump książki
    else:
        "Nie masz jeszcze wszystkich fragmentów kodu. Spróbuj dalej."
        jump książki

label Magazynotwarty:
    scene library_room with fade
    $ magazyn_otwarty = True  # Otworzenie magazynu odblokowuje opcję przejścia na piętro
    if not persistent.opis_described:
        "Otwierasz drzwi do magazynu i wchodzisz do środka."
        "Znajdujesz się w nowym pokoju. Na biurku widzisz otwarty zeszyt z zagadką."
        "Wokół znajdują się regały pełne książek, oznaczone numerami od 1 do 5."
    $ persistent.opis_described = True
    menu:
        "Podejdź do zeszytu":
            jump notebook_hint

        "Zbadaj regał 1":
            jump shelf_1

        "Zbadaj regał 2":
            jump shelf_2

        "Zbadaj regał 3":
            jump shelf_3

        "Zbadaj regał 4":
            jump shelf_4

        "Zbadaj regał 5":
            jump shelf_5

        "Sprawdź hasło":
            jump solve_puzzle


label notebook_hint:
    "W zeszycie czytasz:"
    "\"Pierwsze słowo z trzeciej książki, drugie słowo z czwartej książki, trzecie słowo z piątej książki – to da ci odpowiedź.\""
    menu:
        "Wróć do magazynu":
            jump Magazynotwarty


label shelf_1:
    "Zbliżasz się do pierwszego regału. Na półce widzisz trzy książki."
    menu:
        "Otwórz książkę 1: 'Tajemnice Alchemii'":
            "Pierwsze słowo: Alchemia."
            jump shelf_1

        "Otwórz książkę 2: 'Historia Magii'":
            "Drugie słowo: Jest."
            jump shelf_1

        "Otwórz książkę 3: 'Zagadka Przeszłości'":
            "Pierwsze słowo: Klucz."
            jump shelf_1

        "Wróć do magazynu":
            jump Magazynotwarty


label shelf_2:
    "Zbliżasz się do drugiego regału. Na półce widzisz trzy książki."
    menu:
        "Otwórz książkę 5: 'Sztuka Wojny'":
            "Pierwsze słowo: Ukryty."
            jump shelf_2

        "Otwórz książkę 7: 'Podstawy Matematyki'":
            "Drugie słowo: Skrzynia."
            jump shelf_2

        "Otwórz książkę 9: 'Tajemnice Historii'":
            "Drugie słowo: Jest."
            jump shelf_2

        "Wróć do magazynu":
            jump Magazynotwarty


label shelf_3:
    "Zbliżasz się do trzeciego regału. Na półce widzisz dwie książki."
    menu:
        "Otwórz książkę 6: 'Klucz do Sukcesu'":
            "Pierwsze słowo: Kapsuła."
            jump shelf_3

        "Otwórz książkę 11: 'Ukryte Ścieżki'":
            "Trzecie słowo: Kieł."
            jump shelf_3

        "Wróć do magazynu":
            jump Magazynotwarty


label shelf_4:
    "Zbliżasz się do czwartego regału. Na półce widzisz trzy książki."
    menu:
        "Otwórz książkę 4: 'Sekrety Wszechświata'":
            "Drugie słowo: Jest."
            jump shelf_4

        "Otwórz książkę 8: 'Ukryte Wrota'":
            "Trzecie słowo: Sekret."
            jump shelf_4

        "Wróć do magazynu":
            jump Magazynotwarty


label shelf_5:
    "Zbliżasz się do piątego regału. Na półce widzisz trzy książki."
    menu:
        "Otwórz książkę 420: 'Alchemia Dnia Codziennego'":
            "Pierwsze słowo: Alchemia."
            jump shelf_5

        "Otwórz książkę 16: 'Ukryte Wrota'":
            "Trzecie słowo: Kamień."
            jump shelf_5

        "Wróć do magazynu":
            jump Magazynotwarty


label solve_puzzle:
    $ answer = renpy.input("Podaj rozwiązanie zagadki:").strip()

    if answer.lower() == "klucz jest ukryty":
        "Otworzyło się tajne przejście!"
        "Które prowadzi..."
        jump game_intro
    else:
        "To nie jest poprawna odpowiedź. Spróbuj ponownie."
        jump Magazynotwarty


label Sala_matematyczna:
    scene geometria_pokoj with fade
    $ Sala_matematyczna = True
    "Znajdujesz się w pomieszczeniu pełnym dziwnych przedmiotów. Na stole znajduje się zestaw figur geometrycznych."
    "Na kartce obok znajduje się zagadka: 'Ułóż figury w odpowiedniej kolejności kolorów, aby otworzyć drzwi. Wskazówki: Od zimnych do ciepłych.'"
    $ wybrane_kolory = []
    menu:
        "Kwadrat (czerwony)":
            $ wybrane_kolory.append("czerwony")
            jump Sala_matematyczna
        "Trójkąt (niebieski)":
            $ wybrane_kolory.append("niebieski")
            jump Sala_matematyczna
        "Koło (zielone)":
            $ wybrane_kolory.append("zielony")
            jump Sala_matematyczna
        "Prostokąt (żółty)":
            $ wybrane_kolory.append("żółty")
            jump Sala_matematyczna
        "Gwiazda (fioletowa)":
            $ wybrane_kolory.append("fioletowy")
            jump Sala_matematyczna
        "Serce (pomarańczowe)":
            $ wybrane_kolory.append("pomarańczowy")
            jump Sala_matematyczna
        "Przejdź dalej":
            jump sprawdz_odpowiedz

label sprawdz_odpowiedz:
    # Wyświetl pytanie i pobierz odpowiedź od użytkownika
    $ odpowiedz_input = renpy.input("Podaj kolejność kolorów: (np. żółty, niebieski, fioletowy, itd.)").strip()

    # Rozdziel odpowiedź na listę słów, usuwając dodatkowe spacje i zmieniając na małe litery
    $ odpowiedz_lista = [kolor.strip().lower() for kolor in odpowiedz_input.split(",")]

    # Definiujemy poprawną kolejność kolorów
    $ poprawna_kolejnosc = ["niebieski", "fioletowy", "zielony", "żółty", "pomarańczowy", "czerwony"]

    # Porównujemy listę odpowiedzi z poprawną kolejnością
    if odpowiedz_lista == poprawna_kolejnosc:
        "Zamek na drzwiach się otwiera! Przedmioty zostały ustawione w odpowiedniej kolejności kolorów."
        jump koniec
    else:
        "To nie jest poprawna kolejność kolorów. Spróbuj ponownie."
        jump Sala_matematyczna




label koniec:
    scene koniec with fade
    play music "end.mp3"

    show text "Gratulacje!" with dissolve

    "Udało Ci się dotrzeć do końca tej opowieści. Mamy nadzieję, że podróż była pełna emocji i wyzwań."

    pause 2

    show text "Gra została stworzona przez:" with dissolve
    pause 1

    show text "Dawid Karpiński" with dissolve
    pause 1

    show text "Pamiętaj, każda przygoda zaczyna się od pierwszego kroku, a sukces to suma małych zwycięstw." with dissolve
    pause 3

    show text "Dziękujemy za grę i do zobaczenia w kolejnych projektach!" with dissolve
    pause 3

    return

