import pytest

from alive_progress.animations.bars import bar_factory
from alive_progress.utils.cells import join_cells


@pytest.mark.parametrize('chars, percent, end, expected', [
    ('', -.5, False, '|0123456789|'),
    ('=', -.5, False, '|0123456789|'),
    ('_-=', -.5, False, '|0123456789|'),
    ('', -.5, True, '|!         |'),
    ('=', -.5, True, '|!         |'),
    ('_-=', -.5, True, '|!         |'),
    ('😺', -.5, True, '|!         |'),
    ('_-😺', -.5, True, '|!         |'),

    ('', 0., False, '|0123456789|'),
    ('=', 0., False, '|0123456789|'),
    ('_-=', 0., False, '|0123456789|'),
    ('', 0., True, '|!         |'),
    ('=', 0., True, '|!         |'),
    ('_-=', 0., True, '|!         |'),
    ('😺', 0., True, '|!         |'),
    ('_-😺', 0., True, '|!         |'),

    ('', .15, False, '|%>23456789|'),
    ('=', .15, False, '|%>23456789|'),
    ('_-=', .15, False, '|$%>3456789|'),
    ('', .15, True, '|%>!       |'),
    ('=', .15, True, '|%>!       |'),
    ('_-=', .15, True, '|$%>!      |'),
    ('😺', .15, True, '|%>!       |'),
    ('_-😺', .15, True, '|$%>!      |'),

    ('', .5, False, '|012@#$%>89|'),
    ('=', .5, False, '|===@#$%>89|'),
    ('_-=', .5, False, '|==_@#$%>89|'),
    ('', .5, True, '|012@#$%>! |'),
    ('=', .5, True, '|===@#$%>! |'),
    ('_-=', .5, True, '|==_@#$%>! |'),
    ('😺', .5, True, '| 😺X@#$%>! |'),
    ('_-😺', .5, True, '| _@#$%>!  |'),

    ('', .85, False, '|01234567@#|'),
    ('=', .85, False, '|========@#|'),
    ('_-=', .85, False, '|=======-@#|'),
    ('', .85, True, '|01234567@#!'),
    ('=', .85, True, '|========@#!'),
    ('_-=', .85, True, '|=======-@#!'),
    ('😺', .85, True, '|😺X😺X😺X😺X@#!'),
    ('_-😺', .85, True, '|😺X😺X😺X😺X@#!'),

    ('', 1., False, '|0123456789|'),
    ('=', 1., False, '|==========|'),
    ('_-=', 1., False, '|==========|'),
    ('', 1., True, '|0123456789|'),
    ('=', 1., True, '|==========|'),
    ('_-=', 1., True, '|==========|'),
    ('😺', 1., True, '|😺X😺X😺X😺X😺X|'),
    ('_-😺', 1., True, '|😺X😺X😺X😺X😺X|'),

    ('', 1.5, False, '|0123456789x'),
    ('=', 1.5, False, '|==========x'),
    ('_-=', 1.5, False, '|==========x'),
    ('', 1.5, True, '|0123456789x'),
    ('=', 1.5, True, '|==========x'),
    ('_-=', 1.5, True, '|==========x'),
    ('😺', 1.5, True, '|😺X😺X😺X😺X😺Xx'),
    ('_-😺', 1.5, True, '|😺X😺X😺X😺X😺Xx'),
])
def test_bar_tip_background(chars, percent, end, expected, show_marks):
    bar = bar_factory(chars=chars, tip='@#$%>', background='0123456789xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                      borders='||', errors='!x')(10)
    rendition = bar.end(percent=percent) if end else bar(percent=percent)
    assert show_marks(rendition) == expected
    assert len(rendition) == 12  # length + borders


@pytest.mark.parametrize('chars, tip, background, percent, end, expected', [
    ('', '>', '', -.5, False, '|          |'),
    ('', '>', '0123', -.5, False, '|0123012301|'),
    ('', '@#$%>', '', -.5, False, '|          |'),
    ('=', '', '', -.5, False, '|          |'),
    ('=', '', '.', -.5, False, '|..........|'),
    ('=', '>', '', -.5, False, '|          |'),
    ('=', '>', '0123', -.5, False, '|0123012301|'),
    ('=', '@#$%>', '', -.5, False, '|          |'),
    ('_-=', '', '', -.5, False, '|          |'),
    ('_-=', '', '.', -.5, False, '|..........|'),
    ('_-=', '>', '', -.5, False, '|          |'),
    ('_-=', '>', '0123', -.5, False, '|0123012301|'),
    ('_-=', '@#$%>', '', -.5, False, '|          |'),
    ('', '>', '', -.5, True, '|!         |'),
    ('', '>', '0123', -.5, True, '|!         |'),
    ('', '@#$%>', '', -.5, True, '|!         |'),
    ('=', '', '', -.5, True, '|!         |'),
    ('=', '', '.', -.5, True, '|!         |'),
    ('=', '>', '', -.5, True, '|!         |'),
    ('=', '>', '0123', -.5, True, '|!         |'),
    ('=', '@#$%>', '', -.5, True, '|!         |'),
    ('_-=', '', '', -.5, True, '|!         |'),
    ('_-=', '', '.', -.5, True, '|!         |'),
    ('_-=', '>', '', -.5, True, '|!         |'),
    ('_-=', '>', '0123', -.5, True, '|!         |'),
    ('_-=', '@#$%>', '', -.5, True, '|!         |'),

    ('', '>', '', 0., False, '|          |'),
    ('', '>', '0123', 0., False, '|0123012301|'),
    ('', '@#$%>', '', 0., False, '|          |'),
    ('=', '', '', 0., False, '|          |'),
    ('=', '', '.', 0., False, '|..........|'),
    ('=', '>', '', 0., False, '|          |'),
    ('=', '>', '0123', 0., False, '|0123012301|'),
    ('=', '@#$%>', '', 0., False, '|          |'),
    ('_-=', '', '', 0., False, '|          |'),
    ('_-=', '', '.', 0., False, '|..........|'),
    ('_-=', '>', '', 0., False, '|          |'),
    ('_-=', '>', '0123', 0., False, '|0123012301|'),
    ('_-=', '@#$%>', '', 0., False, '|          |'),
    ('', '>', '', 0., True, '|!         |'),
    ('', '>', '0123', 0., True, '|!         |'),
    ('', '@#$%>', '', 0., True, '|!         |'),
    ('=', '', '', 0., True, '|!         |'),
    ('=', '', '.', 0., True, '|!         |'),
    ('=', '>', '', 0., True, '|!         |'),
    ('=', '>', '0123', 0., True, '|!         |'),
    ('=', '@#$%>', '', 0., True, '|!         |'),
    ('_-=', '', '', 0., True, '|!         |'),
    ('_-=', '', '.', 0., True, '|!         |'),
    ('_-=', '>', '', 0., True, '|!         |'),
    ('_-=', '>', '0123', 0., True, '|!         |'),
    ('_-=', '@#$%>', '', 0., True, '|!         |'),

    ('', '>', '', .15, False, '| >        |'),
    ('', '>', '0123', .15, False, '|0>23012301|'),
    ('', '@#$%>', '', .15, False, '|%>        |'),
    ('=', '', '', .15, False, '|==        |'),
    ('=', '', '.', .15, False, '|==........|'),
    ('=', '>', '', .15, False, '|=>        |'),
    ('=', '>', '0123', .15, False, '|=>23012301|'),
    ('=', '@#$%>', '', .15, False, '|%>        |'),
    ('_-=', '', '', .15, False, '|=_        |'),
    ('_-=', '', '.', .15, False, '|=_........|'),
    ('_-=', '>', '', .15, False, '|->        |'),
    ('_-=', '>', '0123', .15, False, '|->23012301|'),
    ('_-=', '@#$%>', '', .15, False, '|$%>       |'),
    ('', '>', '', .15, True, '| >!       |'),
    ('', '>', '0123', .15, True, '|0>!       |'),
    ('', '@#$%>', '', .15, True, '|%>!       |'),
    ('=', '', '', .15, True, '|==!       |'),
    ('=', '', '.', .15, True, '|==!       |'),
    ('=', '>', '', .15, True, '|=>!       |'),
    ('=', '>', '0123', .15, True, '|=>!       |'),
    ('=', '@#$%>', '', .15, True, '|%>!       |'),
    ('_-=', '', '', .15, True, '|=_!       |'),
    ('_-=', '', '.', .15, True, '|=_!       |'),
    ('_-=', '>', '', .15, True, '|->!       |'),
    ('_-=', '>', '0123', .15, True, '|->!       |'),
    ('_-=', '@#$%>', '', .15, True, '|$%>!      |'),

    ('', '>', '', .5, False, '|     >    |'),
    ('', '>', '0123', .5, False, '|01230>2301|'),
    ('', '@#$%>', '', .5, False, '|   @#$%>  |'),
    ('=', '', '', .5, False, '|=====     |'),
    ('=', '', '.', .5, False, '|=====.....|'),
    ('=', '>', '', .5, False, '|=====>    |'),
    ('=', '>', '0123', .5, False, '|=====>2301|'),
    ('=', '@#$%>', '', .5, False, '|===@#$%>  |'),
    ('_-=', '', '', .5, False, '|=====     |'),
    ('_-=', '', '.', .5, False, '|=====.....|'),
    ('_-=', '>', '', .5, False, '|====_>    |'),
    ('_-=', '>', '0123', .5, False, '|====_>2301|'),
    ('_-=', '@#$%>', '', .5, False, '|==_@#$%>  |'),
    ('', '>', '', .5, True, '|     >!   |'),
    ('', '>', '0123', .5, True, '|01230>!   |'),
    ('', '@#$%>', '', .5, True, '|   @#$%>! |'),
    ('=', '', '', .5, True, '|=====!    |'),
    ('=', '', '.', .5, True, '|=====!    |'),
    ('=', '>', '', .5, True, '|=====>!   |'),
    ('=', '>', '0123', .5, True, '|=====>!   |'),
    ('=', '@#$%>', '', .5, True, '|===@#$%>! |'),
    ('_-=', '', '', .5, True, '|=====!    |'),
    ('_-=', '', '.', .5, True, '|=====!    |'),
    ('_-=', '>', '', .5, True, '|====_>!   |'),
    ('_-=', '>', '0123', .5, True, '|====_>!   |'),
    ('_-=', '@#$%>', '', .5, True, '|==_@#$%>! |'),

    ('', '>', '', .85, False, '|        > |'),
    ('', '>', '0123', .85, False, '|01230123>1|'),
    ('', '@#$%>', '', .85, False, '|        @#|'),
    ('=', '', '', .85, False, '|========  |'),
    ('=', '', '.', .85, False, '|========..|'),
    ('=', '>', '', .85, False, '|========> |'),
    ('=', '>', '0123', .85, False, '|========>1|'),
    ('=', '@#$%>', '', .85, False, '|========@#|'),
    ('_-=', '', '', .85, False, '|========- |'),
    ('_-=', '', '.', .85, False, '|========-.|'),
    ('_-=', '>', '', .85, False, '|========_>|'),
    ('_-=', '>', '0123', .85, False, '|========_>|'),
    ('_-=', '@#$%>', '', .85, False, '|=======-@#|'),
    ('', '>', '', .85, True, '|        >!|'),
    ('', '>', '0123', .85, True, '|01230123>!|'),
    ('', '@#$%>', '', .85, True, '|        @#!'),
    ('=', '', '', .85, True, '|========! |'),
    ('=', '', '.', .85, True, '|========! |'),
    ('=', '>', '', .85, True, '|========>!|'),
    ('=', '>', '0123', .85, True, '|========>!|'),
    ('=', '@#$%>', '', .85, True, '|========@#!'),
    ('_-=', '', '', .85, True, '|========-!|'),
    ('_-=', '', '.', .85, True, '|========-!|'),
    ('_-=', '>', '', .85, True, '|========_>!'),
    ('_-=', '>', '0123', .85, True, '|========_>!'),
    ('_-=', '@#$%>', '', .85, True, '|=======-@#!'),

    ('', '>', '', 1., False, '|          |'),
    ('', '>', '0123', 1., False, '|0123012301|'),
    ('', '@#$%>', '', 1., False, '|          |'),
    ('=', '', '', 1., False, '|==========|'),
    ('=', '', '.', 1., False, '|==========|'),
    ('=', '>', '', 1., False, '|==========|'),
    ('=', '>', '0123', 1., False, '|==========|'),
    ('=', '@#$%>', '', 1., False, '|==========|'),
    ('_-=', '', '', 1., False, '|==========|'),
    ('_-=', '', '.', 1., False, '|==========|'),
    ('_-=', '>', '', 1., False, '|==========|'),
    ('_-=', '>', '0123', 1., False, '|==========|'),
    ('_-=', '@#$%>', '', 1., False, '|==========|'),
    ('', '>', '', 1., True, '|          |'),
    ('', '>', '0123', 1., True, '|0123012301|'),
    ('', '@#$%>', '', 1., True, '|          |'),
    ('=', '', '', 1., True, '|==========|'),
    ('=', '', '.', 1., True, '|==========|'),
    ('=', '>', '', 1., True, '|==========|'),
    ('=', '>', '0123', 1., True, '|==========|'),
    ('=', '@#$%>', '', 1., True, '|==========|'),
    ('_-=', '', '', 1., True, '|==========|'),
    ('_-=', '', '.', 1., True, '|==========|'),
    ('_-=', '>', '', 1., True, '|==========|'),
    ('_-=', '>', '0123', 1., True, '|==========|'),
    ('_-=', '@#$%>', '', 1., True, '|==========|'),

    ('', '>', '', 1.5, False, '|          x'),
    ('', '>', '0123', 1.5, False, '|0123012301x'),
    ('', '@#$%>', '', 1.5, False, '|          x'),
    ('=', '', '', 1.5, False, '|==========x'),
    ('=', '', '.', 1.5, False, '|==========x'),
    ('=', '>', '', 1.5, False, '|==========x'),
    ('=', '>', '0123', 1.5, False, '|==========x'),
    ('=', '@#$%>', '', 1.5, False, '|==========x'),
    ('_-=', '', '', 1.5, False, '|==========x'),
    ('_-=', '', '.', 1.5, False, '|==========x'),
    ('_-=', '>', '', 1.5, False, '|==========x'),
    ('_-=', '>', '0123', 1.5, False, '|==========x'),
    ('_-=', '@#$%>', '', 1.5, False, '|==========x'),
    ('', '>', '', 1.5, True, '|          x'),
    ('', '>', '0123', 1.5, True, '|0123012301x'),
    ('', '@#$%>', '', 1.5, True, '|          x'),
    ('=', '', '', 1.5, True, '|==========x'),
    ('=', '', '.', 1.5, True, '|==========x'),
    ('=', '>', '', 1.5, True, '|==========x'),
    ('=', '>', '0123', 1.5, True, '|==========x'),
    ('=', '@#$%>', '', 1.5, True, '|==========x'),
    ('_-=', '', '', 1.5, True, '|==========x'),
    ('_-=', '', '.', 1.5, True, '|==========x'),
    ('_-=', '>', '', 1.5, True, '|==========x'),
    ('_-=', '>', '0123', 1.5, True, '|==========x'),
    ('_-=', '@#$%>', '', 1.5, True, '|==========x'),
])
def test_bar_draw(chars, tip, background, percent, end, expected):
    bar = bar_factory(chars=chars, tip=tip, background=background,
                      borders='||', errors='!x')(10)
    rendition = bar.end(percent=percent) if end else bar(percent=percent)
    assert join_cells(rendition) == expected
    assert len(rendition) == 12  # length + borders


@pytest.mark.parametrize('params', [
    dict(chars='', tip=''),
    dict(chars='👍.'),
])
def test_bar_error(params):
    with pytest.raises(AssertionError):
        bar_factory(**params)


@pytest.mark.parametrize('end, expected', [
    (False, '|1234567890|'),
    (True, '|aaaaaaaaaa|'),
])
def test_unknown_bar(end, expected, spinner_test):
    bar = bar_factory('a')(10, spinner_factory=spinner_test(('1234567890',)))
    method = bar.unknown.end if end else bar.unknown
    assert join_cells(method()) == expected
