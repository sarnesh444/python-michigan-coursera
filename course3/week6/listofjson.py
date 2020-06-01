import json
data='''
[
{"menu": {
  "id": "file1",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}},
{"menu": {
  "id": "file2",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
]
'''
print(type(data))
#since data has [] so json.loads gives list as output
content=json.loads(data)
print(type(content))
print(len(content))
for l in content:
    print(l["menu"]["id"])
