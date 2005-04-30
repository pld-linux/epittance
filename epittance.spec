Summary:	An integrated file sharing solution for the GNOME Desktop
Name:		epittance
Version:	0.3.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net//elysium-project/%{name}-%{version}.tar.gz
# Source0-md5:	364e7f59ed0c104b33f9d0e25222962e
URL:		http://elysium-project.sourceforge.net/epittance/
BuildRequires:	howl-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libsoup-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An integrated file sharing solution for the GNOME Desktop. It uses WebDAV
and Rendezvous.

%prep
%setup -q

%build
CFLAGS="-DGETTEXT_PACKAGE %{rpmcflags}"
export CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install epittance.schemas

%preun
%gconf_schema_uninstall epittance.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/epittance-1.0
%attr(755,root,root) %{_libdir}/epittance-1.0/libepittance-webdav.so
%attr(755,root,root) %{_libdir}/epittance-server
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/libepittance-nautilus.so
%{_libdir}/bonobo/servers/GNOME_EPittance.server
%{_sysconfdir}/gconf/schemas/epittance.schemas
