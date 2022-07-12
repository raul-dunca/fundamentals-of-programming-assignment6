import unittest
from py import PogoList
from py import sort_function
from py import filter
class PyTest(unittest.TestCase):
    def setUp(self):
        self._list=PogoList()
    def test_list(self):
        self._list.append("21")
        self._list.append(5)
        self.assertEqual(len(self._list),2)
        self._list[1]=931
        self.assertEqual(self._list[1],931)
        del self._list[0]
        for i in self._list:
            self.assertEqual(i,931)

    def test_sort(self):
        def ex_1(a, b):
            if a > b:
                return True
            else:
                return False

        r=sort_function([2,3,1,6,8,3,5,21],ex_1)
        assert r==[1,2,3,3,5,6,8,21]


    def test_filter(self):
        def ex_2(x,a):
            if x[0] == a :
                return True
            else:
                return False
        f=filter(["aloha","Boris","Antarctica","Pacific","snacks","sponge"],ex_2,"a")
        assert f==["aloha"]
