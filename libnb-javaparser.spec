%define section		free

Name:		libnb-javaparser
Version:	6.0
Release:	%mkrel 1
Epoch:		0
Summary:        NetBeans Java Parser
License:        GPLv2 with exceptions
Url:            http://java.netbeans.org/
Group:		Development/Java
Source0:        nb-javaparser-6.0.zip
BuildRequires:	jpackage-utils >= 1.6
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  java >= 1.6.0
Requires:       java >= 1.6.0
BuildArch:      noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Java parser to analyse Java source files inside of the NetBeans IDE

%prep
%{__rm} -fr %{buildroot}
%{__rm} -fr nb-javaparser-6.0
%setup -c -n nb-javaparser-6.0
# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
ant -f Jsr199.nb60/build.xml jar -verbose

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 Jsr199.nb60/dist/javac-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%{__ln_s} %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%{__install} -m 644 Jsr199.nb60/dist/javac-impl.jar %{buildroot}%{_javadir}/%{name}-impl-%{version}.jar
%{__ln_s} %{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/*
