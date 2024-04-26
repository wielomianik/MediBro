### MediBro

Personal project of selenium bot searching for available appointments in MediCover (Poland).
<br>In case of sharpening skills...

### Configuration
```
$ git clone git@github.com:wielomianik/MediBro.git medibro
$ cd medibro
$ mv config.example config.ini -> {Provide your credentials and telegram token here, edit config.ini}
$ nano config.ini

$ python -m venv env
$ source env/bin/activate

(env)$ pip install -r requirements
(env)$ python main.py
```