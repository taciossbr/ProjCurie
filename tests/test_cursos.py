from unittest import TestCase
from flask import url_for
from app import app


class CursosTestCase(TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_root_should_return_200(self):
        result = self.client.get(url_for('cursos.index'))

        self.assertEqual(200, result.status_code)


