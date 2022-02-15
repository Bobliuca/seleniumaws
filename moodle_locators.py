from faker import Faker

fake = Faker(locale='en_CA')
moodle_url = 'http://52.39.5.126/'
moodle_login_url = 'http://52.39.5.126/login/index.php'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_username = 'boliu'
moodle_password = 'Nerdca78*'
moodle_dashboard_url = 'http://52.39.5.126/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()  #country = fake.country() 任意国家 #country= fake.current_country() 当前国家
description = fake.sentence(nb_words=100) #nb_word字数
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text='??????') #生成机构名 ？？？代表字符数。# institution = fake.lexify() #随机生成机构名大写字母，测试了一次，是四个字母。
department = fake.lexify(text='??????')
phone = fake.phone_number() #电话会出现加拿大号码，因为上面有位置定义。
mobile_phone = fake.phone_number()
#address = fake.address()
address = fake.address().replace("\n", "")





