# /path/to/101-setup_web_static.pp
# Puppet manifest to set up web servers for deployment of web_static

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { [
    '/data',
    '/data/web_static',
    '/data/web_static/releases',
    '/data/web_static/shared',
    '/data/web_static/releases/test',
  ]:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  force  => true,
}

# Configure Nginx
exec { 'nginx-config':
  command => 'ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/',
  unless  => 'test -L /etc/nginx/sites-enabled/default',
  notify  => Service['nginx'],
}

file_line { 'nginx-server-block':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n",
  match   => '^server_name _;',
  append_on_no_match => true,
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
