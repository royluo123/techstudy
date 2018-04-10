import xml.etree.ElementTree as etree

tree = etree.parse('test.xml')
root = tree.getroot()
print(root)
view = root.findall('com.uc.browser.Barcode.client.android.ViewfinderView')
print(view)
print(view[0].attrib)
