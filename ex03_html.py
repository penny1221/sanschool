from bs4 import BeautifulSoup


html_doc = """
<html><head><title>Hello World</title></head>
<body><h2>Test Header</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>
"""

soup = BeautifulSoup(html_doc,'html.parser');

print(soup.prettify());
print();

title = soup.title;
print(title);
print(title.string);
print(title.text);
print();

h2 = soup.find('h2');
print(h2);
print(h2.text);
print();

h2s = soup.find_all('h2');
print(h2s);
print(h2s[0].text);
print();

link = soup.find_all('a');

for item in link:
    url = item.get('href');
    name = item.text;
    print(name);
    print(url);
    print();
    
link2 = soup.find(id = "link2");
print(link2.get('href'));
print(link2.text);
print();

    