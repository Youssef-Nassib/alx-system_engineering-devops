#killme 

exec { 'kill killmenow process':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
