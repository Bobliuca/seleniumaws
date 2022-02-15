import sys
import datetime
import moodle_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)




# Fixture method - to open web browser
# Make a full screen
def setUp():
    driver.maximize_window()
# Let's wait for the browser response in general
    driver.implicitly_wait(30)

# Navigating to the Moodle app website
#     driver.get('http://52.39.5.126/')
    driver.get(locators.moodle_url)

#Checking that we're non the correct URL address and we're seeing correct titile
    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f'We are at Moodle homepage -- {driver.current_url}')
        print(f'We are seeing title message -- "Software Quality Assurance Testing"')
    else:
        print(f'We are not at Moodle homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'---------------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()
       #logger 记录新产生的数据，# 较为高级没太多解释， mssagelog  Make a log file with dynamic fake values
        old_instance = sys.stdout  # 旧用例用法，保存和展示一些旧方法
        log_file = open('message.log', 'w')  # 打开文件，记录数据， “w”表示权限
        sys.stdout = log_file  # 更新
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n'
              f'Full Name: {locators.full_name}')
        sys.stdout = old_instance  # 总能更新最新数据
        log_file.close()

def log_in(username, password):
    # if driver.current_url == 'http://52.39.5.126/':
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        #if driver.current_url == 'http://52.39.5.126/login/index.php':
        if driver.current_url == locators.moodle_login_url:
            # print('yah')
            # driver.find_element(By.ID, 'username').send_keys('boliu')
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            # driver.find_element(By.ID, 'password').send_keys(locators.moodle_password)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            # if driver.title == 'Dashboard' and driver.current_url == 'http://52.39.5.126/my/':
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                # assert driver.current_url == 'http://52.39.5.126/my/'
                assert driver.current_url == locators.moodle_dashboard_url
                print(f'log in successfully, Dashbord is present. \n'
                      f'we logged in with Username: {username} and Password: {password}')
            else:
                print(f'We\'re not at the Dashboard. Try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    # driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.25)
    # driver.switch_to.alert.accept()
    # if driver.current_url == 'http://52.39.5.126/':
    if driver.current_url == locators.moodle_url:
        print(f'Log out successfully at: {datetime.datetime.now()}')
def log_out2():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.25)
    # driver.switch_to.alert.accept()
    if driver.current_url == locators.moodle_url:
        print(f'Log out successfully at: {datetime.datetime.now()}')

def create_new_user():
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    # breakpoint(2) 暂停
    #driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/nav/div/button/i').click() 找不到元素的时候用
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    # Enter fake data into username open field
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)

    #Select 'Allow everyone to see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    # Select(driver.find_element(By.ID, 'id_country')).select_by_value('CA') # 或选项
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)

    # upload pitcture to the user  picture section
    #click by you can dray and drop files here to add them section

    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    #以下是三种：选目标首选id，其次是 类名，如果没有就选xpan span，最后再选 Partial link text, 永远不选div，hi这种元素。
    # driver.find_element(By.CLASS_NAME, 'fp-repo-name').click()
    # driver.find_element(By.XPATH, '//span[contains(., "Server files")]').click() #老贺的做法
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Server files').click() #Mike老师的另一个做法 当看到一小部分连接内容的时候可以用 单词可以不写全。。
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Cosmetics').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Biotherm 2021 fall school').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Course image').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'BT2021fall.png').click()
    sleep(0.250)
    # Click by ' Select this file ' button
    driver.find_element(By.XPATH, '//button[contains(., "Select this file")]').click()
    # Enter^value to the 'Picture description' open field
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    # Click by 'Additional names' dropdown menu
    driver.find_element(By.XPATH, '//a[contains(., "Additional names")]').click()
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.pic_desc)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.pic_desc)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.pic_desc)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.pic_desc)
    sleep(0.25)
    ##Click by 'Interests ' dropdown menu
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    sleep(0.25)
    # Using for loop,take all items from the list and populate data
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').click() #很脆弱，但是只有这个路径。
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
    sleep(0.25)
    # Fill Optional section
        # Click by 0ptional link to open that section
    driver.find_element(By.XPATH, "//a[text() = 'Optional']").click() # 用text查看元素。不用contain
    sleep(0.25)
