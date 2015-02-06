%define module	pyPdf

Summary:	Pure-Python PDF toolkit
Name:		python-pypdf
Version:	1.13
Release:	3
Source0:	http://pybrary.net/pyPdf/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pybrary.net/pyPdf/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	%{module}
BuildRequires:	python-devel
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
%{py_puresitedir}/pyPdf-%{version}-py%{py_ver}.egg-info
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


%changelog
* Mon Jan 30 2012 Vladimir Testov <vladimir.testov@rosalab.ru> 1.13-2
+ Revision: 769808
- fixed: replaced %%{pyver} with %%{py_ver}
- fixed: replaced %%{pyver} to %%cd /home/icedphoenix/PKG/python-pypdf/SPECS

* Sat Jan 08 2011 Luc Menut <lmenut@mandriva.org> 1.13-1mdv2011.0
+ Revision: 630620
- update to 1.13

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - use %%pyver macro

* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.12-2mdv2011.0
+ Revision: 590472
- rebuild for python-2.7
- drop the obsolete %%py_requires macro

* Sun Aug 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.12-1mdv2010.0
+ Revision: 422582
- change layout

  + Luc Menut <lmenut@mandriva.org>
    - import python-pypdf

