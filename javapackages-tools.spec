Name     : javapackages-tools
Version  : 4.7.0
Release  : 9
URL      : https://fedorahosted.org/released/javapackages/javapackages-4.7.0.tar.xz
Source0  : https://fedorahosted.org/released/javapackages/javapackages-4.7.0.tar.xz
Summary  : Simple Maven project
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0+
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : asciidoc
BuildRequires : xmlto
BuildRequires : six
BuildRequires : util-linux
BuildRequires : libxslt-bin
BuildRequires : docbook-xml
BuildRequires : dia
Requires : javapackages-tools-bin

Patch1: timestamp.patch

%description
Very short description since we have nothing to say.


%package bin
Summary: bin components for the javapackages-tools package.
Group: Binaries

%description bin
bin components for the javapackages-tools package.


%prep
%setup -q -n javapackages-4.7.0
%patch1 -p1

%build
export LANG=C
%configure --pyinterpreter=/usr/bin/python3
./build

%install
rm -rf %{buildroot}
./install

pushd python
  python3 setup.py install -O1 --skip-build --root %{buildroot}
popd
# fixme: this is needed but the scripts don't work
# chmod a+x %{buildroot}/usr/lib/rpm/*

%files bin
%defattr(755,root,root,-)
/usr/bin/abs2rel
/usr/bin/build-classpath
/usr/bin/build-classpath-directory
/usr/bin/build-jar-repository
/usr/bin/check-binary-files
/usr/bin/clean-binary-files
/usr/bin/create-jar-links
/usr/bin/diff-jars
/usr/bin/find-jar
/usr/bin/gradle-local
/usr/bin/jvmjar
/usr/bin/rebuild-jar-repository
/usr/bin/shade-jar
/usr/bin/xmvn-builddep

