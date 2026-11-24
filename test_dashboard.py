from streamlit.testing.v1 import AppTest

def test_dashboard_starts():
    app = AppTest.from_file("app.py").run(timeout=30)
    assert not app.exception
    assert app.metric[0].value == "1000"
    app.sidebar.slider[0].set_value(500).run(timeout=30)
    assert not app.exception
    assert app.metric[0].value == "500"
