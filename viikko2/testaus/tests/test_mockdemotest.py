from unittest import TestCase, mock
from testaus.mock_demo.mock_demo import get_file_path

class MockDemoTest(TestCase):
    # def test_get_env_works_properly(self):
    #     with mock.patch('src.words.mock_demo.os') as mock_os:
    #         get_env('TEST_ENV')
    #         assert mock_os.getenv.call_count== 1

    # def test_do_get_env_return_value(self):
    #     with mock.patch('src.words.mock_demo.os.getenv', return_value='test_value'):
    #         assert get_env('TEST_ENV') == 'test_value'
    
    def test_get_file_path(self):
        expected_result = 'C:\\Users\\Olli\\Desktop\\AW\\AW-testing-harjoitukset\\viikko2\\testaus\\mock_demo'
        result = get_file_path()
        self.assertEqual(result, expected_result)