#!/usr/bin/tclsh

set arch "noarch"
set base "dbif-1.3"
set fileurl "https://chiselapp.com/user/schelte/repository/dbif/tarball/dbif-4898c5e31c.tar.gz?uuid=4898c5e31c8f6b6433f9e4d392b97886dd92783fb62f6fb50dbe725df9e03327"

set var [list wget $fileurl -O dbif.tar.gz]
exec >@stdout 2>@stderr {*}$var

set var [list tar xzvf dbif.tar.gz]
exec >@stdout 2>@stderr {*}$var

file delete dbif.tar.gz

set var [list mv dbif-4898c5e31c $base]
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

