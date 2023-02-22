from bait_biter import _ui_text


def test_openai_error_msg():
    assert (
        _ui_text.openai_error_msg("this_is_an_error_msg")
        == """
        OpenAI returned an error: 

        Error message: *this_is_an_error_msg*
    """
    )
