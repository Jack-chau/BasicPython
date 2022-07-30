import sys
# print(sys.path)
# sys.path.append('C:/Users/Jack Chau/PycharmProjects/python/python/Begin/SYS')
# import utils
# print(sys.path)


# dinamic go up one folder
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
import utils
