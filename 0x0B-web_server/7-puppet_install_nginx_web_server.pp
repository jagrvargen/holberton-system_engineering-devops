# Installs and configures nginx
include stdlib
package { 'install nginx':
  name   => 'nginx',
  ensure => 'present',
}->
file_line { 'add Holberton School to index.html':
  path => '/usr/share/nginx/html/index.html',
  line => 'Hello Holberton',
}->
file_line { 'Add 301 redirect':
  path  => '/etc/nginx/sites-available/default',
  match  => "^server\s+{\n",
  line => "server {\n\tlocation /redirect_me {\n\t\trewrite ^/.*$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n}\n",
}->
exec{ 'restart nginx':
  command => 'systemctl nginx restart',
}
