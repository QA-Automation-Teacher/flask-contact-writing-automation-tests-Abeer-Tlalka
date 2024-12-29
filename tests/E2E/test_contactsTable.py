import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class TestContactsTable():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("http://127.0.0.1:5000/contacts")
    self.driver.set_window_size(1260, 665)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_contactsTableDeleteButtonMessage(self):
    '''
    test that checks if the delete button is working by clicking on the delete button\n and then checking if the delete message is displayed
    '''
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".popover-title")
    assert len(elements) > 0
  
  def test_contactsTableDeleteButtonNoProcess(self):
    '''
    test that checks if clicking on the no button in the delete popover will close the popover
    '''
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
    self.driver.find_element(By.LINK_TEXT, "No").click()
    # Wait for the popover to disappear
    WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".popover-title"))
    )

    # Assert that the popover is not visible
    popovers = self.driver.find_elements(By.CSS_SELECTOR, ".popover-title")
    assert len(popovers) == 0 or not popovers[0].is_displayed(), "Popover is still visible"
  
  def test_contactsTableDeleteButtonYesProcess(self):
    '''
    test that checks if clicking on the yes button in the delete popover will delete the contact\n and the message "Deleted successfully." will be displayed
    '''
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .btn-danger").click()
    self.driver.find_element(By.LINK_TEXT, "Yes").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "Deleted successfully."
  
  def test_contactsTableEditButton(self):
    '''
    test that chick if the edit button is working by clicking on the edit button\n and then checking if the edit contact page is displayed
    '''
    self.driver.find_element(By.LINK_TEXT, "Edit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Edit contact"
  
  def test_contactsTableHeadTitle(self):
    '''
    test that check if the table head has the correct titles
    '''
    assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").text == "Name"
    assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(2)").text == "Surname"
    assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3)").text == "E-Mail"
    assert self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").text == "Phone"
  
