import time

from pages.elements_page_bazar import ViyarBazarPage, ReviewsBazarPage


class TestElementsBazara:
	class TestVicarBazaar:

		def test_viyar_register(self, driver):
			viyar_page = ViyarBazarPage(driver, "https://viyarbazar.com/")
			viyar_page.open()
			viyar_page.register_on_bazar_viyar()
			viyar_page.viyti_s_akka()
			email_input = viyar_page.avtorizacion()
			viyar_page.after_register_viyar()
			email_output = viyar_page.check_email_in()
			assert email_input == email_output, "Почты разные почему то"
			time.sleep(5)

		def test_viyar_gallery(self, driver):
			gallery_page = ViyarBazarPage(driver, "https://viyarbazar.com/")
			gallery_page.open()
			gallery_page.avtorizacion()
			gallery_page.click_on_gallery()
			gallery_page.random_sort()
			gallery_page.button_more()
			click_on_portfolio = gallery_page.random_portfolio()
			check_portfolio_maker = gallery_page.check_maker()
			assert check_portfolio_maker == click_on_portfolio, "Что то с порфтолио не так"

		def test_viyar_reviews(self, driver):
			viyar_page = ReviewsBazarPage(driver, "https://viyarbazar.com/")
			viyar_page.open()
			viyar_page.click_on_button_reviews()
			viyar_page.open_and_random_filter()
			viyar_page.check_filter()
