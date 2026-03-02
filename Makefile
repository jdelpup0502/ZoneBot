install:
	pip install -r requirements.txt

test:
	python3 -m unittest discover tests

run:
	python3 src/main.py

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
