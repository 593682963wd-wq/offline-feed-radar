"""作者：Wangyuan；日期：2026-10-29；职责：解析调用方提供的RSS/Atom文本，筛选并生成阅读摘要。"""
from defusedxml import ElementTree as ET
from defusedxml.common import DefusedXmlException
from textutils import stable_id,strip_tags

def run(payload):
    if not isinstance(payload,dict):raise TypeError('输入须对象')
    xml=payload.get('xml','')
    if not isinstance(xml,str):raise TypeError('xml须文本')
    if not xml.strip():return {'items':[],'digest':''}
    try:root=ET.fromstring(xml)
    except (ET.ParseError,DefusedXmlException) as error:raise ValueError("XML内容无效或不安全") from error
    items=[];seen=set();query=str(payload.get('query','')).lower();keywords=payload.get('keywords',[])
    for item in root.iter():
        if item.tag.split('}')[-1] not in {'item','entry'}:continue
        fields={}
        for child in item:
            key=child.tag.split('}')[-1]
            if key=='link' and child.attrib.get('href'):
                relation=child.attrib.get('rel','alternate')
                if relation=='alternate' or ('link' not in fields and relation!='self'):fields[key]=child.attrib['href']
            else:fields[key]=''.join(child.itertext())
        title=strip_tags(fields.get('title',''));description=strip_tags(fields.get('description',fields.get('summary',fields.get('content',''))));link=fields.get('link','')
        ident=stable_id(fields.get('guid',fields.get('id',link or title)))
        if ident in seen or query and query not in (title+' '+description).lower():continue
        seen.add(ident);score=sum(1 for word in keywords if str(word).lower() in (title+' '+description).lower())
        items.append({'id':ident,'title':title,'summary':description,'url':link,'matches':score,'published':fields.get('pubDate',fields.get('published',''))})
    items.sort(key=lambda item:-item['matches'])
    return {'items':items,'digest':'\n'.join(f"- {row['title']}: {row['summary']}" for row in items)}
