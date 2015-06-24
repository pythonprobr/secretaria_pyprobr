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
    nav.get('http://localhost:8000')
    assert 'Python.pro.br' in nav.title, 'Browser title was ' + nav.title
