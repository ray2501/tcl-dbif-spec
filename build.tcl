#!/usr/bin/tclsh

set arch "noarch"
set base "dbif-1.3"
set fileurl "http://chiselapp.com/user/schelte/repository/dbif/tarball/dbif-5c978c81f0.tar.gz?uuid=5c978c81f0bea85fbf0f3549833d30cf7194899621af5dc1e042e0ae7ddfaf47"

set var [list wget $fileurl -O dbif.tar.gz]
exec >@stdout 2>@stderr {*}$var

set var [list tar xzvf dbif.tar.gz]
exec >@stdout 2>@stderr {*}$var

file delete dbif.tar.gz

set var [list mv dbif-5c978c81f0 $base]
exec >@stdout 2>@stderr {*}$var

set var [list tar czvf $base.tar.gz $base]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-dbif.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz

