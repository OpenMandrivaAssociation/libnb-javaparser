%define section		free

Name:		libnb-javaparser
Version:	6.5
Release:	%mkrel 2
Epoch:		0
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            http://java.netbeans.org/javaparser/
Group:          Development/Java
Source0:        http://java.netbeans.org/files/documents/25/2367/nb-javaparser-6.5-src.zip
BuildRequires:	java-rpmbuild >= 1.6
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java >= 1.6.0
Requires:       java >= 1.6.0
Provides:	netbeans-javaparser = %{version}
BuildArch:      noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Java parser to analyse Java source files inside of the NetBeans IDE

%prep
%{__rm} -fr %{buildroot}
%{__rm} -fr nb-javaparser-6.5
%setup -n nb-javaparser-6.5
# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
ant -f make/netbeans/nb-javac/build.xml jar

%install
%{__rm} -fr %{buildroot}

# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 make/netbeans/nb-javac/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%{__ln_s} %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%{__install} -m 644 make/netbeans/nb-javac/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl-%{version}.jar
%{__ln_s} %{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/*

