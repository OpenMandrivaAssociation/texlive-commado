# revision 28419
# category Package
# catalog-ctan /macros/generic/commado
# catalog-date 2012-12-02 13:05:20 +0100
# catalog-license lppl1.3
# catalog-version 0.11
Name:		texlive-commado
Version:	0.11
Release:	5
Summary:	Expandable iteration on comma-separated and filename lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/commado
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/commado.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides two packages: commado and filesdo. The
package commado provides the command \DoWithCSL:
\DoWithCSL{cmd}{list} applies an existing one-parameter macro
cmd to each item in a list list in which terms are separated by
commas. The package filesdo provides the command
\DoWithBasesExts: \DoWithBasesExts{cmd}{bases}{exts} which runs
the single parameter command cmd on each file whose base and
extension are respectively from the comma-separated lists bases
and exts. These 'loop'-like commands are (themselves) entirely
expandable. The packages rely on packages plainpkg, and
stacklet.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/commado/commado.RLS
%{_texmfdistdir}/tex/generic/commado/commado.sty
%{_texmfdistdir}/tex/generic/commado/filesdo.sty
%doc %{_texmfdistdir}/doc/generic/commado/README
%doc %{_texmfdistdir}/doc/generic/commado/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/commado/commado.pdf
#- source
%doc %{_texmfdistdir}/source/generic/commado/commado.tex
%doc %{_texmfdistdir}/source/generic/commado/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
