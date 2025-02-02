import pytest

from panel import FloatPanel, Spacer
from panel.tests.util import serve_component, wait_until

pytestmark = pytest.mark.ui

def test_float_panel_closed_status(page):
    float_panel = FloatPanel(
        Spacer(styles=dict(background='red'), width=200, height=200),
        Spacer(styles=dict(background='green'), width=200, height=200),
        Spacer(styles=dict(background='blue'), width=200, height=200),
    )

    serve_component(page, float_panel)

    page.locator('.jsPanel-btn-close').click()

    wait_until(lambda: float_panel.status == 'closed', page)
