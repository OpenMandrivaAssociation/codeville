%define name codeville
%define oname Codeville
%define version 0.8.0
%define release %mkrel 7

Summary: Distributed version control system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.codeville.org/download/%{oname}-%{version}.tar.bz2
License: BSD
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://www.codeville.org/
BuildRequires: python-devel
Requires: python

%description
Codeville is a distributed version control system. It began with a
novel idea for a merge algorithm and has grown from there. It is
designed to be easy to use and scale from small personal projects to
very large distributed ones.

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
rm -rf %buildroot installed-docs
python setup.py install --root=$RPM_BUILD_ROOT
mv %buildroot%_datadir/doc/* installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc installed-docs/*
%_bindir/*
%py_puresitedir/Codeville/
%py_puresitedir/*egg-info




%changelog
* Thu Nov 03 2011 Götz Waschk <waschk@mandriva.org> 0.8.0-7mdv2012.0
+ Revision: 715273
- rebuild

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.8.0-6mdv2011.0
+ Revision: 592375
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.8.0-5mdv2011.0
+ Revision: 437060
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.8.0-4mdv2009.1
+ Revision: 324191
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-3mdv2009.0
+ Revision: 243589
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Michael Scherer <misc@mandriva.org> 0.8.0-1mdv2008.0
+ Revision: 55711
- 0.8.0


* Tue Dec 05 2006 Michael Scherer <misc@mandriva.org> 0.1.16-2mdv2007.0
+ Revision: 91344
- Rebuild for new python
- include egg-info
- Import codeville

