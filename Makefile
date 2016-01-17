install:
	virtualenv .env --no-site-packages --distribute --prompt=\(dpkg-validate\)
	. `pwd`/.env/bin/activate; pip install -r requirements.txt

