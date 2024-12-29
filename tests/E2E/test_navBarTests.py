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

class TestNavBarTests():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("http://127.0.0.1:5000/contacts")
    self.driver.set_window_size(1936, 1048)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_navBarContacts(self):
    '''
    test to check if the contacts link is working by clicking on the Website's name
    '''
    self.driver.find_element(By.LINK_TEXT, "Contactos").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Contacts"
    
    
  
  def test_navBarNewContact(self):
    '''
    test to check if the new contact link is working by clicking on the New Contact button
    '''
    self.driver.find_element(By.LINK_TEXT, "New").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "New contact"
  
  
  
  
  def test_navBarViewContacts(self):
    '''
    test to check if the view contacts link is working by clicking on the View Contacts button
    '''
    self.driver.find_element(By.LINK_TEXT, "View contacts").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Contacts"
  
