# conftest.py
import pytest
import random
from utilities.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def random_email():
    return f"test{random.randint(1000,9999)}@test.com"