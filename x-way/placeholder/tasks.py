from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def show_albums():
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("http://localhost:8000/")

    logger.debug("Start pages albums")

    return True
