Summary:	C++ Template Image Processing Library
Summary(pl.UTF-8):	Biblioteka szablonów C++ do przetwarzania obrazu
Name:		CImg
Version:	3.5.3
Release:	1
License:	CeCILL-C v1 or CeCILL v2
Group:		Development/Libraries
Source0:	http://cimg.eu/files/%{name}_%{version}.zip
# Source0-md5:	b7e07db5ff0f3c02a2c50192982bc318
URL:		http://cimg.eu/
BuildRequires:	unzip
Requires:	libstdc++-devel >= 6:4
Requires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CImg Library is an open-source C++ toolkit for image processing.
It consists in a single header file 'CImg.h' providing a set of C++
classes and functions that can be used in your own sources, to
load/save, process and display images. Very portable (Unix/X11,
Windows, MacOS X, FreeBSD, ...), efficient, easy to use, it's a
pleasant toolkit for coding image processing stuffs in C++.

%description -l pl.UTF-8
Biblioteka CImg to toolkit C++ o otwartych źródłach służący do
przetwarzania obrazu. Składa się z pojedynczego pliku nagłówkowego
CImg.h udostępniającego zbiór klas i funkcji C++, które można
wykorzystać we własnych źródłach do wczytywania, zapisywania,
przetwarzania i wyświetlania obrazów. Jest przenośny (Unix/X11,
Windows, MacOS X, FreeBSD...), wydajny, łatwy w użyciu i przyjemny do
kodowania przetwarzania obrazu w C++.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name}/plugins,%{_examplesdir}/%{name}-%{version}/img}

install CImg.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install plugins/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/plugins
install examples/{*.cpp,*.m,Makefile} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/img/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Licence* README.txt
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/CImg.h
%{_includedir}/%{name}/plugins
%{_examplesdir}/%{name}-%{version}
