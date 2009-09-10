%define name codeville
%define oname Codeville
%define version 0.8.0
%define release %mkrel 5

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


