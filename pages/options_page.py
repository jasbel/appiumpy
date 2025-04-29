from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from locators.accessibility_ids import AX

class OptionsPage(BasePage):
    # ------------ Locators base ------------
    TAB_TITLE = (AppiumBy.ACCESSIBILITY_ID, AX.TabTop.TITLE)

    HOME = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.HOME)
    TEMPORARY = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.TEMPORARY)
    TRANSACTIONS = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.TRANSACTIONS)
    OPTIONS = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.OPTIONS)
    
    OPTION_ITEM_LANGUAGE = (AppiumBy.ACCESSIBILITY_ID,  AX.Options.ITEM_LANGUAGE)
    OPTION_ITEM_PROOFS = (AppiumBy.ACCESSIBILITY_ID,  AX.Options.PROOFS)
    OPTION_PRIVACY_POLICY = (AppiumBy.ACCESSIBILITY_ID,  AX.Options.PRIVACY_POLICY)

    LANGUAGE_ITEM = (AppiumBy.ACCESSIBILITY_ID, AX.Options.ITEM_LANGUAGE)
    PRIVACY_POLICY = (AppiumBy.ACCESSIBILITY_ID, AX.Options.PRIVACY_POLICY)

    # ------------ Métodos generales ------------

    
    def open_language(self):
        self.click(self.LANGUAGE_ITEM)

    def navigate_tabs(self):
        """Click en cada TabBottom y verificar su título"""
        pass

    def verify_tab_titles(self):
        """Verifica que el título sea el esperado para cada tab"""
        pass

    def go_to_home_tab(self):
        """Navega al tab Home"""
        pass

    def verify_home_buttons(self):
        """Verifica existencia de botones NFC y Mobile en Home"""
        pass

    def verify_home_card(self):
        """Verifica existencia de la tarjeta 'Card and trips view' en Home"""
        pass

    def go_to_options_tab(self):
        """Navega al tab Options"""
        pass

    def explore_options_items(self):
        """Explora todos los items del tab Options"""
        pass

    def verify_options_content(self):
        """Verifica que los contenidos mostrados sean correctos"""
        pass

    def select_language_option(self):
        """Clic en opción Language"""
        pass

    def verify_languages_exist(self):
        """Verifica existencia de radio buttons para idiomas"""
        pass

    def verify_default_language(self):
        """Verifica que English esté seleccionado por defecto"""
        pass

    def select_proofs_option(self):
        """Clic en opción Proofs"""
        pass

    def verify_proofs_toggles(self):
        """Verifica existencia de toggles en Proofs"""
        pass

    def explore_bottom_section(self):
        """Navega hasta la parte inferior del Options"""
        pass

    def verify_privacy_policy_button(self):
        """Verifica existencia del botón Privacy Policy"""
        # assert self.is_visible(self.PRIVACY_POLICY)
        pass
