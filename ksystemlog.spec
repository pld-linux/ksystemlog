#
# TODO:
# - update configuration file for PLD
# - suggests syslog/syslog-ng
#
Summary:	System log viewer
Summary(pl.UTF-8):	Przegladarka logów systemowych
Name:		ksystemlog
Version:	0.3.2
Release:	0.5
Epoch:		1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ksystemlog.forum-software.org/archives/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ca98b571202b6f18a9294face233b9f0
Patch0:		%{name}-desktop.patch
URL:		http://ksystemlog.forum-software.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
Suggests:	syslog-ng
#Suggests:	syslog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSystemLog aims to be as simple as possible, with menu displaying
available Logs of the system.

KSystemLog is able to read log lines from multiple files, sorting them
as quickier as possible (there are probably still some works to
improve that), auto displaying new log lines (with a bold font to
better see them), display advanced information about each lines
(level, date, message, user, process, host name, etc.).

%description -l pl.UTF-8
KSystelLog ma być jak najprostszą aplikacją z menu pokazującym
dostępne logi systemowe.

Potrafi czytać linie logów z wielu plików, sortować je jak najszybciej
(tu prawdopodobnie jest jeszcze trochę do zrobienia), automatycznie
wyświetlać nowe linie logów (grubym fontem, żeby były lepiej widoczne),
wyświetlać rozszerzone informacje o każdej linii (poziom, datę,
komunikat, użytkownika, proces, nazwę hosta itp.).

%prep
%setup -q
%patch0 -p1

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}/kde}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kdelnkdir=%{_desktopdir}

# missing in SUBDIRS
%{__make} -C ksystemlog/po install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C ksystemlog/doc install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ksystemlog
%{_datadir}/apps/ksystemlog
%{_datadir}/config.kcfg/ksystemlog.kcfg
%{_desktopdir}/ksystemlog.desktop
%{_iconsdir}/hicolor/*/apps/ksystemlog.png
%{_iconsdir}/hicolor/scalable/apps/ksystemlog.svgz
