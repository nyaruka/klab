# Django settings for klab project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'klab.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Kigali'

USE_TZ=True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

DATE_FORMAT = "d-m-Y"
DATETIME_FORMAT = "d-m-Y H:i"

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Flickr key
FLICKR_KEY = '1d3206d8ecc5cd053f071a19acf3bbfd'

# Flickr secret
FLICKR_SECRET = '36149060106ca80e'

# Flickr user@id
FLICKR_USER_ID = '77982146@N08'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8&k54&4x%kv-rdtb*j&!a7nt@v@rwsie8g72_3lm6y%#%+lli1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.contrib.messages.context_processors.messages',
   'django.core.context_processors.request',
   'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

#-----------------------------------------------------------------------------------
# Email Backend
#-----------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Put your gmail account here'
EMAIL_HOST_PASSWORD = 'Put your gmail password here'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'website@klab.rw'

#-----------------------------------------------------------------------------------
# Permission Configuration
#-----------------------------------------------------------------------------------
# create the smartmin CRUDL permissions on all objects
PERMISSIONS = {
  '*': ('create', # can create an object
        'read',   # can read an object, viewing it's details
        'update', # can update an object
        'delete', # can delete an object,
        'list'),  # can view a list of the objects
  'members.application': ('csv', ),
  'members.member' : ('myprofile', 'new'),
  'projects.project' : ('shortlist',),
}

# assigns the permissions that each group should have, here creating an Administrator group with
# authority to create and change users
GROUP_PERMISSIONS = {
    "Administrator": ('auth.user.*', 
                      'events.event.*', 
                      'blog.post.*', 
                      'django_quickblocks.quickblock.*', 'django_quickblocks.quickblocktype.*', 
                      'members.application.*', 'projects.project.*',
                      'members.member_create',
                      'members.member_read',
                      'members.member_update',
                      'members.member_delete',
                      'members.member_list',
                      'members.member_new',
                      'opportunities.opportunity.*',
                      ),
    "Editors": ('events.event.*', 
                'blog.post.*', 
                'django_quickblocks.quickblock.*', 
                'members.application_list', 'members.application_read', 'members.application_csv',
                'projects.project.*',
                'members.member_create',
                'members.member_read',
                'members.member_update',
                'members.member_delete',
                'members.member_list',
                'members.member_new',
                'opportunities.opportunity.*',
                ),

    "Members": ('members.member_read',
                'members.member_myprofile',
                'projects.project_create', 'projects.project_update', 'projects.project_shortlist', 'projects.project_read'),
}

#-----------------------------------------------------------------------------------
# Login / Logout
#-----------------------------------------------------------------------------------
LOGIN_URL = "/users/login/"
LOGOUT_URL = "/users/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

#-----------------------------------------------------------------------------------
# Guardian Configuration
#-----------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# this is required by guardian
ANONYMOUS_USER_ID = -1

#-----------------------------------------------------------------------------------
# Django-Nose config
#-----------------------------------------------------------------------------------

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

#-----------------------------------------------------------------------------------
# Directory Configuration
#-----------------------------------------------------------------------------------
import os

ROOT_URLCONF = 'klab.urls'

PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))

FIXTURE_DIRS = (os.path.join(PROJECT_DIR,  '../fixtures'),)
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, '../templates'),)
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../static'), os.path.join(PROJECT_DIR, '../media'), )
STATIC_ROOT = os.path.join(PROJECT_DIR, '../sitestatic')
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.humanize',

    # error logging
    'raven.contrib.django',

    # necessary apps
    'nose',
    'south',
    'guardian',
    'smartmin',
    'compressor',
    'sorl.thumbnail',
    'pagination',
    'django_quickblocks',
    'django_notify',
    'mptt',
    'sekizai',

    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',

    # smartmin users app
    'smartmin.users',

    # project's apps
    'blog',
    'events',
    'public',
    'members',
    'projects',
    'opportunities',
)

# cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django-cache'
    }
}





# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
