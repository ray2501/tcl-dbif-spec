#
# spec file for package tcl-dbif
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guido Berhoerster.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define upstream_name dbif

Name:           tcl-dbif
Version:        1.3
Release:        0
License:        SUSE-Permissive
Summary:        Application Layer Around the Tcl DBus Library
Url:            http://dbus-tcl.sourceforge.net/
Group:          Development/Languages/Tcl
Source:         %{upstream_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  tcl-devel
BuildRequires:  tcllib
BuildRequires:  sed
Requires:       tcl
Requires:       tcl-dbus >= 2.1
Provides:       dbus-intf = %{version}
Obsoletes:      dbus-intf <= 0.4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DBus-Intf is a Tcl library for easily providing an introspectable DBus
interface to Tcl programs. It supports the following standard DBus interface
specifications: org.freedesktop.DBus.Peer, org.freedesktop.DBus.Properties, and
org.freedesktop.DBus.Introspectable

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install moduledir=%{tcl_noarchdir}/%{upstream_name}%{version}

cat > %{buildroot}%{tcl_noarchdir}/%{upstream_name}%{version}/pkgIndex.tcl << 'EOD'
#
# Tcl package index file
#
package ifneeded dbif 1.3 \
    [list source [file join $dir dbif-1.3.tm]]
package ifneeded dbus-intf 1.3 \
    [list source [file join $dir dbif-1.3.tm]]
EOD


rm -r %{buildroot}%{_datadir}/doc/%{upstream_name}

mkdir html
cp -p doc/*.html html

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README license.terms html/ examples/
%{tcl_noarchdir}/%{upstream_name}%{version}
%doc %{_mandir}/mann/*.n*

%changelog
