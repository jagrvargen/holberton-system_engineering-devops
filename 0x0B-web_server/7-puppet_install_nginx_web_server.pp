# Answer file for 7-puppet_install_nginx_web_server.pp
include stdlib
exec { 'apt update':
  command => '/usr/bin/apt update',
}->
package { 'nginx':
  ensure => present,
  provider => 'apt',
}->
exec { 'nginx begins':
  command => '/etc/init.d/nginx start',
}->
file { 'alter default index.html page':
  path => '/usr/share/nginx/html/index.html',
  ensure => present,
  content => 'Holberton School',
}->
file_line { 'redirect':
  path => '/etc/nginx/sites-enabled/default',
  line => "server { \nlocation /redirect_me { \n return 301 /; \n }",
  match => '^server {',
}->
exec { 'restart Nginx':
  command => '/etc/init.d/nginx restart',
}

#file { 'alter /var/www/html':
#  path => '/var/www/html/index.nginx-debian.html',
#  ensure => present,
#  content => 'Holberton School',
#}->
