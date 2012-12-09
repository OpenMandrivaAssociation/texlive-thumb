# revision 16549
# category Package
# catalog-ctan /macros/latex/contrib/thumb
# catalog-date 2006-12-11 00:37:24 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-thumb
Version:	1.0
Release:	2
Summary:	Thumb marks in documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thumb
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumb.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756838
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719735
- texlive-thumb
- texlive-thumb
- texlive-thumb

