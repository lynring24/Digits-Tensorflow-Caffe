from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
import heapq, numpy as np
from sklearn.metrics import accuracy_score

browser = webdriver.Chrome()
browser.get('http://localhost:5000/models/20180705-154809-8bc1')
browser.implicitly_wait(3)
time.sleep(5)

# select extracted.txt for test data set
browser.find_element_by_id('image_list').send_keys("D:/Crawler/extracted.txt")

button = browser.find_element_by_name('classify-many-btn')
browser.execute_script("arguments[0].setAttribute('formtarget','_self')", button)
button.click()
# crawl the result
wait = WebDriverWait(browser, 60);
time.sleep(60)
rows = browser.find_elements_by_tag_name('tr')
print (rows.__len__())
print(browser.current_url)
y_true = []
y_pred = []
for row in rows[1:]:
    cols = row.find_elements_by_tag_name('td')
    expected = []
    for i in range(0, 5):
        expected.append([int(cols[2*i+2].text), float(cols[2*i+3].text[:-1])])
    argmax = heapq.nlargest(1, expected, lambda s: s[1])[0][0]
    print(cols[0].text)
    y_true.append(int(cols[1].text.encode("utf-8")[14]))
    y_pred.append(argmax)

print(accuracy_score(y_true, y_pred))
# after extract the index, count the accuracy
with open('accuracy.txt', 'w') as dest:
    dest.write('accuracy: ', str(accuracy_score(y_true, y_pred)))