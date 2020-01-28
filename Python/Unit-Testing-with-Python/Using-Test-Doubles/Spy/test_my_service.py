from unittest.mock import Mock

from my_service import MyService, Request
from single_sign_on import SingleSignOnRegistry, SSOToken


def test_hello_name():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(stub_sso_registry)
    response = service.handle(Request("Eldan"), SSOToken)
    assert response.text == "Hello Eldan!"


def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken()
    service.handle(Request("Eldan"), token)
    spy_sso_registry.is_valid.assert_called_with(token)


def test_single_sign_on_with_invalid_token():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    spy_sso_registry.is_valid.return_value = False
    service = MyService(spy_sso_registry)
    token = SSOToken()
    response = service.handle(Request("Eldan"), token)
    spy_sso_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"
