import urllib.request
url = "http://comp2152.gblearn.com/2019/winter/a1_ui_tester.php"
tester_file = urllib.request.urlopen(url)
exec(tester_file.read())
