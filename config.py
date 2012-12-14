import os

# configuration
PROJECT_PATH = os.getcwd() + '/'
STATIC_PATH = PROJECT_PATH + 'static/'
IMAGES_PATH = STATIC_PATH + 'images/'

SITE_URL = 'http://127.0.0.1:8000'
STATIC_URL = SITE_URL + '/static/'
IMAGES_URL = STATIC_URL + 'images/'

DATABASE = 'sqlite:////' + PROJECT_PATH + 'portfolio.db'

# MySQL
#DATABASE = "mysql://name:password@localhost/base_name"

DEBUG = True

# Very secret passphrase
SECRET_KEY = 'VERYVERYVERYSECRETSECRET'

USERNAME = 'admin'
PASSWORD = 'admin'

EMAIL = "username@mail.com"

GOOGLE_ANALYTICS= """<script type="text/javascript">
        var _gaq = _gaq || [];
        _gaq.push(['_setAccount', 'UA-XXXXXXXX-X']);
        _gaq.push(['_trackPageview']);

        (function () {
            var ga = document.createElement('script');
            ga.type = 'text/javascript';
            ga.async = true;
            ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(ga, s);
        })();
    </script>
"""