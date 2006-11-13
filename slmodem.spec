# NOTE: no SMP drivers for now - I don't know if these binaries would work?
# TODO: test it on SMP and add SMP modules or update above comment
#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
%bcond_without	kernel		# don't build kernel modules
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)

%if !%{with dist_kernel}
%undefine with_smp
%endif

%define _snap	20060727

#
%define	rel	0.%{_snap}.1
Summary:	Smart Link soft modem drivers
Summary(de):	Smart Link Software Modem Treiber
Summary(pl):	Sterowniki do modemów programowych Smart Link
Name:		slmodem
Version:	2.9.11
Release:	%{rel}
License:	BSD almost without source
Group:		Base/Kernel
Source0:	http://linmodems.technion.ac.il/packages/smartlink/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	ef7fa570699e1808eaa997b30b881917
Source1:	%{name}.init
Source2:	%{name}.sysconfig
URL:		http://www.smlink.com/
BuildRequires:	%{kgcc_package}
%{?with_dist_kernel:BuildRequires:	kernel-module-build}
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smart Link soft modem drivers.

%description -l de
Smart Link Software Modem Treiber.

%description -l pl
Sterowniki do modemów programowych Smart Link.

%package -n kernel-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component
Summary(de):	Linux Kernel Treiber für Smart Link AMR/PCI Software Modems
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards.

%description -n kernel-char-slmodem-amr -l de
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für HAMR5600 AMR/CNR/MDC/ACR basierende Modems und
für SmartPCI56, SmartPCI561 PCI basierende Modems.

%description -n kernel-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561.

%package -n kernel-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component
Summary(de):	Linux Kernel Trebier für Smart Link USB Software Modems
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem.

%description -n kernel-char-slmodem-usb -l de
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für SmartUSB56 basierende Modems.

%description -n kernel-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56.

%package -n kernel-smp-char-slmodem-amr
Summary:	Linux kernel driver for Smart Link soft modem AMR/PCI component (SMP)
Summary(de):	Linux Kernel Treiber für Smart Link AMR/PCI Software Modems (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu AMR/PCI modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-amr
Linux kernel drivers for Smart Link soft modem. This package contains
driver for HAMR5600 based AMR/CNR/MDC/ACR modem cards and SmartPCI56,
SmartPCI561 based PCI modem cards. SMP kernels.

%description -n kernel-smp-char-slmodem-amr -l de
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für HAMR5600 AMR/CNR/MDC/ACR basierende Modems und
für SmartPCI56, SmartPCI561 PCI basierende Modems. SMP Kernel Treiber.

%description -n kernel-smp-char-slmodem-amr -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik do opartych na HAMR5600 kart modemowych
AMR/CNR/MDC/ACR oraz kart PCI SmartPCI56 i SmartPCI561. J±dra SMP.

%package -n kernel-smp-char-slmodem-usb
Summary:	Linux kernel driver for Smart Link soft modem USB component (SMP)
Summary(de):	Linux Kernel Trebier für Smart Link USB Software Modems (SMP)
Summary(pl):	Sterownik j±dra Linuksa dla elementu USB modemów programowych Smart Link (SMP)
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-char-slmodem-usb
Linux kernel drivers for Smart Link soft modem. This package contains
driver for SmartUSB56 based USB modem. SMP kernels.

%description -n kernel-smp-char-slmodem-usb -l de
Linux Kernel Treiber für Smart Link Software Modems. Dieses Packet
enthält Treiber für SmartUSB56 basierende Modems. SMP Kernel Treiber.

%description -n kernel-smp-char-slmodem-usb -l pl
Sterowniki j±dra Linuksa dla modemów programowych Smart Link. Ten
pakiet zawiera sterownik dla modemów USB opartych na SmartUSB56. J±dra
SMP.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
cd drivers
cp amrlibs.o ..

%if %{with kernel}
# kernel module(s)
for cfg in %{?with_dist_kernel:%{?with_smp:smp} up}%{!?with_dist_kernel:nondist}; do
	if [ ! -r "%{_kernelsrcdir}/config-$cfg" ]; then
		exit 1
	fi
	install -d o/include/linux
	ln -sf %{_kernelsrcdir}/config-$cfg o/.config
	ln -sf %{_kernelsrcdir}/Module.symvers-$cfg o/Module.symvers
	ln -sf %{_kernelsrcdir}/include/linux/autoconf-$cfg.h o/include/linux/autoconf.h
	%{__make} -j1 -C %{_kernelsrcdir} O=$PWD/o prepare scripts
	%{__make} -C %{_kernelsrcdir} clean \
		RCS_FIND_IGNORE="-name '*.ko' -o" \
		M=$PWD O=$PWD/o \
		%{?with_verbose:V=1}
cp ../amrlibs.o .
	%{__make} -C %{_kernelsrcdir} modules \
%if "%{_target_base_arch}" != "%{_arch}"
		ARCH=%{_target_base_arch} \
		CROSS_COMPILE=%{_target_base_cpu}-pld-linux- \
%endif
		HOSTCC="%{__cc}" \
		CPP="%{__cpp}" \
		M=$PWD O=$PWD/o \
		%{?with_verbose:V=1}
	mv slamr{,-$cfg}.ko
	mv slusb{,-$cfg}.ko

done
%endif

%if %{with userspace}
%{__make} -C ../modem \
	CC="%{__cc}"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -d $RPM_BUILD_ROOT{%{_sbindir},/lib/modules/%{_kernel_ver}{,smp}/misc,%{_var}/lib/%{name}}

%if %{with userspace}
install modem/slmodemd	 $RPM_BUILD_ROOT%{_sbindir}
install modem/modem_test $RPM_BUILD_ROOT%{_sbindir}/slmodem-test
install %{SOURCE1}	 $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2}	 $RPM_BUILD_ROOT/etc/sysconfig/%{name}
%endif

%if %{with kernel}
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc
install drivers/slamr-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
		$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/slamr.ko
install drivers/slusb-%{?with_dist_kernel:up}%{!?with_dist_kernel:nondist}.ko \
		$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/slusb.ko
%if %{with smp} && %{with dist_kernel}
install drivers/slamr-smp.ko \
		$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/slamr.ko
install drivers/slusb-smp.ko \
		$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/slusb.ko
%endif
%endif

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
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service %{name} stop
	/sbin/chkconfig --del %{name}
fi

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc COPYING README* Changes
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%dir %{_var}/lib/%{name}
%endif

%if %{with kernel}
%files -n kernel-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slamr.*o*

%files -n kernel-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/slusb.*o*

%if %{with smp}
%files -n kernel-smp-char-slmodem-amr
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slamr.*o*

%files -n kernel-smp-char-slmodem-usb
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/slusb.*o*
%endif
%endif
