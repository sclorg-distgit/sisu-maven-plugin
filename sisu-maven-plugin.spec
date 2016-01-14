%global pkg_name sisu-maven-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global tag d63011e

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1
Release:        8.8%{?dist}
Summary:        Sisu plugin for Apache Maven
BuildArch:      noarch
License:        ASL 2.0 or EPL
URL:            http://sonatype.github.com/%{pkg_name}/
Source:         https://github.com/sonatype/%{pkg_name}/tarball/%{pkg_name}-%{version}#/%{pkg_name}-%{version}.tar.gz

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-common-artifact-filters
BuildRequires:  %{?scl_prefix}plexus-utils
BuildRequires:  %{?scl_prefix}sisu
BuildRequires:  %{?scl_prefix}sonatype-plugins-parent
# test deps
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix}maven-surefire-provider-junit


%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package        javadoc
Summary:        API documentation for %{pkg_name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n sonatype-%{pkg_name}-%{tag}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{pkg_name}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE-ASL.txt LICENSE-EPL.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt


%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.1-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.1-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.1-8.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-8
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon May 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-6
- Fix license tag

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 1.1-3
- Build with xmvn

* Wed Aug  8 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Added parent POM dependency

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Initial packaging