##Fill out the Web page input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(locators.web_page_url)
    sleep(0.25)
    # 这个句法用的是css，两个元素input和id_url合着用，有id没有用。
    # driver.find_element(By.css_SELECTOR, "如果出现一大串div元素，肯定不被雇佣").click()
    ##Fill out the ICQ ID input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(locators.icq_number)
    sleep(0.25)
    # Fill out the Skgpe input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(locators.new_username)
    # Fill out the  aim input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_aim").send_keys(locators.new_username)
    # Fill out the  yahoo input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_yahoo").send_keys(locators.new_username)
    # Fill out the  msn input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_msn").send_keys(locators.new_username)
    # Fill out the ID number input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.icq_number)
    sleep(.25)
    # Fill out the institution input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_institution").send_keys(locators.institution)
    # Fill out the department input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_department").send_keys(locators.department)
    # Fill out the phone number input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_phone1").send_keys(locators.phone)
    # Fill out the mobile phone input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.mobile_phone)
    sleep(.25)
    # Fill out the mobile phone input open field
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(.25)
    # if driver.current_url == 'http://52.39.5.126/admin/user.php':
    # click by "create user ' button
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(.25)
    print(f' --- Test Scenario: Create a new user "{locators.new_username}" --- is passed')

def check_user_created():
    # Check that we are on the User 's Main Page
    if driver.current_url == locators.moodle_users_main_page:
        assert driver.find_element(By.XPATH, "//h1[text() = 'Software Quality Assurance Testing']").is_displayed()
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label') and \
            driver.find_element(By.NAME, 'email'):
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            sleep(0.25)
            if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]'):
                print('--- Test Scenario: Check user created --- is passed')
                # Log out from the Moodle app
                # log_out()

def delete_a_new_user():
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    # driver.find_element(By.ID, 'id_email').send_key(locators.email)
    driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
    sleep(0.25)
    if driver.find_element(By.XPATH, f'//span[contains(., "{locators.email}")]'):
            # and driver.find_element(By.XPATH, f'//td[contains(., "Delete")]'):
        driver.find_element(By.XPATH, f'//td[contains(., "Delete")]').click()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Delete').click()
        sleep(.75)
        print(f'New user with "{locators.email}" has been deleted.')



    # breakpoint()

def check_we_logged_in_with_new_cred():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'--- User with the name {locators.full_name} is displayed. Test Passed ---')


def delete_a_new_user():
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.5)
    if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() \
            and driver.find_element(By.ID, 'id_email').is_displayed():
        driver.find_element(By.ID, "id_email").send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.ID, "id_addfilter").click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]').is_displayed() and\
                driver.find_element(By.XPATH, '//*[@title="Delete"]').is_displayed():
            #is_displayed()用法：当没有显示在屏幕上的时候就不用。  '//*[@title="Delete"]‘有数据但不在屏幕上显示。
            #(By.XPATH, '//*[@资产="值"]'), Mike说，他找不到元素的时候XPATH是最好用的。这个公式最常用。
            # 我在作业里面用(By.XPATH, '//td[6]/a/i').click()
            driver.find_element(By.XPATH, '//*[@title="Delete"]').click()
            sleep(.25)
            driver.find_element(By.XPATH, '//button[contains(., "Delete")]').click()
            print(f'User with email {locators.email} got deleted. ')
        else:
            print(f'User with email {locators.email} not found. ')
            




# ### Create a new user Test Case ###
# # Open web browser
# setUp()
# # Log in
# log_in(locators.moodle_username, locators.moodle_password)
# # Create a new user
# create_new_user()
# # Check a new user has been added
# check_user_created()
# # Close the web browser
# #tearDown()
# #sleep(5)
# ### Log In With New User Credentials Test Case ###
# # Open web browser
# #setUp()
# # Log in
# log_in(locators.new_username, locators.new_password)
# # Check we logged in with the new credentials
# check_we_logged_in_with_new_cred()
# log_out()
# log_in(locators.moodle_username, locators.moodle_password)
# delete_a_new_user()
# log_out()
# # Close the web browser
# tearDown()

#填表最常见四种可能性
# 单独
# 多项
# 选择
# 拖拽



#mike 说的三种XPATH元素方式：
# text,
# //*[@title="Delete"]
#      没记住，回头看视频在总结一下。