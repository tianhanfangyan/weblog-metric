"""
Django settings for weblog_base project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f0u24)98#0z28j+zbr0jfam4qtb3#+5dc0c!54_+sbny3kl5wz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOG_PATH = './'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weblog_base',
    'weblog_show'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'weblog_base.urls'

WSGI_APPLICATION = 'weblog_base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'web_log',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'TEST_CHARSET': "utf8",
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_DIR+'/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
                'format': '%(levelname)s %(asctime)s %(message)s'
                },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
         'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'debug.log',
            'maxBytes': 1024*1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'error': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'error.log',
            'maxBytes': 1024*1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'apis': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'apis.log',
            'maxBytes': 1024*1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'error': {
            'handlers': ['error'],
            'level': 'DEBUG',
            'propagate': False
        },
        'apis': {
            'handlers': ['apis'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

OPENTSDBTAG_REGEX = [
    #stats_byhost.openapi_access.webv2-yf-core-inner-docker.byhost.10_75_24_234.http_2xx._2_statuses_count_json.bytes
    {"regexStr":r"^([\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.byhost)\.(?P<ip>[0-9_\*]{1,15})\.(http_2xx|http_4xx|http_4xx|http_5xx|total)\.(?P<api>[\s\S][^\.]*)\.(hits|bytes|less_1s|less_2s|less_4s|less_500ms|over_4s)$",
     "index":{'srcIP':2,'api':4,'group':5},
     "replace":"__"
    },
    #stats_byhost.openapi_profile.fanservice_web-tc-inner.byhost.10_77_109_71.HTTP.fanservice_dm_attachment.interval2
    {"regexStr":r"^([\s\S][^\.|^\*]*\.openapi_profile\.[\s\S][^\.|^\*]*\.byhost)\.(?P<ip>[0-9_\*]{1,15})\.([\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.(interval1|interval2|interval3|interval4|interval5|slow_count|total_count)$",
     "index":{'srcIP':2,'api':4,'group':5},
     "replace":"__"
    },
    #stats_byhost.timers.openapi_access.remind-aliyun-outer-docker.byhost.10_85_1_20.http_2xx._2_remind_push_count_json.std
    {"regexStr":r"^([\s\S][^\.|^\*]*\.timers\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.byhost)\.(?P<ip>[0-9_\*]{1,15})\.(http_2xx|http_4xx|http_5xx|total)\.(?P<api>[\s\S][^\.]*)\.(mean)$",
     "index":{'srcIP':2,'api':4,'group':5},
     "replace":"__"
    },
    #stats_byhost.timers.openapi_profile.blossom-tc-inner.byhost.10_73_14_31.API._appinfo_delete.avg_time.mean
    {"regexStr":r"^([\s\S][^\.|^\*]*\.timers\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.byhost)\.(?P<ip>[0-9_\*]{1,15})\.([\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.(avg_time\.mean)$",
     "index":{'srcIP':2,'api':4,'group':5},
     "replace":"__"
    },
    #stats_byhost.keyValue.openapi_access.directmessage-tc-outer-docker.byhost.10_73_32_214.total._2_direct_messages_block_batch_json.bytes
    {"regexStr":r"^([\s\S][^\.|^\*]*\.keyValue\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.byhost)\.(?P<ip>[0-9_\*]{1,15})\.([\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.([\s\S][^\.|^\*]*)$",
     "index":{'srcIP':2,'api':4,'group':5},
     "replace":"__"
    },
    #stats_byhost.keyValue.openapi_jvm.directmessage-yf-inner-docker.JVM.10_13_1_88.JVMTotal.GCTime
    {"regexStr":r"^([\s\S][^\.|^\*]*\.keyValue\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.JVM)\.(?P<ip>[0-9_\*]{1,15})\.(JVMTotal\.[\s\S][^\.|^\*]*)$",
     "index":{'srcIP':2,'group':3},
     "replace":"__"
    },
    #stats_byhost.openapi_access.webv2-yf-core-inner-docker.http_2xx._2_statuses_count_json.hits
    {"regexStr":r"^([\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*)\.(http_2xx|http_4xx|http_5xx|total)\.(?P<api>[\s\S][^\.]*)\.(hits|bytes|less_1s|less_2s|less_4s|less_500ms|over_4s)$",
     "index":{'api':3,'group':4},
     "replace":"__"
    },
    #stats_byhost.openapi_profile.fanservice_web-tc-inner.REDIS.fanservice_tauth.interval1
    {"regexStr":r"^([\s\S][^\.|^\*]*\.openapi_profile\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.(interval1|interval2|interval3|interval4|interval5|slow_count|total_count)$",
     "index":{'api':2,'group':3},
     "replace":"__"
    },
    #/*stats_byhost.timers.openapi_access.blossom-tc-inner-docker.http_2xx._2_appinfo_get_app_json.mean*/
    {"regexStr":r"^([\s\S][^\.|^\*]*\.timers\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.(std|mean|upper|lower|count|count_ps|sum|sum_squares|median|count_90|mean_90|upper_90|sum_90|sum_squares_90)$",
     "index":{'api':2,'group':3},
     "replace":"__"
    },
    #/*stats_byhost.timers.openapi_profile.camera_remind-tc-docker.REDIS.rm8601_eos_grid_sina_com_cn_8601.avg_time.mean*/
    {"regexStr":r"^([\s\S][^\.|^\*]*\.timers\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.(avg_time)\.(std|mean|upper|lower|count|count_ps|sum|sum_squares|median|count_90|mean_90|upper_90|sum_90|sum_squares_90)$",
     "index":{'api':2,'group':4},
     "replace":"__"
    },
    #stats_byhost.keyValue.openapi_tauth2_access.tauth2_tc.TAUTH2.1199065384.total_count
    {"regexStr":r"^([\s\S][^\.|^\*]*\.keyValue\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*\.[\s\S][^\.|^\*]*)\.(?P<api>[\s\S][^\.]*)\.([\s\S][^\.|^\*]*)$",
     "index":{'api':2,'group':3},
     "replace":"__"
    }

]
