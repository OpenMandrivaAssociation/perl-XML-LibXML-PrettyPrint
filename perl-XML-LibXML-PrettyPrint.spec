%define upstream_name    XML-LibXML-PrettyPrint
%define upstream_version 0.006

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.006
Release:    1

Summary:    Add pleasant whitespace to a DOM tree 
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-PrettyPrint-%{version}.tar.gz

BuildRequires: perl(Exporter::Tiny)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.170.0
BuildRequires: perl(Test::More) >= 0.960.0
BuildRequires: perl(Test::Warnings)
BuildRequires: perl(XML::LibXML) >= 1.620.0
BuildArch:  noarch

%description
Long XML files can be daunting for humans to read. Of course, XML is really
designed for computers to read - not people - but there are times when mere
mortals do need to read and edit XML by hand. For example, if your application
stores its configuration in XML, or you need to dump some XML to STDOUT for
debugging purposes.

Syntax highlighting helps, but to really make sense of some XML, proper
indentation can be vital. Hence XML::LibXML::PrettyPrint - it can be applied
to an XML::LibXML DOM tree to reformat it into a more readable result.

Pretty-printing XML is not as CPU-efficient as dumping it out sloppily, so
unless you're pretty sure that a human is going to need to make sense of your
XML, you should probably not use this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%make_install

%files
%doc CONTRIBUTING COPYRIGHT CREDITS Changes INSTALL LICENSE META.json META.yml MYMETA.yml README SIGNATURE
%{_bindir}/xml-pretty
%perl_vendorlib/*
%{_mandir}/man1/xml-pretty.1*
%{_mandir}/man3/*
