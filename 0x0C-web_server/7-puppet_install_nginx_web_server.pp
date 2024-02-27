# nginx_setup.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create a custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

# Enable custom configuration for redirection
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Notify Nginx to reload configuration
exec { 'reload_nginx':
  command     => 'service nginx reload',
  refreshonly => true,
  subscribe   => [File['/etc/nginx/sites-available/default'], File['/var/www/html/custom_404.html']],
}

# Ensure Nginx is listening on port 80
firewall { '80':
  proto  => 'tcp',
  action => 'accept',
}


