## kLab Website

This is the public repository for the kLab website hosted at: http://klab.rw

Although Nyaruka originally created the website we look forward to having contributions from the Kigali community to enhance it over time.  Just use the normal Github fork/pull request process in order to submit patches.

Before embarking on major changes please file a new Issue with your planned enhancement so we can discuss whether it is appropriate.

Thanks.

## Getting Started

These instructions are for Unix/OS X, you will have to modify these a bit to get going on Windows.  Consult your favorite Windows Python guru for details.

#### 1. Check out the repository:

```
  % git clone git://github.com/nyaruka/klab.git
  % cd klab
```

#### 2. Create a virtual environment and active it:

```  
  % virtualenv env
  % source env/bin/activate
```

#### 3. Initialize it with all the required libraries:

```   
  % pip install -r pip-freeze.txt
```

#### 4. Symlink your dev settings file:

```
  % cd klab
  % ln -s settings.py.dev settings.py
  % cd ..
```

#### 5. Initialize our database:

```
  % python manage.py syncdb
  % python manage.py migrate
```

#### 6. Load our test data

```
  % python manage.py loaddata ../test_data.json
```

#### 7. Start the server:

```
  % python manage.py runserver
```

You should now be able to load and interact with the kLab website at: http://localhost:8000/
