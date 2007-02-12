#
# Conditional build:
%bcond_with	cheaters
#
# Straced order of file searching:
# %Maelstrom Sprites
# Maelstrom Sprites.bin
# Maelstrom Sprites
# %Maelstrom_Sprites
# Maelstrom_Sprites.bin
# Maelstrom_Sprites
#
# %Maelstrom Sounds
# Maelstrom Sounds.bin
# Maelstrom Sounds
# %Maelstrom_Sounds
# Maelstrom_Sounds.bin
# Maelstrom_Sounds

Summary:	Rockin' asteroids game
Summary(pl.UTF-8):   Gra, w której strzela się do asteroidów
Summary(pt_BR.UTF-8):   Maelstrom - um jogo tipo Asteroids muito bem-feito
Name:		Maelstrom
Version:	3.0.6
Release:	6
License:	GPL for code, artwork and sounds can be redistributed only with Maelstrom
Group:		X11/Applications/Games
# Source0-md5:	8aab0e75ca52808fd6777535ebb1f1c4
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-cheaters.patch
Patch1:		%{name}-dirs.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-sec.patch
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom
%define		specflags_ia32	 -fomit-frame-pointer 

%description
Maelstrom is a rockin' asteroids game ported from the Macintosh
Originally written by Andrew Welch of Ambrosia Software, and ported to
UNIX and then SDL by Sam Lantinga <slouken@devolution.com>.

%description -l pl.UTF-8
Maelstrom jest kosmiczną strzelanką sportowaną na Uniksy i SDL przez
Sama Lantinga <slouken@devolution.com>, oryginalnie napisaną na
Macintosha przez Andrew Welcha z Ambrosia Software.

%description -l pt_BR.UTF-8
O Maelstrom é um jogo de asteróides vagantes portado do Macintosh,
originalmente escrito por Andrew Welch da Ambrosia Software, e portado
para o UNIX e SDL por Sam Lantinga.

Sua nave está no temido círculo de asteróides "Maelstrom", e você tem
que sobreviver explodindo todos os asteróides e evitando outros
inimigos como estrelas Nova, turbilhões e naves e minas Shenobi.

Gráficos 3D muito legais e sons, com suporte a temas e jogos via rede.

%prep
%setup	-q
# everlasting shield, more shots available, all-in-one equipment and
# reversed bonus in time function ;)
%{?with_cheaters:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/games,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_gamedir}/Images/Makefile*
rm -f Docs/Makefile*

# /usr is read-only
mv -f $RPM_BUILD_ROOT%{_gamedir}/Maelstrom-Scores $RPM_BUILD_ROOT/var/games
ln -sf /var/games/Maelstrom-Scores $RPM_BUILD_ROOT%{_gamedir}

# not needed (examples for internal Mac library)
# and playwave conflicts with SDL_mixer
rm -f $RPM_BUILD_ROOT%{_bindir}/{macres,playwave,snd2wav}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changelog COPYING CREDITS Docs
%attr(2755,root,games) %{_bindir}/*
%{_gamedir}
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/Maelstrom-Scores
%{_desktopdir}/*.desktop
