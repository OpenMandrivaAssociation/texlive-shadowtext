%global tl_name shadowtext
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Produce text with a shadow behind it
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/shadowtext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/shadowtext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package introduces a command \shadowtext, which adds a drop shadow
to the text that is given as its argument. The colour and positioning of
the shadow are customisable.

