# Changes a php filename in order to fix server malfunction
exec { '/bin/mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp':
  creates => '/var/www/html/wp-includes/class-wp-locale.phpp',
}

->

file {  '/var/www/html/wp-includes/class-wp-locale.php':
  ensure => absent,
}
