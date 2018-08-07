# tcl-dbif-spec

openSUSE RPM spec for tcl-dbif.

dbif its official homepage is
[http://chiselapp.com/user/schelte/repository/dbif](http://chiselapp.com/user/schelte/repository/dbif).

It is a sub-project of dbus-tcl project. dbif is a Tcl library for easily providing
an introspectable DBus interface to Tcl programs.

This RPM spec is used to create a openSUSE RPM for tcl-dbif.

Notice:
1. The spec is from openSUSE build service and I update the dbif version.
2. After check `::tcl::tm::path`, install tm file to /usr/share/tcl/dbif1.2
   do not work. A workaround solution is to add the pkgIndex.tcl file,
   then tclsh can find dbif package

