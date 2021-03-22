from selenium.webdriver.common.by import By
import time

# Текст на кнопке на разных локалях
text_translate = {
    "ar": "أضف الى سلة التسوق",
    "ca": "Afegeix a la cistella",
    "cs": "Vložit do košíku",
    "da": "Læg i kurv",
    "de": "In Warenkorb legen",
    "en-gb": "Add to basket",
    "el": "Προσθήκη στο καλάθι",
    "es": "Añadir al carrito",
    "fi": "Lisää koriin",
    "fr": "Ajouter au panier",
    "it": "Aggiungi al carrello",
    "ko": "장바구니 담기",
    "nl": "Voeg aan winkelmand toe",
    "pl": "Dodaj do koszyka",
    "pt": "Adicionar ao carrinho",
    "pt-br": "Adicionar à cesta",
    "ro": "Adauga in cos",
    "ru": "Добавить в корзину",
    "sk": "Pridať do košíka",
    "uk": "Додати в кошик",
    "zh-cn": "Add to basket"}


def test_button_add_to_basket_avalable(browser, language):
    link = "http://selenium1py.pythonanywhere.com/" + language + "/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".add-to-basket>button")
    # Проверка наличия надписи на кнопке и ее соотвествия ожидаемой надписи
    button_name = button.text
    url_button_name = text_translate.get(language)
    assert button_name == url_button_name, "Button isn't available"

# pytest -s -v --language=en-gb test_items.py
# pytest -s -v --language=fr test_items.py

