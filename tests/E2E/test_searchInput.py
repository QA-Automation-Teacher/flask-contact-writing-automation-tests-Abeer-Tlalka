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
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
class TestSearchInput():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("http://127.0.0.1:5000/contacts")
    self.driver.set_window_size(1936, 1048)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchInputNameExist(self):
    '''
    test to check if the search input is working by searching for a name that exists , and then checking if the name is displayed in the first row of the table
    '''
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("abeer")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text == "abeer"
  
  def test_searchInputNameDoesNotExist(self):
    '''
    test that checks if the search input is working by searching for a name\n that does not exist, and then checking if the table is empty
    '''
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("alex")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    # CHECK IF THE TABLE IS EMPTY
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.table-hover tbody"))
    )
    tbody = self.driver.find_element(By.CSS_SELECTOR, "table.table-hover tbody")

    # Check if tbody has no child tr elements
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    assert len(rows) == 0, "Table is  empty"

  
  def test_searchInputEmpty(self):
    '''
    test that checks if the search input is working by searching for an empty string,\n and then checking if the table showed all the contacts
    becuse there is no name to search for
    '''
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    
    # CHECK IF THE TABLE IS EMPTY
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.table-hover tbody"))
    )
    tbody = self.driver.find_element(By.CSS_SELECTOR, "table.table-hover tbody")

    # Check if tbody has no child tr elements
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    assert len(rows) != 0, "Table is not empty"
