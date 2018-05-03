
build:
	python setup.py bdist_wheel

clean:
	rm -rf build/ dist/ pyaclg.egg-info/

run:
	python pyaclg/main.py
