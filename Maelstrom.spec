#
# Conditional build:
# _with_cheaters
#
Summary:	Rockin' asteroids game
Summary(pl):	Gra, w której strzelasz do asteroidów
Name:		Maelstrom
Version:	3.0.5
Release:	2
License:	GPL for code, artwork and sounds can be redistributed only with Maelstrom
Group:		X11/Application/Games
Source0:	http://www.devolution.com/~slouken/Maelstrom/src/%{name}-%{version}.tar.gz
Source1:	http://mops.uci.agh.edu.pl/~gotar/%{name}.desktop
Patch0:		http://mops.uci.agh.edu.pl/~gotar/%{name}-cheaters.patch
Patch1:		%{name}-dirs.patch
Patch2:		%{name}-amfix.patch
URL:		http://www.devolution.com/~slouken/Maelstrom/
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_gamedir	%{_datadir}/Maelstrom

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
%{?_with_cheaters:%patch0 -p1}
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/games,%{_applnkdir}/Games/Arcade}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/X11R6
rm -f $RPM_BUILD_ROOT%{_gamedir}/Images/Makefile*
rm -f Docs/Makefile*

# /usr is read-only
mv -f $RPM_BUILD_ROOT%{_gamedir}/Maelstrom-Scores $RPM_BUILD_ROOT/var/games
ln -sf /var/games/Maelstrom-Scores $RPM_BUILD_ROOT%{_gamedir}

# not needed (examples for internal Mac library)
# and playwave conflicts with SDL_mixer
rm -f $RPM_BUILD_ROOT%{_bindir}/{macres,playwave,snd2wav}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changelog COPYING CREDITS Docs
%attr(755,root,root) %{_bindir}/*
%{_gamedir}
%attr(666,root,root) %config(noreplace) %verify(not md5 size mtime) /var/games/Maelstrom-Scores
%{_applnkdir}/Games/Arcade/*
