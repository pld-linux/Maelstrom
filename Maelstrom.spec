Summary:	Rockin' asteroids game
Summary(pl):	Gra, w której strzelasz do asteroidów
Name:		Maelstrom
Version:	3.0.5
Release:	1
License:	GPL for code, artwork and sounds can be redistributed only with Maelstrom
Group:		X11/Application/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/src/%{name}-%{version}.tar.gz
Source1:	http://mops.uci.agh.edu.pl/~gotar/%{name}.desktop
Patch0:		http://mops.uci.agh.edu.pl/~gotar/%{name}-cheaters.patch
URL:		http://www.devolution.com/~slouken/Maelstrom/
BuildRequires:	SDL-devel
BuildRequires:	SDL_net-devel
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maelstrom is a rockin' asteroids game ported from the Macintosh
Originally written by Andrew Welch of Ambrosia Software, and ported
to UNIX and then SDL by Sam Lantinga <slouken@devolution.com>.

%description -l pl
Maelstrom jest kosmiczn± strzelank± sportowan± na UNIXy i SDL przez
Sama Lantinga <slouken@devolution.com>, oryginalnie napisan± na
Macintosha przez Andrew Welcha z Ambrosia Software.

%prep
%setup	-q
# everlasting shield, more shots available, all-in-one equipment and
# reversed bonus in time function ;)
#%patch0 -p1

%build
# make install forgets to install binaries
#aclocal
#%{__autoconf}
#%{__automake}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/X11R6,%{_applnkdir}/Games/Arcade}

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/X11R6
rm -f $RPM_BUILD_ROOT%{_prefix}/games/Maelstrom/Images/Makefile*
rm -f Docs/Makefile*

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changelog COPYING CREDITS Docs
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%{_prefix}/games/Maelstrom/Images
%{_prefix}/games/Maelstrom/Maelstrom_*
%{_prefix}/games/Maelstrom/icon.*
%attr(666,root,root) %config(noreplace) %verify(not md5 size mtime) %{_prefix}/games/Maelstrom/Maelstrom-Scores
%{_applnkdir}/Games/Arcade/*
