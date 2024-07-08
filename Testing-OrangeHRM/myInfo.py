from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome(executable_path='./path/to/chromedriver')

try:
    # Buka halaman OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login sebagai admin
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()
    
    # Navigasi ke My Info
    driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
    
    # Verifikasi
    assert "Personal Details" in driver.page_source

    print("Test My Info module berhasil!")
    
except Exception as e:
    print("Error:", e)

finally:
    # Tunggu sebentar sebelum menutup browser
    time.sleep(3)
    driver.quit()
