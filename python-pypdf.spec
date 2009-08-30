%define module	pyPdf

Summary:	Pure-Python PDF toolkit
Name:		python-pypdf
Version:	1.12
Release:	%mkrel 1
Source0:	http://pybrary.net/pyPdf/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pybrary.net/pyPdf/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{module}
%py_requires -d
BuildArch:	noarch

%description
A Pure-Python library built as a PDF toolkit. It is capable of:
    * extracting document information (title, author, ...),
    * splitting documents page by page,
    * merging documents page by page,
    * cropping pages,
    * merging multiple pages into a single page,
    * encrypting and decrypting PDF files.

%files
%defattr(-,root,root)
%doc README CHANGELOG
%{py_puresitedir}/pyPdf-1.12-py2.6.egg-info
%dir %{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --no-compile

%clean
%__rm -rf %{buildroot}