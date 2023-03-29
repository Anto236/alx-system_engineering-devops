# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled on boot
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    # Redirect /redirect_me
    if ($request_uri = /redirect_me) {
        return 301  https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    # Handle root request
    location / {
        return 200 "Hello World!";
    }
}
',
  notify => Service['nginx'],
}

# Restart Nginx service after configuration changes
exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  refreshonly => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
