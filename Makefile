PACKAGE=appiumcore

clean:
	rm -rf ffbuild build dist

build: clean ## build package into an whl file
	python setup.py sdist bdist_wheel

install.build: ## install and upgrade dependencies for building
	pip install -U setuptools wheel

ffbuild: build ## build for ff pipelines 2.0
	mkdir -p ffbuild/packages
	cp dist/*.whl -t ffbuild/packages