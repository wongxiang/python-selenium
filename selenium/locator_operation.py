# coding:utf-8
import unittest;
import time;
from selenium import webdriver;

driver=webdriver.Chrome();
driver.find_element_by_id("id");
driver.find_element_by_name("name");
driver.find_element_by_class_name("classname");
driver.find_element_by_tag_name("tag name");
driver.find_element_by_link_text("link text");
driver.find_element_by_partial_link_text("text");
driver.find_element_by_xpath("xpath");
driver.find_element_by_css_selector();


