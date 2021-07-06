import pandas as pd
from pandas.testing import assert_frame_equal
from titanic.clean import clean_titanic_data

class TestClean(object):

    def test_clean(self, titanic_data):
        actual = clean_titanic_data(titanic_data)
        expected = pd.DataFrame({'Survived': 0, 'Pclass': 3, 'Age': 22, 'SibSp': 1, 'Parch': 0, 'Fare': 7.25, 'SexCode': 1}, pd.Index(data=[1], name='PassengerId'))
        assert_frame_equal(actual, expected)
