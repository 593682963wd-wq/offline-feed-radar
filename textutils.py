from __future__ import annotations
import hashlib,re,html
import xml.etree.ElementTree as ET
from typing import Any

def stable_id(text: str) -> str:
    # 展示用slug不能作为去重身份，大小写/标点/截断均可能合并不同条目。
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def strip_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", text).strip()

def first_text(item: ET.Element, names: tuple[str, ...]) -> str:
    for name in names:
        found = item.find(name)
        if found is not None and found.text:
            return found.text.strip()
    return ""

def priority_for(score: int) -> str:
    if score >= 86:
        return "必看"
    if score >= 76:
        return "精选"
    if score >= 64:
        return "候选"
    return "跳过"

def advice_for(score: int) -> str:
    if score >= 86:
        return "进入今日简报，并安排一次工具/案例验证。"
    if score >= 76:
        return "保留到精选池，周复盘时再判断是否深入。"
    if score >= 64:
        return "先收藏为候选，不占用当日注意力。"
    return "热度不能证明价值，默认跳过。"
