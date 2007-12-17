Summary:	In short, miau is an IRC-bouncer/proxy
Name:		miau
Version:	0.6.4
Release:	%mkrel 1
License:	GPL
Group:		Networking/IRC
Source0:	http://downloads.sourceforge.net/miau/%{name}-%{version}.tar.bz2
URL:		http://miau.sourceforge.net/
Requires(post): info-install
Requires(preun): info-install
BuildRequires:	mandriva-release

%description
Miau is a smart and versatile irc-bouncing tool for unix. The difference between
miau and other bouncers is that miau will go on irc as soon as it's launched,
guarding or attempting to get your nick. Control over the session can be taken
as with other bouncers, by simply connecting to miau (and providing a password)
like you would connect to a normal irc-server. On disconnect, miau is able to
stay in the channels and to reintroduce them to your client on your next
connect. Other handy features are message-logging, flood-protection,
dcc-bouncing, etc.

%prep
%setup -q

%build
%configure \
	--enable-dccbounce \
	--enable-automode \
	--enable-releasenick \
	--enable-ctcp-replies \
	--enable-mkpasswd \
	--enable-uptime \
	--enable-chanlog \
	--enable-privlog \
	--enable-onconnect \
	--enable-empty-awaymsg
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

rm -f %{buildroot}%{_datadir}/miaurc

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}


%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO misc/miaurc
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/miau.1*
