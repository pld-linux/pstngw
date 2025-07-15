Summary:	H.323 to PSTN gateway
Summary(pl.UTF-8):	Bramka H.323 -> PSTN
Name:		pstngw
Version:	1.2.2
Release:	2
License:	MPL 1.0
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	42cf263a23b45ee962a026b463050ce2
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.12.0
BuildRequires:	pwlib-devel >= 1.4.11
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple PSTN to H.323 gateway program using the OpenH323
library. It allows H.323 clients to make outgoing calls, and incoming
calls to be routed to a specific H.323 client.

%description -l pl.UTF-8
To jest bardzo prosta bramka H.323 -> PSTN używająca biblioteki OpenH323.
Pozwala klientom H.323 na nawiązywania połączeń, oraz na przekierowywanie
połączeń przychodzących do odpowiedniego klienta.

%prep
%setup -qn %{name}
%patch -P0 -p1

%build
%{__make} %{?debug:debug}%{!?debug:opt}shared \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

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
