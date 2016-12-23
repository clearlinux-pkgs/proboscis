#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : proboscis
Version  : 1.2.6.0
Release  : 14
URL      : https://pypi.python.org/packages/source/p/proboscis/proboscis-1.2.6.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/proboscis/proboscis-1.2.6.0.tar.gz
Summary  : Extends Nose with certain TestNG like features.
Group    : Development/Tools
License  : Apache-2.0
Requires: proboscis-python
BuildRequires : nose-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
Proboscis
================
Proboscis is a Python test framework that extends Python's built-in unittest
module and `Nose`_ with features from `TestNG`_.

%package python
Summary: python components for the proboscis package.
Group: Default

%description python
python components for the proboscis package.


%prep
%setup -q -n proboscis-1.2.6.0

%build
%{__python} setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
%{__python} setup.py test
%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
