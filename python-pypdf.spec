%define module	pyPdf

Summary:	Pure-Python PDF toolkit
Name:		python-pypdf
Version:	5.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pypdf/pypdf-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/py-pdf/pypdf
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
%{python_sitelib}/pypdf-%{version}.dist-info
%{python_sitelib}/pypdf/
#--------------------------------------------------------------------

%prep
%autosetup -n pypdf-%{version} -p1

%build
%py_build

%install
%py_install
