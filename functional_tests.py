import selenium
import unittest
from selenium import webdriver
import vars


# ________________________________________________________________________
# Chapter 1 Tutorial
# browser = webdriver.Firefox()

# browser.get(vars.my_localhost)

# try:
#     assert 'To-Do' in browser.title, "Browser title was " + browser.title
#     print("Django success")
# except:
#     print("Django didn't work")

# browser.quit()

# ________________________________________________________________________
# Chapter 2 tutorial
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8080')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
