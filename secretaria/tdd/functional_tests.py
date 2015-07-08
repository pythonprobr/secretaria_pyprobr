#!/usr/bin/env py.test

import pytest

from selenium import webdriver

@pytest.yield_fixture
def nav():
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

def test_titulo_da_pagina(nav):
    nav.get('http://localhost:8000/newsletter')
    assert 'Newsletter - cadastro' in nav.title, 'Browser title was ' + nav.title
    inputbox = nav.find_element_by_id('id_email')
    placeholder = inputbox.get_attribute('placeholder')
    assert placeholder == 'Digite seu e-mail', 'placeholder was' + placeholder
