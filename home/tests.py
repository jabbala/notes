from django.test import TestCase

# Create your tests here.
def test_initial():
    assert True

def test_failing():
    print("This is a test message")
    assert 1 == 1