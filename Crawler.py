from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://localhost:5000/models/images/classification/new')
browser.implicitly_wait(3)
time.sleep(5)

# submit username
browser.find_element_by_id('username').send_keys('et')
browser.find_element_by_name('login-button').click()
browser.implicitly_wait(3)

# select dataset
browser.find_element_by_xpath('//*[@id="dataset"]/option').click()

# fill inputs
train_epochs = browser.find_element_by_id('train_epochs')
train_epochs.clear()
train_epochs.send_keys(30)

snapshot_interval = browser.find_element_by_id('snapshot_interval')
snapshot_interval.clear()
snapshot_interval.send_keys(str(1.0))

val_interval = browser.find_element_by_id('val_interval')
val_interval.clear()
val_interval.send_keys(str(1.0))

# browser.find_element_by_id('random_seed').__setattr__()

batch_size = browser.find_element_by_id('batch_size')
batch_size.clear()
batch_size.send_keys(str(50))

# browser.find_element_by_id('batch_accumulation').__setattr__()
solver_type = Select(browser.find_element_by_id('solver_type'))
solver_type.select_by_index(0)

# standard networks
browser.find_element_by_id('standard_networks-0').click()
# standard_networks-1 / standard_networks-2

elements = [train_epochs, snapshot_interval, val_interval, batch_size]
model_name = ""
for element in elements:
    model_name = model_name + element.get_attribute('value').encode('utf-8')+"_"
model_name = model_name + solver_type.first_selected_option.text

browser.find_element_by_id('model_name').send_keys(model_name)
browser.find_element_by_name('create-model').click()
# submit creation

# wait until the creation is done
while True:
    text_success = browser.find_element_by_class_name('text-success').text
    if text_success == 'Done' : break;

# select extracted.txt for test data set
browser.find_element_by_id('image_list').send_keys("extracted.txt")

