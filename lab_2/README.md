# Wstęp do Multimediów

Laboratorium 2 | Dźwięk

# 1. Analiza widma i spektrogramu dźwięków

### 1. Pojedyncze tony
- Wygeneruj ton o częstotliwości 1000 Hz i amplitudzie 0,5
- Wyświetl widmo sygnału (Analizuj - Narysuj widmo) i sprawdź, jaki wpływ na wygląd widma ma zmiana rozmiaru okna analizy widmowej (Rozmiar: …)
- Sprawdź, jaki wpływ na widmo sygnału ma rodzaj zastosowanego okna (Funkcja: …)

- Klikając czarny trójkąt przy nazwie ścieżki zmień widok na „Spektrogram”
- Zaobserwuj, jak wygląda spektrogram dla wygenerowanego tonu (pojedynczej częstotliwości)

- Wygeneruj kolejny ton (będąc „odklikniętym” z poprzedniej ścieżki), o częstotliwości 2000 Hz i amplitudzie 0,3
- Zaznacz obie ścieżki i w menu wybierz Ścieżki – Miksuj – Miksuj i renderuj
- Zaobserwuj, jak wygląda spektrogram

### 2. Dźwięki muzyczne
- Zaimportuj ścieżkę „flet.wav”
- Posłuchaj i wyświetlając widmo sygnału, sprawdź, jaka jest częstotliwość dźwięku, który gra flecistka
- Zaobserwuj, jak wygląda na spektrogramie dźwięk instrumentu muzycznego – zwróć uwagę na występowanie wielu częstotliwości harmonicznych (wielokrotności częstotliwości podstawowej)

- Zaimportuj ścieżkę „oboj_piano.wav” oraz osobno „oboj_forte.wav”
- Posłuchaj kolejno każdej ze ścieżek i zobacz na spektrogramie, w jaki sposób różnica w barwie dźwięku pomiędzy instrumentem grającym cicho (piano) i głośno (forte) widoczna jest na spektrogramie

- Zaimportuj ścieżkę „waltornia.wav”
- Zmień pionową skalę spektrogramu z liniowej na logarytmiczną (kliknięcie prawym przyciskiem myszy na skali po lewej stronie wykresu) i słuchając nagrania zobacz, jak na spektrogramie widoczna jest melodia, którą gra waltornista.

### 3. Mowa
- Zaimportuj ścieżkę „mowa_mezczyzna.wav” oraz osobno „mowa_kobieta.wav”
- Na podstawie widma obu sygnałów przeanalizuj, w jakich zakresach częstotliwości więcej energii ma dźwięk mowy męskiej, a w jakich mowy kobiecej (lepiej będzie to widać ustawiając liniową skalę poziomą wykresu)

# 2. Edycja dźwięków

### 1. Mowa
- Otwórz ścieżkę „mowa_kobieta.wav” oraz osobno „mowa_mezczyzna.wav”
- Zastosuj filtrację górnoprzepustową (zaznacz ścieżkę, Efekt – Filtr górnoprzepustowy) do ścieżki z mową kobiecą, tj. odfiltruj dolne częstotliwości dźwięku, stosując ustawienia: częstotliwość graniczna 200 Hz, rolloff 24 dB/oktawę
- Zobacz różnicę w widmie przed i po filtracji. Posłuchaj ścieżki mowy kobiecej po filtracji – czy utracona została jakaś istotna część sygnału?
- Zastosuj taką samą filtrację górnoprzepustową (te same parametry), do mowy męskiej. Zaobserwuj widmo przed i po filtracji. Posłuchaj ścieżki mowy męskiej – czy przy filtracji utracona została istotna część sygnału w porównaniu do mowy kobiecej?

- Do mowy kobiecej zastosuj dodatkowo filtrację dolnoprzepustową, tj. odfiltruj wysokie częstotliwości sygnału, stosując ustawienia np: 8 000 Hz, 24 db/okt
- Stosując różne wartości częstotliwości granicznej filtru, sprawdź, przy jakiej częstotliwości utracona zostaje wyrazistość mowy, a przy jakiej zrozumiałość.

### 2. Eliminacja zakłóceń

