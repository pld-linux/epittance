Summary:	An integrated file sharing solution for the GNOME Desktop
Summary(pl):	Zintegrowane rozwi±zanie do wspó³dzielenia plików dla ¶rodowiska GNOME
Name:		epittance
Version:	0.3.0
Release:	0.2.20050502
License:	GPL v2
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/elysium-project/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	1dafd9339ce735471f08d5189e812678
URL:		http://elysium-project.sourceforge.net/epittance/
BuildRequires:	howl-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libsoup-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An integrated file sharing solution for the GNOME Desktop. It uses
WebDAV and Rendezvous.

%description -l pl
Zintegrowane rozwi±zanie do wspó³dzielenia plików dla ¶rodowiska
GNOME. U¿ywa WebDAV oraz Rendezvous.

%prep
%setup -q

%build
glib-gettextize
%{__intltoolize}
autoreconf -i
%configure
cd src
%{__make} EPittance.h
cd -
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
%attr(755,root,root) %{_libdir}/epittance-1.0/*.so
%attr(755,root,root) %{_libdir}/epittance-server
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/libepittance-nautilus.so
%{_libdir}/bonobo/servers/GNOME_EPittance.server
%{_sysconfdir}/gconf/schemas/epittance.schemas
