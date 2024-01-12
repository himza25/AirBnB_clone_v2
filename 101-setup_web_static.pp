# 101-setup_web_static.pp
class web_static_setup {
    # Ensure Nginx is installed
    package { 'nginx':
        ensure => installed,
    }

    # Ensure directories are present and have correct owner and group
    file { '/data':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/releases':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/shared':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/releases/test':
        ensure => directory,
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    # Create a fake HTML file
    file { '/data/web_static/releases/test/index.html':
        ensure  => present,
        content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
        owner   => 'ubuntu',
        group   => 'ubuntu',
    }

    # Create a symbolic link
    file { '/data/web_static/current':
        ensure => link,
        target => '/data/web_static/releases/test',
        force  => true,
        require => File['/data/web_static/releases/test/index.html'],
    }

    # Update Nginx configuration
    exec { 'update_nginx_config':
        command => "sed -i '/server_name _;/a \\\n\\tlocation /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}\\n' /etc/nginx/sites-available/default",
        onlyif  => "grep -q 'server_name _;' /etc/nginx/sites-available/default",
        notify  => Service['nginx'],
    }

    # Ensure the Nginx service is running and enabled
    service { 'nginx':
        ensure => running,
        enable => true,
    }
}

include web_static_setup
