# fix wordpress bug - a typo in the file
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
