Summary:	IRC-bouncer/proxy
Name:		miau
Version:	0.6.6
Release:	3
License:	GPLv2+
Group:		Networking/IRC
Source0:	http://downloads.sourceforge.net/miau/%{name}-%{version}.tar.bz2
URL:		http://miau.sourceforge.net/

%description
Miau is a smart and versatile irc-bouncing tool for unix. The difference
between miau and other bouncers is that miau will go on irc as soon as it's
launched, guarding or attempting to get your nick. Control over the session can
be taken as with other bouncers, by simply connecting to miau (and providing a
password) like you would connect to a normal irc-server. On disconnect, miau is
able to stay in the channels and to reintroduce them to your client on your
next connect. Other handy features are message-logging, flood-protection,
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
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{_datadir}/miaurc

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO misc/miaurc
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/miau.1*


%changelog
* Mon Jun 04 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.6-2
+ Revision: 802209
- Drop some legacy junk

* Mon May 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.6-1
+ Revision: 681986
- update to new version 0.6.6

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-6mdv2011.0
+ Revision: 620325
- the mass rebuild of 2010.0 packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.6.5-5mdv2010.0
+ Revision: 436161
- rebuild
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.6.5-2mdv2008.1
+ Revision: 170981
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long

* Tue Jan 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5-1mdv2008.1
+ Revision: 155993
- new version
- new license policy
- drop useless br

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-1mdv2008.0
+ Revision: 31315
- new version


* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.3-1mdv2007.0
+ Revision: 110074
- Import miau