- Zaimportuj ścieżkę „ton_trzaski.wav” i posłuchaj – w nagraniu znajduje się ton i zakłócenia (trzaski)
- Przełącz widok ścieżki na spektrogram, zaobserwuj występowanie trzasków, które nie były widoczne na przebiegu czasowym sygnału, a następnie ponownie rozwiń menu przy nazwie ścieżki i włącz „Ustawienia spektrogramu”.
- Sprawdź, jak rozmiar okna analizy fft wpływa na wygląd spektrogramu. Zmieniaj po kolei rozmiar okna z 1024 na coraz mniejsze, a później coraz większe i zobacz, który rozmiar jest najlepszy dla uzyskania największej rozdzielczości w dziedzinie czasu (pozioma oś), a który zapewnia najlepszą rozdzielczość w dziedzinie częstotliwości (pionowa oś).

- Przy optymalnych ustawieniach okna analizy dla widoczności trzasków (których czas trwania jest bardzo krótki) spróbuj usunąć zakłócenia w następujący sposób:
    1. W widoku spektrogramu zaznacz fragment, w który występuje trzask
    2. Przełącz widok na przebieg czasowy
    3. W menu wybierz Zaznacz – Na miejscach przejść przez zero (to pozwoli uniknąć nieciągłości sygnału na krańcach zaznaczenia)
    4. Usuń zaznaczony fragment (pojedynczy trzask) naciskając delete
    5. Posłuchaj nowej wersji ścieżki

(więcej szczegółów dot. usuwania trzasków tutaj: https://manual.audacityteam.org/man/click_removal_using_the_spectrogram_view.html)


- Zaimportuj ścieżkę „gitara_pisk.wav”
- Zaobserwuj na spektrogramie, jakiego rodzaju zakłócenie występuje w tym nagraniu i spróbuj je usunąć w następujący sposób:
    1. Zaznacz odpowiedni fragment spektrogramu (dany zakres częstotliwości w całym czasie trwania zakłócenia)
    2. Spróbuj usunąć zakłócenie używając filtra notch (Efekt – Filtr Notch) o odpowiednich parametrach
    3. Posłuchaj nowej wersji ścieżki

(więcej szczegółów dot. usuwania trzasków tutaj: https://manual.audacityteam.org/man/spectral_selection.html#Example_of_using_spectral_editing_to_remove_an_unwanted_whistle_noise)

# 3. Lateralizacja źródła dźwięku

- Do tego zadania niezbędne są słuchawki!
- Zaimportuj ścieżkę „lektor.wav”
- Zaznacz zaimportowaną ścieżkę i powiel ją (Edycja – Powiel)
- Jedną ze ścieżek ustaw w panoramie (suwak L – P pod nazwą ścieżki) na prawo, a drugą na lewo
- Kliknij kursorem w jakieś miejsce ścieżki, gdzie amplituda sygnału jest duża
- Klikając „lupkę” przybliż przebieg czasowy tak, aby na skali były tysięczne części sekundy
- Zmień typ kursora na poziomą podwójną strzałkę (↔)
- Przesuń jedną ze ścieżek w prawo lub w lewo o tysięczne części sekundy
- Posłuchaj, jak po przesunięciu zmienia się położenie pozornego źródła dźwięku
- Jeśli przesuniesz ścieżkę o zbyt dużą wartość, zniknie wrażenie przesuwania się źródła dźwięku, a powstanie wrażenie „echa”

# 4. Próbkowanie i kwantyzacja
- zaimportuj pliki "drums_sweep.wav", " drums_sweep_convert_Fs11025Hz.wav" i "drums_sweep_convertFs11025Hz_filtering.wav"
- posłuchaj i oceń brzmienie każdego pliku (drugi z nich to konwersja z fs = 44 100 Hz na 11 025 Hz bez odpowiedniej filtracji sygnału, a trzeci to konwersja z 44 100 Hz na 11 025 Hz, ale z włączoną filtracją anty-aliasingową),
- posłuchaj, czy słyszysz składowe, które ni występowały w oryginalnym sygnale?
- zobaczyć na spektrogramie w jaki sposób wygląda aliasing na granicy pasma.

- zaimportuj pliki "drums.wav", "drums_8bits.wav" i "drums_8bits_dith1.0.wav"
- posłuchaj i oceń wybrzmiewanie uderzenia stopy i werbla oraz brzmienia talerzy po kwantyzacji do 8 bitów
- posłuchaj i oceń wybrzmiewanie uderzenia stopy i werbla oraz brzmienia talerzy po kwantyzacji do 8 bitów, ale z dodaniem sygnału dither'a. Czy odzyskało wybrzmienie, ale kosztem mniejszego SNR?
- obejrzyj i porównaj spektrogramy każdego sygnału (najlepiej ustawienia: Gain-0dB, Range120dB, Max Freq-22000Hz, Windows size - 4096, Windows type: Blackman Harris)