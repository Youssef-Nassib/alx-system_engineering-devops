#kill me now

exec { 'kill killmenow process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
