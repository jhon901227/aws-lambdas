from tests.test_pythonhello import PythonhelloLambdaTestCase


class TestSuccess(PythonhelloLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

