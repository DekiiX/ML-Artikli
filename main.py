from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://docs.aws.amazon.com/")
driver.find_element("link text", "Machine Learning").click()
driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")
# Izvlacenje svih <a> elemenata na prvoj stranici koji se zavrsavaju sa odredjenim href atributom

links = soup.find_all("a", href=re.compile(r"\?icmpid=docs_homepage_ml$"))

with open('C:\\Users\\Kompjuter\\PycharmProjects\\HelloWorld\\ml_artikli.txt', 'a') as file:
    # Artikli sa prve stranice
    for link in links:
        text = link.get_text()
        href = link["href"]
        file.write('\n' + text + '\n')
        file.write('https://docs.aws.amazon.com/' + href + '\n')

# Artikli sa druge stranice
button = driver.find_element(By.XPATH, "//button[contains(text(), '2')]")
button.click()
driver.implicitly_wait(10)
html_2 = driver.page_source
soup_2 = BeautifulSoup(html_2, "lxml")

# Izvlacenje svih <a> elemenata na drugoj stranica koji se zavrsavaju sa odredjenim href atributom (imaju svi isti)
links_2 = soup_2.find_all("a", href=re.compile(r"\?icmpid=docs_homepage_ml$"))

with open('C:\\Users\\Kompjuter\\PycharmProjects\\HelloWorld\\ml_artikli.txt', 'a') as file:
    # Artikli sa druge stranice
    for link2 in links_2:
        text = link2.get_text()
        href2 = link2["href"]
        file.write('\n' + text + '\n')
        file.write('https://docs.aws.amazon.com/' + href2 + '\n')