%files
%defattr(-,root,root,-)
/usr/lib/python3.6/site-packages/javapackages-4.7.0-py3.6.egg-info/PKG-INFO
/usr/lib/python3.6/site-packages/javapackages-4.7.0-py3.6.egg-info/SOURCES.txt
/usr/lib/python3.6/site-packages/javapackages-4.7.0-py3.6.egg-info/dependency_links.txt
/usr/lib/python3.6/site-packages/javapackages-4.7.0-py3.6.egg-info/top_level.txt
/usr/lib/python3.6/site-packages/javapackages/__init__.py
/usr/lib/python3.6/site-packages/javapackages/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/__pycache__/version.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/cache/__init__.py
/usr/lib/python3.6/site-packages/javapackages/cache/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/cache/__pycache__/cache.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/cache/__pycache__/metadata.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/cache/__pycache__/osgi.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/cache/cache.py
/usr/lib/python3.6/site-packages/javapackages/cache/metadata.py
/usr/lib/python3.6/site-packages/javapackages/cache/osgi.py
/usr/lib/python3.6/site-packages/javapackages/common/__init__.py
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/binding.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/config.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/exception.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/manifest.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/mock.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/osgi.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/strutils.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/__pycache__/util.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/common/binding.py
/usr/lib/python3.6/site-packages/javapackages/common/config.py
/usr/lib/python3.6/site-packages/javapackages/common/exception.py
/usr/lib/python3.6/site-packages/javapackages/common/manifest.py
/usr/lib/python3.6/site-packages/javapackages/common/mock.py
/usr/lib/python3.6/site-packages/javapackages/common/osgi.py
/usr/lib/python3.6/site-packages/javapackages/common/strutils.py
/usr/lib/python3.6/site-packages/javapackages/common/util.py
/usr/lib/python3.6/site-packages/javapackages/ivy/__init__.py
/usr/lib/python3.6/site-packages/javapackages/ivy/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/ivy/__pycache__/ivyfile.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/ivy/ivyfile.py
/usr/lib/python3.6/site-packages/javapackages/maven/__init__.py
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/artifact.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/dependency.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/exclusion.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/extension.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/plugin.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/pom.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/__pycache__/pomreader.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/maven/artifact.py
/usr/lib/python3.6/site-packages/javapackages/maven/dependency.py
/usr/lib/python3.6/site-packages/javapackages/maven/exclusion.py
/usr/lib/python3.6/site-packages/javapackages/maven/extension.py
/usr/lib/python3.6/site-packages/javapackages/maven/plugin.py
/usr/lib/python3.6/site-packages/javapackages/maven/pom.py
/usr/lib/python3.6/site-packages/javapackages/maven/pomreader.py
/usr/lib/python3.6/site-packages/javapackages/metadata/__init__.py
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/alias.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/artifact.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/dependency.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/exclusion.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/metadata.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/__pycache__/skippedartifact.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/metadata/alias.py
/usr/lib/python3.6/site-packages/javapackages/metadata/artifact.py
/usr/lib/python3.6/site-packages/javapackages/metadata/dependency.py
/usr/lib/python3.6/site-packages/javapackages/metadata/exclusion.py
/usr/lib/python3.6/site-packages/javapackages/metadata/metadata.py
/usr/lib/python3.6/site-packages/javapackages/metadata/skippedartifact.py
/usr/lib/python3.6/site-packages/javapackages/version.py
/usr/lib/python3.6/site-packages/javapackages/xmvn/__init__.py
/usr/lib/python3.6/site-packages/javapackages/xmvn/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/xmvn/__pycache__/xmvn_config.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/xmvn/__pycache__/xmvn_resolve.cpython-36.pyc
/usr/lib/python3.6/site-packages/javapackages/xmvn/xmvn_config.py
/usr/lib/python3.6/site-packages/javapackages/xmvn/xmvn_resolve.py
/usr/lib/rpm/fileattrs/javadoc.attr
/usr/lib/rpm/fileattrs/maven.attr
/usr/lib/rpm/fileattrs/osgi.attr
/usr/lib/rpm/javadoc.req
/usr/lib/rpm/macros.d/macros.fjava
/usr/lib/rpm/macros.d/macros.jpackage
/usr/lib/rpm/maven.prov
/usr/lib/rpm/maven.req
/usr/lib/rpm/osgi.prov
/usr/lib/rpm/osgi.req
/usr/share/gradle-local/init.gradle
/usr/share/java-utils/abs2rel.sh
/usr/share/java-utils/builddep.py
/usr/share/java-utils/builddep.pyc
/usr/share/java-utils/builddep.pyo
/usr/share/java-utils/java-functions
/usr/share/java-utils/java-wrapper
/usr/share/java-utils/maven_depmap.py
/usr/share/java-utils/maven_depmap.pyc
/usr/share/java-utils/maven_depmap.pyo
/usr/share/java-utils/mvn_alias.py
/usr/share/java-utils/mvn_alias.pyc
/usr/share/java-utils/mvn_alias.pyo
/usr/share/java-utils/mvn_artifact.py
/usr/share/java-utils/mvn_artifact.pyc
/usr/share/java-utils/mvn_artifact.pyo
/usr/share/java-utils/mvn_build.py
/usr/share/java-utils/mvn_build.pyc
/usr/share/java-utils/mvn_build.pyo
/usr/share/java-utils/mvn_compat_version.py
/usr/share/java-utils/mvn_compat_version.pyc
/usr/share/java-utils/mvn_compat_version.pyo
/usr/share/java-utils/mvn_config.py
/usr/share/java-utils/mvn_config.pyc
/usr/share/java-utils/mvn_config.pyo
/usr/share/java-utils/mvn_file.py
/usr/share/java-utils/mvn_file.pyc
/usr/share/java-utils/mvn_file.pyo
/usr/share/java-utils/mvn_package.py
/usr/share/java-utils/mvn_package.pyc
/usr/share/java-utils/mvn_package.pyo
/usr/share/java-utils/pom_editor.py
/usr/share/java-utils/pom_editor.pyc
/usr/share/java-utils/pom_editor.pyo
/usr/share/java-utils/request-artifact.py
/usr/share/java-utils/request-artifact.pyc
/usr/share/java-utils/request-artifact.pyo
/usr/share/man/man1/abs2rel.1
/usr/share/man/man1/build-classpath.1
/usr/share/man/man1/build-jar-repository.1
/usr/share/man/man1/diff-jars.1
/usr/share/man/man1/find-jar.1
/usr/share/man/man1/rebuild-jar-repository.1
/usr/share/man/man1/shade-jar.1
/usr/share/man/man7/gradle_build.7
/usr/share/man/man7/mvn_alias.7
/usr/share/man/man7/mvn_artifact.7
/usr/share/man/man7/mvn_build.7
/usr/share/man/man7/mvn_compat_version.7
/usr/share/man/man7/mvn_config.7
/usr/share/man/man7/mvn_file.7
/usr/share/man/man7/mvn_install.7
/usr/share/man/man7/mvn_package.7
/usr/share/man/man7/pom_add_dep.7
/usr/share/man/man7/pom_add_parent.7
/usr/share/man/man7/pom_add_plugin.7
/usr/share/man/man7/pom_change_dep.7
/usr/share/man/man7/pom_disable_module.7
/usr/share/man/man7/pom_remove_dep.7
/usr/share/man/man7/pom_remove_parent.7
/usr/share/man/man7/pom_remove_plugin.7
/usr/share/man/man7/pom_set_parent.7
/usr/share/man/man7/pom_xpath_disable.7
/usr/share/man/man7/pom_xpath_inject.7
/usr/share/man/man7/pom_xpath_remove.7
/usr/share/man/man7/pom_xpath_replace.7
/usr/share/man/man7/pom_xpath_set.7
/usr/share/maven-metadata/javapackages-metadata.xml
/usr/share/xmvn/configuration.xml
