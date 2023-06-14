import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.slider_page_locators import SlidePageLocators, ProgressBarPageLocators
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
	TabsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
	locators = AccordianPageLocators()

	def check_accordian(self, accordian_num):
		accordian = {'first':
						 {'title': self.locators.SECTION_FIRST,
						  'content': self.locators.SECTION_CONTENT_FIRST},
					 'second':
						 {'title': self.locators.SECTION_SECOND,
						  'content': self.locators.SECTION_CONTENT_SECOND},
					 'third':
						 {'title': self.locators.SECTION_THIRD,
						  'content': self.locators.SECTION_CONTENT_THIRD},
					 }

		section_title = self.element_is_visible(accordian[accordian_num]['title'])
		section_title.click()
		try:
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		except TimeoutException:
			section_title.click()
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
	locators = AutoCompletePageLocators()

	def fill_input_multi(self):
		colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
		for color in colors:
			input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
			input_multi.send_keys(color)
			input_multi.send_keys(Keys.ENTER)
		return colors

	def remove_value_from_multi(self):
		count_value_before = len(self.element_are_presents(self.locators.MULTI_VALUE))
		remove_button_list = self.element_are_visible(self.locators.MULTI_VALUE_REMOVE)
		for value in remove_button_list:
			value.click()
			break
		count_value_after = len(self.element_are_presents(self.locators.MULTI_VALUE))
		return count_value_before, count_value_after

	def check_color_in_multi(self):
		color_list = self.element_are_presents(self.locators.MULTI_VALUE)
		colors = []
		for color in color_list:
			colors.append(color.text)
		return colors

	def fill_input_single(self):
		color = random.sample(next(generated_color()).color_name, k=1)
		input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
		input_single.send_keys(color)
		input_single.send_keys(Keys.ENTER)
		return color

	def check_color_in_single(self):
		color = self.element_is_visible(self.locators.SINGLE_VALUE)
		return [color.text]


class DatePickerPage(BasePage):
	locators = DatePickerPageLocators()

	def select_date(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_INPUT)
		value_data_before = input_date.get_attribute('value')
		input_date.click()
		self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
		self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		value_date_after = input_date.get_attribute('value')
		return value_data_before, value_date_after

	def select_date_and_time(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
		self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
		input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_after = input_date_after.get_attribute('value')
		return value_date_before, value_date_after

	def set_date_by_text(self, element, value):
		select = Select(self.element_is_presents(element))
		select.select_by_visible_text(value)

	def set_date_item_from_list(self, elements, value):
		item_list = self.element_are_presents(elements)
		for item in item_list:
			if item.text == value:
				item.click()
				break


class SliderPage(BasePage):
	locators = SlidePageLocators()

	def change_slider_value(self):
		value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
		self.action_drug_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
		value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		return value_before, value_after


class ProgressBarPage(BasePage):
	locators = ProgressBarPageLocators()

	def change_progress_bar_value(self):
		progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar.click()
		value_before = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		time.sleep(random.randint(1, 8))
		progress_bar.click()
		value_after = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after

	def change_progress_bar_value_100(self):
		progress_bar = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar.click()
		value_before = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		self.check_progress_bar()
		value_after = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after

	def check_progress_bar(self):

		try:
			value_succsess = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE_SUCCSESS).text
			if value_succsess == "100%":
				progress_bar_reset = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON_RESET)
				progress_bar_reset.click()
			else:
				time.sleep(1)  # Задержка выполнения на 1 секунду
				self.check_progress_bar()  # Рекурсивный вызов функции

		except TimeoutException:
			self.check_progress_bar()


class TabsPage(BasePage):
	locators = TabsPageLocators()

	def check_tabs(self):
		what_button = self.element_is_visible(self.locators.TABS_WHAT)
		origin_button = self.element_is_visible(self.locators.TABS_ORIGIN)
		use_button = self.element_is_visible(self.locators.TABS_USE)
		more_button = self.element_is_visible(self.locators.TABS_MORE)
		what_button.click()
		what_content = self.element_is_visible(self.locators.TABS_WHAT_CONTENT).text
		origin_button.click()
		origin_content = self.element_is_visible(self.locators.TABS_ORIGIN_CONTENT).text
		use_button.click()
		use_content = self.element_is_visible(self.locators.TABS_USE_CONTENT).text
		try:
			more_button.click()
			more_content = self.element_is_visible(self.locators.TABS_MORE_CONTENT).text
		except ElementClickInterceptedException:
			print('lol')
		return len(what_content), len(origin_content), len(use_content)



