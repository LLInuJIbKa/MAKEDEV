Summary:	Script to make and update /dev entries
Summary(de):	Script zum Erstellen und Aktualisieren von /dev-Eintr�gen
Summary(fr):	Script pour cr�er et mettre � jour les entr�es /dev
Summary(pl):	Skrypt do tworzenia i poprawiania urz�dze� z /dev 
Summary(tr):	Ayg�t tan�m� yapmak ve de�i�tirmek i�in bir ara�
Name:		MAKEDEV
Version:	2.6
Release:	1
Copyright:	none
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/dev

%description
The /dev tree holds special files, each of which corresponds to a type
of hardware device that Linux supports. This package contains a script
which makes it easier to create and maintain the files which fill the
/dev tree.

%description -l de
Die /dev-Hierarchie enth�lt spezielle Dateien, von denen jede einem
Hardwareger�ttyp entspricht, der von Linux unterst�tzt wird. Dieses
Paket enth�lt ein Skript, das die Erstellung und die Pflege der
Dateien innerhalb dieser Hierarchie vereinfacht.

%description -l fr
L'arborescence /dev contient des fichiers sp�ciaux. Chacun d'eux
correspond � un p�riph�rique mat�riel g�rable par Linux. Ce paquetage
contient un script facilitant la cr�ation et la maintenance des
fichiers qui remplissent l'arborescence /dev.

%description -l pl
Pliki specjalne znajduj�ce si� w katalogu /dev odpowiadaj�
urz�dzeniom, kt�re s� obs�ugiwane przez Linuxa. Pakiet ten zawiera
skrypt, kt�ry uczyni tworzenie i operowanie tymi plikami �atwiejszym.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak �zere), makinaya
ba�l� ayg�tlar� g�stermek i�in �zel dosyalar kullan�rlar. Bu �zel
dosyalar�n t�m� /dev dizin yap�s� alt�ndad�r. Bu paket en �ok
kullan�lan /dev dosyalar�n� i�erir. Bu dosyalar, bir sistemin d�zg�n
olarak i�leyebilmesi i�in temel gereksinimlerdendir.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

make install \
	ROOT=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/MAKEDEV
%{_mandir}/man8/*
