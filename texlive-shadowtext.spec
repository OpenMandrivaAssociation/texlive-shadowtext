# revision 26522
# category Package
# catalog-ctan /macros/latex/contrib/shadowtext
# catalog-date 2012-05-18 19:11:54 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-shadowtext
Version:	0.3
Release:	11
Summary:	shadowtext
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/shadowtext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package introduces a command \shadowtext, which adds a drop
shadow to the text that is given as its argument. The colour
and positioning of the shadow are customisable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/shadowtext/shadowtext.sty
%doc %{_texmfdistdir}/doc/latex/shadowtext/README
%doc %{_texmfdistdir}/doc/latex/shadowtext/shadowtext.pdf
%doc %{_texmfdistdir}/doc/latex/shadowtext/shadowtext.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 813752
- Update to latest release.
- Import texlive-shadowtext
- Import texlive-shadowtext

