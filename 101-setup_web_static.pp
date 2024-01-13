# 101-setup_web_static.pp
class web_static_setup {
    # Ensure Nginx is installed
    package { 'nginx':
        ensure => installed,
    }

    # Create required directories
    file {
        '/data':
            ensure => 'directory',
            owner  => 'ubuntu',
            group  => 'ubuntu';

        '/data/web_static':
            ensure => 'directory',
            owner  => 'ubuntu',
            group  => 'ubuntu';

        '/data/web_static/releases':
            ensure => 'directory',
            owner  => 'ubuntu',
            group  => 'ubuntu';

        '/data/web_static/shared':
            ensure => 'directory',
            owner  => 'ubuntu',
            group  => 'ubuntu';

        '/data/web_static/releases/test':
            ensure => 'directory',
            owner  => 'ubuntu',
            group  => 'ubuntu';
    }

    # Create a fake HTML file
    file { '/data/web_static/releases/test/index.html':
        ensure  => 'present',
        content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
        owner   => 'ubuntu',
        group   => 'ubuntu',
        mode    => '0644',
    }

    # Create a symbolic link
    file { '/data/web_static/current':
        ensure => 'link',
        target => '/data/web_static/releases/test',
        require => File['/data/web_static/releases/test/index.html'],
        force => true,
    }

    # Update Nginx configuration
    exec { 'nginx_config_update':
        command => "sed -i '/server_name _;/a \\\n\\tlocation /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}\\n' /etc/nginx/sites-available/default",
        refreshonly => true,
        subscribe => Package['nginx'],
    }

    # Ensure Nginx is restarted to apply the changes
    service { 'nginx':
        ensure    => 'running',
        enable    => true,
        subscribe => Exec['nginx_config_update'],
    }
}

include web_static_setup
