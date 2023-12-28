# WordPress Structures

## File Structure
```bash
tree -L 1 /var/www/html

├── index.php
├── license.txt
├── readme.html
├── wp-activate.php
├── wp-admin
├── wp-blog-header.php
├── wp-comments-post.php
├── wp-config.php
├── wp-config-sample.php
├── wp-content
├── wp-cron.php
├── wp-includes
├── wp-links-opml.php
├── wp-load.php
├── wp-login.php
├── wp-mail.php
├── wp-settings.php
├── wp-signup.php
├── wp-trackback.php
└── xmlrpc.php
```

## Key WordPress files

- `__index.php__` - homepage of WordPress
- `__license.txt__`- contains useful information of the installed WordPress
- `__wp-activate.php__` - used for the email activation process
- `__wp-admin__` - contains the login page for administrator access and the backend dashboard. The login page can be located at one of the following paths:
	- /wp-admin/login.php
	- /wp-admin/wp-login.php
	- /login.php
	- /wp-login.php

## WorPress Configuration File
- `__wp-config.php__` file contains infomratino required by WordPress to connect to the databases ( names, hosts, usernames & passwords, etc.)

```php
<?php
/** <SNIP> */
/** The name of the database for WordPress */
define( 'DB_NAME', 'database_name_here' );

/** MySQL database username */
define( 'DB_USER', 'username_here' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password_here' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Authentication Unique Keys and Salts */
/* <SNIP> */
define( 'AUTH_KEY',         'put your unique phrase here' );
define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
define( 'NONCE_KEY',        'put your unique phrase here' );
define( 'AUTH_SALT',        'put your unique phrase here' );
define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
define( 'NONCE_SALT',       'put your unique phrase here' );

/** WordPress Database Table prefix */
$table_prefix = 'wp_';

/** For developers: WordPress debugging mode. */
/** <SNIP> */
define( 'WP_DEBUG', false );

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
```

## Key WordPress directories
- `__wp-content__` is the main directory where plugins and themes are stored. Its subdirectory `__uploads__` is where uploaded files are stored.

```bash
tree -L 1 /vaw/www/html/wp-content
.
├── index.php
├── plugins
└── themes
```

- `__wp-includes__` contains everything except for the administrative comonents and teh themes that belong to the website. Thisis where core files are stored (certificates, fonts, JS files,widget, etc.)

```bash
tree -L 1 /var/www/html/wp-includes
.
├── <SNIP>
├── theme.php
├── update.php
├── user.php
├── vars.php
├── version.php
├── widgets
├── widgets.php
├── wlwmanifest.xml
├── wp-db.php
└── wp-diff.php
```
