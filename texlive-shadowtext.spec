Name:		texlive-shadowtext
Version:	26522
Release:	2
Summary:	shadowtext
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shadowtext
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
