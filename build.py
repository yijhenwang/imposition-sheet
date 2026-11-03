# 把起始資料塞進網頁，產生可以直接打開的 index.html
# 公開版只放「空白書冊」和一份虛構範例，實際書籍資料用匯入的方式載入
import json, pathlib

root = pathlib.Path(__file__).parent
load = lambda name: json.dumps(json.loads((root / "data" / name).read_text(encoding="utf-8")), ensure_ascii=False)

html = (root / "src/template.html").read_text(encoding="utf-8")
html = html.replace("/*__DATA__*/null", load("空白書冊.imposition.json"))
html = html.replace("/*__SAMPLE__*/null", load("範例_家常料理.imposition.json"))
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html built", len(html) // 1024, "KB")
