import pytest
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'C:\Program Files\Google\chromedriver.exe')

    yield

    pytest.driver.quit()


def test_show_my_pets():

    pytest.driver.find_element(By.ID, 'email').send_keys('Stalevars@mail.ru')

    pytest.driver.find_element(By.ID, 'pass').send_keys('Stalevars98')

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = pytest.driver.find_element(By.TAG_NAME, 'img')
    names = pytest.driver.find_element(By.TAG_NAME, 'title')
    descriptions = pytest.driver.find_element(By.TAG_NAME, 'text')



    for i in range(len(names)):
        assert  photo[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


