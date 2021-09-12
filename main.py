from xml import dom
import xml.dom.minidom;
doc = xml.dom.minidom.Document()

view_width = "android:layout_width"
view_height = "android:layout_height"
view_wrap = "wrap_content"
view_match = "match_parent" 
#创建根节点
def create_root():
    root = doc.createElement("LinearLayout")
    root.setAttribute('android:layout_width', 'match_parent')
    root.setAttribute('android:layout_height', 'match_parent')
    root.setAttribute('android:orientation', 'vertical')
    return root
def read_iyu():
    
    pass
#用于测试
def test_iyu():
    iyu = xml.dom.minidom.parse("mian.iyu")
    root = iyu.documentElement
    view = root.getElementsByTagName("View")
    #todo
    for i in view:
        #dosomethind
        pass
    dom_view_type = view[0].getAttribute("type")
    ppt = view[0].getElementsByTagName("ppt")
    #print(view_type)
    split_data = ppt[0].firstChild.data.split("\n")
    #应该换成更好的查找方式
    dom_view_width = split_data[0].split("width=")[1]
    dom_view_height = split_data[1].split("height=")[1]
    dom_view_text = split_data[2].split("text=")[1]
    print("分词",split_data)
    dom_array = []
    each_dom = {}
    each_dom["text"] = dom_view_text
    dom_array.append(each_dom)
    print("结果",dom_array)
    return dom_array
#在这里转换为xml
def write_xml(root,dom_array):
    #print(dom_array[0])
    for i in dom_array:
        View = doc.createElement("TextView")
        View.setAttribute("text",i["text"])
        root.appendChild(View)
        print(i)
    pass
def write_file():
    f = open("layout.xml","w")
    doc.writexml(f,indent="\t",addindent="\t",newl="\n",encoding="utf-8")
    f.close()
#读取 处理 输出
root=create_root()
doc.appendChild(root)

dom_iyu = test_iyu()
write_xml(root,dom_iyu)
write_file()

