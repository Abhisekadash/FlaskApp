from Flask-App.src.main import index

def test_index():
	assert index() == "Hello World"