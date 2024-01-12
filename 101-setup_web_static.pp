# 101-setup_web_static.pp
class web_static_setup {
    package { 'nginx':
        ensure => installed,
    }

    file { '/data/web_static':
        ensure => 'directory',
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/releases':
        ensure => 'directory',
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/shared':
        ensure => 'directory',
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/releases/test':
        ensure => 'directory',
        owner  => 'ubuntu',
        group  => 'ubuntu',
    }

    file { '/data/web_static/releases/test/index.html':
        ensure  => 'present',
        content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
        owner   => 'ubuntu',
        group   => 'ubuntu',
    }

    file { '/data/web_static/current':
        ensure => 'link',
        target => '/data/web_static/releases/test',
        force  => true,
        require => File['/data/web_static/releases/test/index.html'],
    }

    exec { 'update_nginx_config':
        command => "sed -i '/server_name _;/a \\\n\\tlocation /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}\\n' /etc/nginx/sites-available/default",
        refreshonly => true,
        subscribe => File['/data/web_static/current'],
    }

    service { 'nginx':
        ensure => running,
        enable => true,
        require => Exec['update_nginx_config'],
    }
}

include web_static_setup
