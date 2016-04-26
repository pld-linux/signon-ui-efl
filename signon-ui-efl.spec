Summary:	EFL based authentication UI for accounts-sso
Summary(pl.UTF-8):	Oparty na EFL interfejs użytkownika do uwierzytelniania dla accounts-sso
Name:		signon-ui-efl
Version:	0.0.3
Release:	1
License:	GPL v3
Group:		X11/Applications
#Source0Download: https://gitlab.com/accounts-sso/signonui-efl/tags
Source0:	https://gitlab.com/accounts-sso/signonui-efl/repository/archive.tar.bz2?ref=upstream/%{version}&fake_out=/%{name}-%{version}.tar.bz2
# Source0-md5:	953ccf370b6acb25e0ee0a58b4f1a911
URL:		https://gitlab.com/accounts-sso/signonui-efl
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	ecore-devel
BuildRequires:	elementary-devel
BuildRequires:	evas-devel
# ewebkit2
BuildRequires:	ewebkit-devel
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gsignond-devel
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libnotify-devel
BuildRequires:	libproxy-devel
BuildRequires:	libsignon-qt5-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFL based authentication UI for accounts-sso.

%description -l pl.UTF-8
Oparty na EFL interfejs użytkownika do uwierzytelniania dla
accounts-sso.

%prep
%setup -q -n signonui-efl-upstream
cd %{version}-72daf63a2d7a896e4b308d5b0d429b42747fa23a

%{__sed} -i -e 's/-Werror //' src/Makefile.am

%build
cd %{version}-72daf63a2d7a896e4b308d5b0d429b42747fa23a
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-webkit2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd %{version}-72daf63a2d7a896e4b308d5b0d429b42747fa23a

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{version}-72daf63a2d7a896e4b308d5b0d429b42747fa23a/{AUTHORS,README}
%attr(755,root,root) %{_libexecdir}/signonui-efl
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
