import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auto_metamask import *


if __name__ == '__main__':
    metamask_path = downloadMetamask('https://github.com/MetaMask/metamask-extension/releases/download/v10.34.0/metamask-chrome-10.34.0.zip')
    driver = setupWebdriver(metamask_path, '/Applications/Chromium.app/Contents/MacOS/Chromium', None, 'chromedriver_mac64/chromedriver')

    # Test account, please do not use for production environment
    setupMetamask(
        'fork black anger brother supply divert embark moment much refuse forest hidden', '69xG2j4JEp')
    # Please use a special network name to avoid conflicts with built-in networks, such as 'MY_MATIC'
    addNetwork('BNB Chain', 'https://bsc-dataseed.binance.org/', '56', 'BNB')
    changeNetwork('BNB Chain')

    # Test account, please do not use for production environment
    importPK("6d8266f91168dd2af7faf91949865e701d3e9bc12bd410f5f55691f85827c4a1")

    driver.switch_to.new_window()
    driver.get('https://metamask.github.io/test-dapp/')

    # Wait 20s for the page to load, and click the 'Connect' button
    wait = WebDriverWait(driver, 20, 1)
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='connectButton']"))).click()
    # MetaMask will pop up a window, complete the connection
    connect()

    # Click the 'Request Permissions' button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='requestPermissions']"))).click()
    # MetaMask will pop up a window
    connect()

    # Click the 'Personal Sign' button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='personalSign']"))).click()
    # MetaMask will pop up a window
    confirm()

    # Click the 'Send Transaction' button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='sendButton']"))).click()
    # MetaMask will pop up a window
    confirm()
    waitPending(20)

    # Click the 'Create Token' button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='createToken']"))).click()
    # MetaMask will pop up a window
    confirm()
    waitPending(20)

    # Click the 'Approve Tokens' button
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[id='approveTokens']"))).click()
    # MetaMask will pop up a window
    approveTokens(6)
    waitPending(20)

    time.sleep(60)
    driver.quit()