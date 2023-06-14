import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


class TestWidgets:

	class TestAccordianPage:

		def test_accordian(selfs, driver):
			accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
			accordian_page.open()
			first_title, first_content = accordian_page.check_accordian('first')
			second_title, second_content = accordian_page.check_accordian('second')
			third_title, third_content = accordian_page.check_accordian('third')
			assert first_title == "What is Lorem Ipsum?" and first_content > 0
			assert second_title == "Where does it come from?" and second_content > 0
			assert third_title == "Why do we use it?" and third_content > 0

	class TestAutoCompletePage:
		def test_fill_multi_autocomplete(self, driver):
			autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
			autocomplete_page.open()
			colors = autocomplete_page.fill_input_multi()
			colors_result = autocomplete_page.check_color_in_multi()
			assert colors == colors_result

		def test_remove_value_from_multi(self, driver):
			autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
			autocomplete_page.open()
			autocomplete_page.fill_input_multi()
			count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
			assert count_value_before != count_value_after

		def test_fill_single_autocomplete(self, driver):
			autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
			autocomplete_page.open()
			color = autocomplete_page.fill_input_single()
			color_result = autocomplete_page.check_color_in_single()
			assert color == color_result


	class TestDatePickerPage:

		def test_change_date(self, driver):
			date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
			date_picker_page.open()
			value_data_before, value_date_after = date_picker_page.select_date()
			assert value_data_before != value_date_after


		def test_change_date_and_time(self, driver):
			date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
			date_picker_page.open()
			value_data_before, value_date_after = date_picker_page.select_date()
			print(value_date_after)
			print(value_data_before)
			assert value_data_before != value_date_after

	class TestSliderPage:
		def test_slider(self, driver):
			slider = SliderPage(driver, 'https://demoqa.com/slider')
			slider.open()
			before, after = slider.change_slider_value()
			assert before != after


	class TestProgressBarPage:
		def test_progress_bar(self, driver):
			progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
			progress_bar.open()
			#value_before, value_after = progress_bar.change_progress_bar_value()
			value_before, value_after = progress_bar.change_progress_bar_value_100()
			assert value_before != value_after

class TestTabsPage:

	def test_tabs(self, driver):
		tabs = TabsPage(driver, 'https://demoqa.com/tabs')
		tabs.open()
		what_content, origin_content, use_content = tabs.check_tabs()
		assert what_content != origin_content and what_content != use_content
