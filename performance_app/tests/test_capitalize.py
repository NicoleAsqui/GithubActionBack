def capitalize_string(svariable):
    return svariable.capitalize()


def test_capitalize_string():
    assert capitalize_string('test') == 'Test'


test_capitalize_string()
