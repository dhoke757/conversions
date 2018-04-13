#Test Driven Development for Converter
from convert import *
import pytest

def test_cm_m():
	assert cm_m(3) == 0.03
	assert cm_m(504) == 5.04 
	assert cm_m(496.64) == pytest.approx(4.9664)

def test_cm_km():
	assert cm_km(3) == 0.00003
	assert cm_km(504) == 0.00504 
	assert cm_km(496.64) == pytest.approx(0.0049664)

def test_m_cm():
	assert m_cm(3) == 300
	assert m_cm(504) == 50400 
	assert m_cm(496.64) == pytest.approx(49664)
#use for demonstration of rounding error with pytest
def test_m_km():
	assert m_km(3) == 0.003
	assert m_km(504) == 0.504 
	#assert m_km(55.8) == pytest.approx(0.0558)
	assert m_km(55.8) == 0.0558
def test_m_m():
	assert m_m(3) == 3
	assert m_m(504) == 504
	assert m_m(496.64) == pytest.approx(496.64)

def test_km_m():
	assert km_m(3) == 3000
	assert km_m(504) == 504000 
	assert km_m(496.64) == pytest.approx(496640)

def test_km_cm():
	assert km_cm(3) == 300000
	assert km_cm(504) == 50400000 
	assert km_cm(496.64) == pytest.approx(49664000)