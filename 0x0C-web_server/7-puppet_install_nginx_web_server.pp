# install and configure an Nginx server using Puppet instead of Bash

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
  name   => 'nginx'
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Holberton School',
}

file_line { 'put_in_line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => '/listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => [Package['nginx'], Exec['apt-update']],
}
