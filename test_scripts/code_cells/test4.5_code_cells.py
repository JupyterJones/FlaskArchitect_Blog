print("hello")

from IPython.display import HTML
HTML("""
<script>
console.log("hello");
</script>
<b>HTML</b>
""")

%%javascript
console.log("hi");

from IPython.display import Image
Image("http://ipython.org/_static/IPy_header.png")

