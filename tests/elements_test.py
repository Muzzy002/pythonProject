import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
	UploadAndDownloadPage


class TestElements:
	class TestTextBox:

		def test_text_box(self, driver):
			test_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
			test_box_page.open()
			full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()
			output_full_name, output_email, output_current_address, output_permanent_address = test_box_page.check_filled_form()

			for i in full_name, email, current_address, permanent_address:
				print('\n' + i)

			assert full_name == output_full_name, "NAME FAILED"
			assert email == output_email, "EMAIL FAILED"
			assert current_address == output_current_address, "CUR ADR FAILED"
			assert permanent_address == output_permanent_address, "PER ADR FAILED"

	class TestCheckBox:
		def test_check_box(self, driver):
			check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
			check_box_page.open()
			check_box_page.open_full_list()
			check_box_page.click_random_checkbox()
			input_checkbox = check_box_page.get_checked_checkboxes()
			output_result = check_box_page.get_output_result()
			assert input_checkbox == output_result, "Тест по чек боксам не прошел"

	class TestRadioButton:

		def test_radio_button(self, driver):
			radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
			radio_button_page.open()
			radio_button_page.click_on_the_radio_button("yes")
			output_yes = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button("impressive")
			output_impressive = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button("no")
			output_no = radio_button_page.get_output_result()
			assert output_yes == "Yes", "'Yes' have no been selected"
			assert output_impressive == "Impressive", "'Impressive' have no been selected"
			assert output_no == "No", "'No' have no been selected"

	class TestWebTable:

		def test_web_table_add_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			new_person = web_table_page.add_new_person()
			table_result = web_table_page.check_new_added_person()
			assert new_person in table_result, "ABRAKADABRA"

		def test_web_table_search_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			key_word = web_table_page.add_new_person()[random.randint(0, 5)]
			web_table_page.search_some_person(key_word)
			table_result = web_table_page.check_search_person()
			print(key_word, table_result)
			assert key_word in table_result

		def test_web_table_person_info(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			lastname = web_table_page.add_new_person()[1]
			web_table_page.search_some_person(lastname)
			age = web_table_page.update_person_info()
			row = web_table_page.check_search_person()
			assert age in row, "person card has not been changed"

		def test_web_table_dalete_person(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			email = web_table_page.add_new_person()[3]
			web_table_page.search_some_person(email)
			web_table_page.delete_person()
			text = web_table_page.check_deleted()
			assert text == "No rows found"

		def test_web_table_change_count_row(self, driver):
			web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
			web_table_page.open()
			count = web_table_page.select_up_to_some_rows()
			assert count == [5, 10, 20, 25, 50, 100], "Все гуд только на сайте баг"

	class TestButtonPage:

		def test_different_click_on_the_buttons(self, driver):
			button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
			button_page.open()
			button_page.random_click_on_different_button()
			time.sleep(5)

	class TestLinkPage:

		def test_check_link(self, driver):
			links_page = LinksPage(driver, 'https://demoqa.com/links')
			links_page.open()
			href_link, current_url = links_page.check_new_tab_simple_link()
			assert href_link == current_url, "the link is broken or url is incorrect"

		def test_broken_link(self, driver):
			links_page = LinksPage(driver, "https://demoqa.com/links")
			links_page.open()
			response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
			assert response_code == 400, 'test_broken_link наебнулся'

	class TestUploadANDDownload:

		def test_upload_file(self, driver):
			upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
			upload_page.open()
			file_name, result = upload_page.update_file()
			assert file_name == result

		def test_download_file(self, driver):
			upload_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
			upload_page.open()
			check = upload_page.download_file()
			assert check is True
