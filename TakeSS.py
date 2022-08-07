from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

browser = webdriver.Chrome(service=Service(executable_path=r'C:\Users\abhay\PycharmProjects\chromedriver.exe'),
                           options=options)

browser = webdriver.Remote(command_executor='http://localhost:61663', desired_capabilities={})
browser.close()
browser.session_id = '22ec909a14ccb6ab2aac7b86684bdb67'

mylist = browser.find_elements('xpath', '//body//*[not(self::script) and not(self::style) and not(contains(@style,'
                                        '"display:none")) and (self::img)]')

print(len(mylist))
index = 0
filename = ""
while index < len(mylist):
    try:
        if mylist[index].get_attribute("id") != "":
            filename = mylist[index].tag_name + "_id_" + mylist[index].get_attribute("id")
        elif mylist[index].get_attribute("class") != "":
            filename = mylist[index].tag_name + "_class_" + mylist[index].get_attribute("class")
        elif mylist[index].get_attribute("name") != "":
            filename = mylist[index].tag_name + "_name_" + mylist[index].get_attribute("name")
        else:
            if len(mylist[index].text()) > 10:
                filename = mylist[index].tag_name + "_text_" + mylist[index].text()[0:10]
            else:
                filename = mylist[index].tag_name + "_text_" + mylist[index].text()

        mylist[index].screenshot(r'C:\Users\abhay\PycharmProjects\pythonProject\ss\{}.png'.format(filename))

    except Exception as e:
        print("Exception")
    index += 1
