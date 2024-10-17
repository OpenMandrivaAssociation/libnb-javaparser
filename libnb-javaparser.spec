# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           libnb-javaparser
Version:        6.8
Release:        3
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            https://java.netbeans.org/javaparser/
Group:          Development/Java
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# hg clone http://hg.netbeans.org/main/nb-javac/
# cd nb-javac/
# hg update -r 1c46268162cd
# tar -czvf ../nb-javac-6.8.tar.gz *
Source0:        nb-javac-%{version}.tar.gz

BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  java-rpmbuild >= 1.5

Requires:       java >= 1.6.0
Requires:       jpackage-utils
Provides:       netbeans-javaparser

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Java parser to analyse Java source files inside of the NetBeans IDE

%prep
%setup -q -c
# remove all binary libs
find . -name "*.jar" -exec %__rm -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
%ant -f make/netbeans/nb-javac/build.xml jar

%install
%__rm -fr %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}
%__install -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%__ln_s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%__install -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl-%{version}.jar
%__ln_s %{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ASSEMBLY_EXCEPTION LICENSE README
%{_javadir}/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 6.8-2mdv2011.0
+ Revision: 609761
- rebuild

* Sun Apr 11 2010 Jaroslav Tulach <jtulach@mandriva.org> 6.8-1mdv2010.1
+ Revision: 533601
- Upgrading to NetBeans version 6.8

* Fri Sep 25 2009 Jaroslav Tulach <jtulach@mandriva.org> 6.7.1-1mdv2010.0
+ Revision: 448791
- Update to NetBeans 6.7.1 javaparser

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0:6.5-3mdv2010.0
+ Revision: 438715
- rebuild

* Sat Jan 17 2009 Jaroslav Tulach <jtulach@mandriva.org> 0:6.5-2mdv2009.1
+ Revision: 330444
+ rebuild (emptylog)

* Mon Jan 05 2009 Jaroslav Tulach <jtulach@mandriva.org> 0:6.5-1mdv2009.1
+ Revision: 324960
- Updating to version 6.5

* Wed Aug 13 2008 Jaroslav Tulach <jtulach@mandriva.org> 0:6.1-1mdv2009.0
+ Revision: 271348
- Updating the parser to 6.1 version

* Sat Jul 26 2008 Thierry Vignaud <tv@mandriva.org> 0:6.0-5mdv2009.0
+ Revision: 250291
- rebuild

* Wed Jan 23 2008 Jaroslav Tulach <jtulach@mandriva.org> 0:6.0-3mdv2008.1
+ Revision: 157149
- Updated to new upstream source package

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:6.0-2mdv2008.1
+ Revision: 120969
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Tue Dec 11 2007 Jaroslav Tulach <jtulach@mandriva.org> 0:6.0-1mdv2008.1
+ Revision: 117585
- Initial version of the NetBeans javaparser library
- create libnb-javaparser

