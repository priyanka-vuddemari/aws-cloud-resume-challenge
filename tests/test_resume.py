import pytest
import requests
from playwright.sync_api import sync_playwright

API_URL = "https://40g9acq651.execute-api.ap-south-2.amazonaws.com/count"
RESUME_URL = "https://d14zfhp4g206cx.cloudfront.net/"

# ── API Smoke Tests ──

def test_api_returns_200():
    """API should return a 200 status code"""
    response = requests.get(API_URL)
    assert response.status_code == 200

def test_api_returns_views_key():
    """API response should contain a views key"""
    response = requests.get(API_URL)
    data = response.json()
    assert "views" in data

def test_api_views_is_integer():
    """Views count should be an integer"""
    response = requests.get(API_URL)
    data = response.json()
    assert isinstance(data["views"], int)

def test_api_views_increments():
    """Views count should increment on each call"""
    first = requests.get(API_URL).json()["views"]
    second = requests.get(API_URL).json()["views"]
    assert second == first + 1

def test_api_views_greater_than_zero():
    """Views count should be greater than zero"""
    response = requests.get(API_URL)
    data = response.json()
    assert data["views"]