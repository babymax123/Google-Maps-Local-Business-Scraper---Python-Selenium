🗺️ Google Maps Business Scraper

Google Maps Business Scraper is a Python automation tool built with Selenium that extracts local business data directly from Google Maps search results.

This tool automatically performs infinite scrolling to collect all available results based on:

Keyword (business type)

Village (Desa)

District (Kecamatan)

The extracted data is exported into CSV and Excel formats.

🚀 Features

✅ Automated Google Maps search

✅ Infinite auto-scroll until results end

✅ Extract business name

✅ Extract business rating

✅ Export to CSV

✅ Export to Excel

✅ Simple CLI input

🛠️ Tech Stack

Python 3

Selenium

Pandas

WebDriver Manager

ChromeDriver

📦 Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/google-maps-scraper.git
cd google-maps-scraper
2️⃣ Install Dependencies
pip install selenium pandas webdriver-manager openpyxl

Make sure Google Chrome is installed on your system.

▶️ How to Run
python main.py

You will be prompted to enter:

Business keyword (example: toko)

Village name

District name

Example:

Masukkan jenis usaha: toko
Masukkan nama desa: Sukamaju
Masukkan nama kecamatan: Cibinong
📁 Output

The script generates:

hasil_scraping_maps.csv

hasil_scraping_maps.xlsx

Both files contain:

Business Name

Rating

Search Location

⚠️ Disclaimer

This project is intended for educational and research purposes only.
Please ensure compliance with Google Maps Terms of Service before using this tool.

📄 License
```
This project is licensed under the MIT License.
```
👨‍💻 Author

Your Name
GitHub: https://github.com/babaymax123
