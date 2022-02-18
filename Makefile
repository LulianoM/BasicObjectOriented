venv:
	test -d .venv || python3 -m venv .venv

install: venv
	./venv/bin/pip3 install --upgrade pip
	./venv/bin/pip3 install -r requirements.txt
	./venv/bin/pip3 install streamlit --upgrade

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	rm -f tmp/*

run: venv
	streamlit run main.py