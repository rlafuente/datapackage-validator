install:
	virtualenv .env --no-site-packages --distribute --prompt=\(dpkg-validate\)
	. `pwd`/.env/bin/activate; pip install -r requirements.txt

clean:
	rm -fr build dist datapkg_validator.egg-info
