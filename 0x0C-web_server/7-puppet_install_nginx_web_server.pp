# Define a class for installing and configuring Nginx
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page",
  }

  file { '/etc/nginx/sites-available/default':
    content => template('nginx/default.erb'),
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

# Define a template for the Nginx configuration file
# that includes a redirect for /redirect_me
# and a custom 404 page
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
}

# Set up the redirect for /redirect_me
nginx::config { 'redirect':
  from   => '/',
  to     => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
  status => 301,
}

# Define the Nginx class as the default class to be applied to the node
node default {
  include nginx
}
