### Testing

python
from geolib.Circle import Circle, Cylinder
from geolib.Square import Square, Cube

c1 = Circle(-1)
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3265, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-4-28bef95d2504>", line 1, in <module>
    c1 = Circle(-1)
  File "/Users/mayurbarge/geometry/geolib/Circle.py", line 14, in __init__
    raise ValueError('Radius should not be negative')
ValueError: Radius should not be negative

c1 = Circle(3.0)

c1.get_area()
Out[6]: 28.274333882308138

cy1 = c1.project(4.0)
cy1.get_volume()
Out[8]: 113.09733552923255
