def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# domain_name("http://google.com.pl")
# domain_name("www.google.com.pl")
domain_name("http://github.com/carbonfive/raygun")
