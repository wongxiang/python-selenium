# coding:utf-8
import unittest;
import time;
from selenium import webdriver;

driver=webdriver.Chrome();
driver.get("http://www.baidu.com");
time.sleep(5);
driver.refresh();
time.sleep(5);
driver.get("http://sports.sina.com.cn");
time.sleep(5);
driver.back();
time.sleep(5);
driver.forward();
time.sleep(5);
driver.set_window_size(540,960);
time.sleep(5);
driver.maximize_window();
time.sleep(5);
driver.get_screenshot_as_file("D:\\workspace\\python\\test\\screenshot\\1.png");
driver.close();
driver.quit();

