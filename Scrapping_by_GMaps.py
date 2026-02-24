
Google Maps Business Scraper
Author: Muhamad Aan A.
GitHub: https://github.com/babymax123
License: MIT License
Year: 2026

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrape_maps(keyword, desa, kecamatan):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Buat query otomatis
    query = f"{keyword} {desa} {kecamatan}"
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
    driver.get(url)

    time.sleep(5)

    # Cari panel hasil
    try:
        scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
    except:
        print("Tidak menemukan panel hasil.")
        driver.quit()
        return []

    print("Mulai scrolling sampai habis...")

    last_height = 0

    while True:
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight",
            scrollable_div
        )
        time.sleep(2)

        new_height = driver.execute_script(
            "return arguments[0].scrollHeight",
            scrollable_div
        )

        # Hitung sementara jumlah hasil
        places_now = driver.find_elements(By.XPATH, '//div[@role="article"]')
        print(f"Jumlah sementara: {len(places_now)}")

        if new_height == last_height:
            print("Scroll selesai (sudah mentok).")
            break

        last_height = new_height

    # Ambil semua hasil setelah scroll selesai
    places = driver.find_elements(By.XPATH, '//div[@role="article"]')

    print(f"Total hasil ditemukan: {len(places)}")

    data = []

    for place in places:
        try:
            name = place.find_element(By.XPATH, './/div[contains(@class,"qBF1Pd")]').text
        except:
            name = "N/A"

        try:
            rating = place.find_element(By.XPATH, './/span[@role="img"]').get_attribute("aria-label")
        except:
            rating = "N/A"

        data.append({
            "Nama": name,
            "Rating": rating,
            "Lokasi Search": f"{desa}, {kecamatan}"
        })

    driver.quit()
    return data


if __name__ == "__main__":
    keyword = input("Masukkan jenis usaha (contoh: toko): ")
    desa = input("Masukkan nama desa: ")
    kecamatan = input("Masukkan nama kecamatan: ")

    hasil = scrape_maps(keyword, desa, kecamatan)

    df = pd.DataFrame(hasil)

    df.to_csv("hasil_scraping_maps.csv", index=False, encoding="utf-8-sig")
    df.to_excel("hasil_scraping_maps.xlsx", index=False)


    print("\n Data berhasil disimpan!")
