from HA1 import yamamura
from HA1 import roses

def test_yamamura():
	assert yamamura(theta = 0.11, Y_0 = 0, f = 1.9, b = 0.19) == 0
  
  
    
def test_roses():
    assert roses(0, 90) == 1
