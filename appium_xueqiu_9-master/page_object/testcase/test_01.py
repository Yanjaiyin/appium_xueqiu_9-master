import pytest


class Test01():
    name_list=["echo","rita"]
    @pytest.mark.parametrize("key",name_list)
    def test_01(self,key):
        print("1")
        print(key)





        