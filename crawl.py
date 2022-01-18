import time
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys


def write(reg, phone):
    import csv
    data = [reg,phone]
    f = open('data.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()


    


def get_phone(reg):
    # print(driver.title)
    # # driver.close()
    # print(reg)
    # phone = "08092978383"
    # write(reg, phone)
    # return
    PATH = "/home/unknown/Documents/bot/chromedriver"
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2})
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-setuid-sandbox")

    chromeOptions.add_argument("--remote-debugging-port=9222")  # this

    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("start-maximized")
    # chromeOptions.add_argument("disable-infobars")
    chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")

    driver = webdriver.Chrome(PATH, options=chromeOptions)
    # time.sleep(1)
    driver.get("https://portal.jamb.gov.ng/examslipprinting/printexaminationslip")
    title = driver.title
    search = driver.find_element_by_id('txtRegNumber')
    search.send_keys(reg)
    driver.find_element_by_id('lnkSearch').click()
    time.sleep(2)
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle
    signin_window_handle = None
    do_this_thrice = 0
    while not signin_window_handle:
        do_this_thrice += 1
        if (do_this_thrice > 3):
            break
        for handle in driver.window_handles:
            if (do_this_thrice > 3):
                break
            
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    if signin_window_handle is None:
        # Exist
        write(reg, "mopup")
        print("Reg. No " , reg,  " is a Mop-up candidate")
        # driver.quit()
        # time.sleep(20)
        return
    # time.sleep(1)
    driver.switch_to.window(signin_window_handle)
    trs = driver.find_elements_by_xpath("//td")
    active = False
    phone = None
    for tr in trs:
        try:    
            if active:
                phone = tr.text
                break
            if tr.text == 'Telephone No.:':
                active = True
        except Exception as e:
            print("Error: -->  ", e)
            print("Trying again")
            time.sleep(2)
            get_phone(reg)
            
    # print(phone)
    write(reg, phone)
    print("Processed ", reg, " ********** Phone:",phone)
    driver.quit()

reg_numbers = [
'10637289GG',
'10082194FF',
]

# # i = 0
for reg in reg_numbers:
    # i +=1
    # if i > 5:
        # break
    try:
        get_phone(reg)
    except:
        get_phone(reg)
    
# get_phone("11294721HB")
