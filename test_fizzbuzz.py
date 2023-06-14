import pytest
import productionCode
# def test_canAssertTrue():
#     assert True
# FizzBuzzKata

def test_return1whenPassed1():
    o = productionCode.fizzBuzz(1)
    assert o=='1'

def test_return2whenPassed2():
    o = productionCode.fizzBuzz(2)
    assert o=='2'

def test_returnFizzWhenPassed3():
    o = productionCode.fizzBuzz(3) 
    assert o=="Fizz"