from webdriver import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonTest(WebDriverBase):

    GIRIS_BUTONU = (By.ID , "nav-link-accountList")
    GIRIS_SAYFA_KONTROL = (By.ID, "a-autoid-0-announce")
    GIRIS_MAIL_INPUT = (By.ID, "ap_email")
    GIRIS_PASSWORD_INPUT = (By.ID, "ap_password")
    GIRIS_YAP_BUTON = (By.ID, "signInSubmit")
    GIRIS_YAPILDI_KONTROL = (By.CLASS_NAME, "nav-shortened-name")

    ARAMA_BARI = (By.ID, "twotabsearchtextbox")
    ARAMA_BUTONU = (By.CLASS_NAME, "nav-search-submit")
    URUN_SEC = (By.XPATH, "//div[@data-index='3']/div/div/div/div[2]/div[1]/div/div/span/a")

    URUN_SAYFA_KONTROL = (By.ID, "submit.add-to-cart-announce")
    URUN_LISTE_EKLE = (By.ID, "add-to-wishlist-button-submit")
    URUN_EKLE_WISH_LIST = (By.XPATH, '//*[@id="WLNEW_section_wlType"]/div[2]/div[2]/div/div/span/div/label/i')
    WISH_LIST_CREATE = (By.ID, "WLNEW_create")

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.amazon.com")
        self.girisYap()
        self.urunuBul("Samsung")
        self.urunuEkle()
        self.driver.quit()

    """Log In Function"""
    def girisYap(self):
        self.get_element(self.GIRIS_BUTONU).click()
        assert self.get_element(self.GIRIS_SAYFA_KONTROL).text == "Sign in"
        self.get_element(self.GIRIS_MAIL_INPUT).send_keys("erkanongur@hotmail.com")
        self.get_element(self.GIRIS_PASSWORD_INPUT).send_keys("23181113ss")
        self.get_element(self.GIRIS_YAP_BUTON).click()
        assert self.get_element(self.GIRIS_YAPILDI_KONTROL).text == "erkan"

    """Searching Product and Choosing Third Result"""
    def urunuBul(self, nesne):
        self.get_element(self.ARAMA_BARI).send_keys(nesne)
        self.get_element(self.ARAMA_BUTONU).click()
        self.get_element(self.URUN_SEC).click()
        assert self.get_element(self.URUN_SAYFA_KONTROL).text == "Add to Cart"

    """Adds Product to WishList"""
    def urunuEkle(self):
        self.get_element(self.URUN_LISTE_EKLE).click()
        """self.get_element(self.URUN_EKLE_WISH_LIST).click()"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.WISH_LIST_CREATE))
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.WISH_LIST_CREATE))
        self.get_element(self.URUN_EKLE_WISH_LIST).click()
        self.get_element(self.WISH_LIST_CREATE).click()
AmazonTest()

