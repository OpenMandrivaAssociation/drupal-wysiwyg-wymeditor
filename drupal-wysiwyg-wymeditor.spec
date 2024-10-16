%define oname	wymeditor
%define pre_rc	2
%define rel	1

Name:		drupal-wysiwyg-%{oname}
Summary:	WYMeditor for Drupal Wysiwyg module
Version:	0.5
Release:	%{?pre_rc:0.rc%{pre_rc}.}%{rel}
License:	GPLv2 or MIT
Group:		Networking/WWW
URL:		https://www.wymeditor.org/
Source0:	%{oname}-%{version}%{?pre_rc:-rc-%{pre_rc}}.tar.gz
Requires:	drupal-wysiwyg
Provides:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
WYMeditor is a web-based WYSIWYM (What You See Is What You Mean) XHTML editor 
(not WYSIWYG).

WYMeditor's main concept is to leave details of the document's visual layout,
and to concentrate on its structure and meaning, while trying to give the user
as much comfort as possible (at least as WYSIWYG editors).

WYMeditor has been created to generate perfectly structured XHTML strict code,
to conform to the W3C XHTML specifications and to facilitate further processing
by modern applications.

With WYMeditor, the code can't be contaminated by visual informations like font
styles and weights, borders, colors, ...

%prep
%setup -q -n %{oname}

%build

%install
%__install -d %{buildroot}%{_var}/www/drupal//sites/all/libraries/
cp -a . %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}
rm %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}/{*.txt,README}

%files
%{_var}/www/drupal//sites/all/libraries/%{oname}
%doc README


%changelog
* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.5-0.rc2.1
+ Revision: 798354
- imported package drupal-wysiwyg-wymeditor
- imported package drupal-wysiwyg-wymeditor

