## Simple flask application snippet

Simple flask application, that can be used as a starting point. It has complete file/directory structure. Includes css and js framework and sample template file.

Requires:
- python3
- flask
- gunicorn3

Includes:
- kube.css
- kube.js

Installation:
```bash
apt install python3 python3-dev python3-pip gunicorn3
pip3 install flask
```

Running:
```bash
python3 application.py
```
or
```bash
gunicorn3 --bind 0.0.0.0:8000 wsgi
```
