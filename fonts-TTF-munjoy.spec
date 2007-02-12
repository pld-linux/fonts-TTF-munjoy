%define		_name	munjoyfonts
Summary:	munjoy fonts
Summary(pl.UTF-8):   Fonty munjoy
Name:		fonts-TTF-munjoy
Version:	0.1
Release:	1
License:	distributable
Group:		Fonts
Source0:	http://www.munjoylinux.org/source/munjoyfonts.tar.gz 
# Source0-md5:	0319cc9dc14a92814498dce3e9c74056
URL:		http://www.munjoylinux.org/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
munjoy fonts.

%description -l pl.UTF-8
Fonty munjoy.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_ttffontsdir}/*
