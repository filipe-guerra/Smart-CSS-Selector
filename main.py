import time
import numpy as np
import pandas as pd
from selenium import webdriver


def get_one_ocorrence(s, item):
    _mask = s.groupby(item)[item].transform('size') == 1
    _one_occurrence = s[item].where(_mask)

    return _one_occurrence


driver = webdriver.Chrome(r"C:\Users\Filipe\Documents\source\smart css selector\chromedriver.exe")
driver.get("http://www.python.org")
# assert "Python" in driver.title

time.sleep(5)
found_elements = driver.find_elements_by_css_selector('*')

list_of_elemets = []
for element in found_elements:
    d = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
    d['tag_name'] = element.tag_name
    list_of_elemets.append(d)

len(list_of_elemets)

target = ['class', 'tag_name', 'href', 'name', 'src',
          'type', 'title', 'media', 'id', 'value']

s = pd.DataFrame.from_dict(list_of_elemets)

# Class list analyse
classes = s['class'].fillna('').str.split(' ')
class_list = [item for sublist in classes.tolist() for item in sublist]
class_list_dataframe = pd.DataFrame(class_list) 
class_items_one_occurence = class_list_dataframe.value_counts()[class_list_dataframe.value_counts() == 1]

tag_name_mask = s.groupby('tag_name')['tag_name'].transform('size') == 1
tag_name_one_occurrence = s.tag_name.where(tag_name_mask)
href = get_one_ocorrence(s, 'href')

# pd.DataFrame(s, index=[0])

# first_tag = pd.DataFrame(s, index=[0])['tag_name'][0]

# class_list = s['class'].tolist()

# for item in class_list:
#     if ' ' in str(item):
#         class_list.remove(item)
#         class_list.extend(item.split(' '))

# class_list = [item for item in class_list if item != 'nan']
# class_list = [item for item in class_list if item]
# cl_df = pd.DataFrame(class_list)
# class_items_unique = cl_df.value_counts()[cl_df.value_counts() == 1]

# class_items = cl_df.value_counts()
# class_mask = s['class'].value_counts() == 1
print('done')
