%define         clutter_version 0.10

Name:           clutter-gtk
Version:        0.10.2
Release:        2%{?dist}
Summary:        A basic GTK clutter widget

Group:          Development/Languages
License:        LGPLv2+
URL:            http://www.clutter-project.org
Source0:        http://www.clutter-project.org/sources/%{name}/%{clutter_version}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel clutter-devel

%description
This allows clutter to be embedded in GTK applications. 
We hope with further work in the future clutter-gtk will 
also allow the reverse, namely embedding GTK in Clutter

%package devel
Summary:        Clutter-gtk development environment
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gtk2-devel clutter-devel

%description devel
Header files and libraries for building a extension library for the
clutter-gtk


%prep
%setup -q


%build
%configure --disable-introspection
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS
%exclude %{_libdir}/*.la
%{_libdir}/*.so.*
%{_datadir}/gtk-doc/html/clutter-gtk

%files devel
%defattr(-,root,root,-)
%doc
%{_libdir}/pkgconfig/clutter-gtk-%{clutter_version}.pc
%{_libdir}/*.so
%{_includedir}/clutter-1.0/clutter-gtk

%changelog
* Fri Jan  8 2010 Owen Taylor <otaylor@redhat.com> - 0.10.2-2
- Remove gir-repository-devel requirement, and disable introspection support
  Related: rhbz 553806

* Mon Sep 14 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.10.2-1.1
- Add BuildRequires: gir-repository-devel

* Wed Jul 29 2009 Bastien Nocera <bnocera@redhat.com> 0.10.2-1
- Update to 0.10.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Bastien Nocera <bnocera@redhat.com> 0.9.2-1
- Update to 0.9.2

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.9.0-2
- Rebuild for new clutter

* Tue May 26 2009 Bastien Nocera <bnocera@redhat.com> 0.9.0-1
- Update to 0.9.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Fri Jan 23 2009 Allisson Azevedo <allisson@gmail.com> 0.8.2-2
- Rebuild

* Wed Oct 15 2008 Allisson Azevedo <allisson@gmail.com> 0.8.2-1
- Update to 0.8.2

* Sat Sep  6 2008 Allisson Azevedo <allisson@gmail.com> 0.8.1-1
- Update to 0.8.1

* Thu Jun 26 2008 Colin Walters <walters@redhat.com> 0.6.1-1
- Update to 0.6.1 so we can make tweet go
- Loosen files globs so we don't have to touch them every version

* Thu Feb 21 2008 Allisson Azevedo <allisson@gmail.com> 0.6.0-1
- Update to 0.6.0

* Mon Sep  3 2007 Allisson Azevedo <allisson@gmail.com> 0.4.0-1
- Update to 0.4.0

* Thu May 10 2007 Allisson Azevedo <allisson@gmail.com> 0.1.0-3
- fix devel files section

* Thu May 10 2007 Allisson Azevedo <allisson@gmail.com> 0.1.0-2
- INSTALL removed from docs
- fix make install for keeping timestamps
- fix devel files section
- changed license for LGPL

* Fri Apr 13 2007 Allisson Azevedo <allisson@gmail.com> 0.1.0-1
- Initial RPM release
