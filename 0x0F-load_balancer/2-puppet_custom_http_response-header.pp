# Answer file for 0x0F - Load Balancer
# Sets a custom http header response for an Nginx web server
include stdlib
exec { 'update':
  command  => '/usr/bin/apt update',
}->
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}->
file { 'ensure default':
  path     => '/etc/nginx/sites-enabled/default',
  ensure   => present,
}->
file_line { 'add custom header':
  path     => '/etc/nginx/sites-enabled/default',
  line     => "server { \n        add_header X-Served-By \$hostname; \n ",
  match    => "^server {",
}->
exec { 'restart':
  command  => '/etc/init.d/nginx restart',
}
