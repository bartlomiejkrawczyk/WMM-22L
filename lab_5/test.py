
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt


skip_wnd = False


def printi(img, img_title="image"):
    """ Pomocnicza funkcja do wypisania informacji o obrazie. """
    print(f"{img_title}, wymiary: {img.shape}, typ danych: {img.dtype}, wartości: {img.min()} - {img.max()}")


def cv_imshow(img, img_title="image"):
    """
    Funkcja do wyświetlania obrazu w wykorzystaniem okna OpenCV.
    Wykonywane jest przeskalowanie obrazu z rzeczywistymi lub 16-bitowymi całkowitoliczbowymi wartościami pikseli,
    żeby jedną funkcją wywietlać obrazy różnych typów.
    """
    # cv2.namedWindow(img_title, cv2.WINDOW_AUTOSIZE) # cv2.WINDOW_NORMAL

    if (img.dtype == np.float32) or (img.dtype == np.float64):
        img_ = img / 255
    elif img.dtype == np.int16:
        img_ = img*128
    else:
        img_ = img
    cv2.imshow(img_title, img_)
    # oczekiwanie przez bardzo krótki czas - okno się wyświetli, ale program się nie zablokuje, tylko będzie kontynuowany
    cv2.waitKey(1)


""" Wczytanie obrazu z pliku """
image = cv2.imread("./images/latarnia2_mono.png", cv2.IMREAD_UNCHANGED)
printi(image, "image")

"""
Obliczenie średniej bitowej dla pliku .png
os.stat() podaje rozmiar pliku w bajtach, a potrzebny jest w bitach (-> '8*')
"""
bitrate = 8*os.stat("./images/latarnia2_mono.png").st_size / \
    (image.shape[0]*image.shape[1])
print(f"bitrate: {bitrate:.4f}")

"""
Obliczanie entropii
"""


def calc_entropy(hist):
    pdf = hist/hist.sum()  # normalizacja histogramu -> rozkład prawdopodobieństwa; UWAGA: niebezpieczeństwo '/0' dla 'zerowego' histogramu!!!
    # entropy = -(pdf*np.log2(pdf)).sum() ### zapis na tablicach, ale problem z '/0'
    entropy = -sum([x*np.log2(x) for x in pdf if x != 0])
    return entropy


hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])
"""
cv2.calcHist() zwraca histogram w postaci tablicy 2D,
do dalszego przetwarzania wygodniejsza może być tablica jednowymiarowa -> flatten().
"""
hist_image = hist_image.flatten()
# print(hist_image.sum(), 512*512) ### dla sprawdzenia: suma wartości histogramu powinna być równa liczbie pikseli w obrazie

H_image = calc_entropy(hist_image)
print(f"H(image) = {H_image:.4f}")


"""
Obraz różnicowy
"""


"""
Predykcja w kierunku poziomym:
od wartości danego piksela odejmowana jest wartość piksela z lewej strony - 'lewego sąsiada' (operacje na kolumnach).
Operację taką można wykonać dla pikseli leżących w drugiej i kolejnych kolumnach obrazu, z pominięciem skrajnie lewej kolumny.
"""
img_tmp1 = image[:,
                 1:]  # wszystkie wiersze (':'), kolumny od 'pierwszej' do ostatniej ('1:')
# wszystkie wiersze, kolumny od 'zerowej' do przedostatniej (':-1')
img_tmp2 = image[:, :-1]

"""
W wyniku odejmowania pojawią się wartości ujemne - zakres wartości pikseli w obrazie różnicowym to będzie [-255, 255],
dlatego trzeba zminić typ wartości pikseli, żeby zakres wartości nie ograniczał się do [0, 255];
może to być np. cv2.CV_16S (odpowiednio np.int16 w NumPy), żeby pozostać w domenie liczb całkowitych.
"""
image_hdiff = cv2.addWeighted(img_tmp1, 1, img_tmp2, -1, 0, dtype=cv2.CV_16S)
printi(image_hdiff, "image_hdiff")
"""
image_hdiff ma o jedną kolumnę mniej - dla skrajnie lewej kolumny nie było danych do odejmowania,
kolumnę tę można potraktować oddzielnie i 'połączyć' wyniki.
"""
image_hdiff_0 = cv2.addWeighted(
    image[:, 0], 1, 0, 0, -127, dtype=cv2.CV_16S)  # od 'zerowej' kolumny obrazu oryginalnego odejmowana stała wartość '127'
printi(image_hdiff_0, "image_hdiff_0")
# połączenie tablic w kierunku poziomym, czyli 'kolumna za kolumną'
image_hdiff = np.hstack((image_hdiff_0, image_hdiff))
printi(image_hdiff, "image_hdiff")

"""
Funkcja cv2.imshow() zakłada inny zakres wartości pikseli w zależności od typu danych;
żeby uzyskać poprawne wyświetlanie obrazów z 16-bitowymi wartościami pikseli należy wartości pikseli
pomnożyć przez 128 (zmiana zakresu z [-255, 255] na [-32640, 32640], co pokrywa prawie cały zakres wartości dostępnych
dla 16-bitowych liczb całkowitych).
"""
cv2.imshow("image_hdiff not scaled",
           image_hdiff)  # obraz 'całkowicie szary', co odpowiada wartościom bliskim 0
# obraz z widocznymi zmianami, czerń - wartość minimalna (ujemna), szrość - poziom 0, biel - wartość maksymalna
cv2.imshow("image_hdiff scaled", image_hdiff*128)
# zdefiniowana funkcja pomocnicza odpowiednio 'obsługuje' obrazy z 16-bitowymi wartościami
cv_imshow(image_hdiff, "image_hdiff")

cv2.waitKey(0)  # oczekiwanie na reakcję użytkownika
cv2.destroyAllWindows()  # należy pamiętać o zniszczeniu okien na końcu programu
