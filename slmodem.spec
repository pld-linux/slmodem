# NOTE: no SMP drivers for now - I don't know if these binaries would work?
# TODO: test it on SMP and add SMP modules or update above comment
# 
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
%bcond_without  smp             # don't build SMP module
%bcond_without  up              # don't build UP module
#
Summary:	Smart Link soft modem drivers
Summary(pl):	Sterowniki do modemów programowych Smart Link
Name:		slmodem
Version:	2.9.6
%define	rel	0.1
Release:	%{rel}
License:	BSD almost without source
Vendor:		Smart Link Ltd.
Group:		Base/Kernel
# ftp://ftp.smlink.com/linux/unsupported/
Source0:	ftp://ftp.smlink.com/linux/unsupported/%{name}-%{version}.tar.gz
# Source0-md5:	ab6bdd1372fc6071c51a93697de177e9
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://www.smlink.com/
%{?with_dist_kernel:BuildRequires:	kernel-headers}
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.118
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smart Link soft modem drivers.

%description -l pl
Sterowniki do modemów programowych Smart Link.

%package -n kernel-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards.

%description -n kernel-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561.

%package -n kernel-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem.

%description -n kernel-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych  na SmartUSB56.

%package -n kernel-smp-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards. SMP kernels.

%description -n kernel-smp-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561. J±dra SMP.

%package -n kernel-smp-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem. SMP kernels.

%description -n kernel-smp-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych  na SmartUSB56. J±dra SMP.

%prep
%setup -q

%build
cp -r drivers drivers-smp

cd drivers

%if %{with up}
ln -sf %{_kernelsrcdir}/config-up .config
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf-up.h include/linux/autoconf.h
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
%{__make} -C %{_kernelsrcdir} modules \
        SUBDIRS=$PWD \
        O=$PWD \
        V=1
%endif

%if %{with smp}
cd ../drivers-smp
ln -sf %{_kernelsrcdir}/config-smp .config
rm -rf include
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf-smp.h include/linux/autoconf.h
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
%{__make} -C %{_kernelsrcdir} modules \
        SUBDIRS=$PWD \
        O=$PWD \
        V=1
%endif

%{__make} -C ../modem

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/modules/%{_kernel_ver}{,smp}/misc,%{_var}/lib/%{name}}

install modem/slmodemd $RPM_BUILD_ROOT%{_sbindir}
install modem/modem_test $RPM_BUILD_ROOT%{_sbindir}/slmodem-test

%if %{with up}
install drivers/*.ko $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc
%endif

%if %{with smp}
install drivers-smp/*.ko $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc
%endif

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/sysconfig/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel-char-slmodem-amr
%depmod %{_kernel_ver}

%postun -n kernel-char-slmodem-amr
%depmod %{_kernel_ver}

%post -n kernel-char-slmodem-usb
%depmod %{_kernel_ver}

%postun -n kernel-char-slmodem-usb
%depmod %{_kernel_ver}

%post -n kernel-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-char-slmodem-amr
%depmod %{_kernel_ver}smp

%post -n kernel-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-char-slmodem-usb
%depmod %{_kernel_ver}smp

%post
/sbin/chkconfig --add %{name}
if [ -f /var/lock/subsys/%{name} ]; then
        /etc/rc.d/init.d/%{name} restart >&2
else
        echo "Run \"/etc/rc.d/init.d/%{name} start\" to start %{name} daemon." >&2
fi

%preun
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/%{name} ]; then
                /etc/rc.d/init.d/%{name} stop
        fi
        /sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc COPYING README* Changes
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/%{name}
%dir %{_var}/lib/%{name}

%if %{with up}
%files -n kernel-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slamr.*o*

%files -n kernel-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slusb.*o*
%endif

%if %{with smp}
%files -n kernel-smp-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slamr.*o*

%files -n kernel-smp-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slusb.*o*
%endif
