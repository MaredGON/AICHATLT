
from playwright.sync_api import sync_playwright

def scrape_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Дождаться, пока страница загрузится
        page.wait_for_load_state('networkidle')

        # Получить весь текст с страницы
        content = page.content()

        browser.close()
        return content

def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

urls = {
    'latoken_info': 'https://coda.io/@latoken/latoken-talent/latoken-161',
    'hackathon_info': 'https://deliver.latoken.com/hackathon',
    'rag_culture_deck': 'https://coda.io/@latoken/latoken-talent/culture-139'
}

for name, url in urls.items():
    content = scrape_website(url)
    if content:
        save_to_file(content, f'{name}.txt')
        print(f"Информация {name} сохранена")
    else:
        print(f"Не удалось получить данные с {url}")