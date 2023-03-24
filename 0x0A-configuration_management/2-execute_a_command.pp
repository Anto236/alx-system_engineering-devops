# create a manifest that kills a process named killmenow.

exec { 'pkill_killmenow_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/local/bin', '/bin'],
}
