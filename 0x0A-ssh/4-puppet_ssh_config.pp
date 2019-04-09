# Configures the /etc/ssh/config file to allow ssh connection
# w/o password authentication and sets the identity file to
# ~/.ssh/holberton
include stdlib
file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#\s+PasswordAuthentication yes|^\s+PasswordAuthentication yes',
}->
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/holberton',
}
