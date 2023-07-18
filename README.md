# This is where I'm learning data science with python

## Virtual env

I don't know what virtual envs are in python yet outside of a way to apparently manage depedencies.

```
source env/bin/activate
```

To list out dependencies to file:

```
pip3 freeze > requirements.txt
```

To install from that:

```
pip3 install -r requirements.txt
```

This will create an env folder (which is gitignored) that contains a copy of each dependency.
