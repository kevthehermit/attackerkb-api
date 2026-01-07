from attackerkb_api.api import valid_uuid


def test_valid_uuid():
    assert valid_uuid("de559d8e-26e9-49fb-9a38-57b55e4a4c9a")


def test_invalid_uuid():
    assert not valid_uuid("thisisnotauuid")
