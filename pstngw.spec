Summary:	H.323 to PSTN gateway
Summary(pl):	Bramka H.323 -> PSTN
Name:		pstngw
Version:	1.1.3
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.8.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple PSTN to H.323 gateway program using the OpenH323
library. It allows H.323 clients to make outgoing calls, and incoming
calls to be routed to a specific H.323 client.

%description -l pl
To jest bardzo prosta bramka H.323 -> PSTN u¿ywaj±ca biblioteki OpenH323.
Pozwala klientom H.323 na nawi±zywania po³±czeñ, oraz na przekierowywanie
po³±czeñ przychodz±cych do odpowiedniego klienta.

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} optshared OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.htm
%attr(755,root,root) %{_bindir}/*
