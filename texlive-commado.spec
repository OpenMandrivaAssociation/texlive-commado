%global tl_name commado
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	r0.11a
Release:	%{tl_revision}.1
Summary:	Expandable iteration on comma-separated and filename lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/commado
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides two packages: commado and filesdo. The package
commado provides the command \DoWithCSL: \DoWithCSL{<cmd>}{<list>}
applies an existing one-parameter macro <cmd> to each item in a list
<list> in which terms are separated by commas. The package filesdo
provides the command \DoWithBasesExts:
\DoWithBasesExts{<cmd>}{<bases>}{<exts>} which runs the single parameter
command <cmd> on each file whose base and extension are respectively
from the comma-separated lists <bases> and <exts>. These 'loop'-like
commands are (themselves) entirely expandable. The packages rely on
packages plainpkg, and stacklet

