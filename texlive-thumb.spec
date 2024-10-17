Name:		texlive-thumb
Version:	16549
Release:	2
Summary:	Thumb marks in documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thumb
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Place thumb marks in books, manuals and reference maunals.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thumb/thumb.sty
%doc %{_texmfdistdir}/doc/latex/thumb/README
%doc %{_texmfdistdir}/doc/latex/thumb/thumb.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thumb/thumb.dtx
%doc %{_texmfdistdir}/source/latex/thumb/thumb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
