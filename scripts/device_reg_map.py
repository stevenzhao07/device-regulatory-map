#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
device_reg_map.py — 通用器械跨辖区监管映射
============================================
分类规则索引 + 注册路径对比 + 代表机构职责。与 samd-ra-toolkit 互补：
本仓管通用器械（含植入物），samd 仓管 SaMD/AIaMD。

诚实边界：分类结论须以官方分类目录/规则原文复核；周期为经验值。
"""
from __future__ import annotations
import argparse
import sys

JURISDICTIONS = {
    "CN": {
        "region": "中国",
        "authority": "NMPA（国家药监局）",
        "classification": "《医疗器械分类规则》（国家食品药品监督管理总局令第15号，2015-07-14 公布，2016-01-01 施行）+《医疗器械分类目录》→ 第一类（备案）/ 第二、三类（注册）",
        "pathway": "第二类：省级药监注册；第三类：NMPA 注册；第一类：备案",
        "rep": "MAH（上市许可持有人）— 注册人可为境外主体，须指定境内代理人",
        "timeline": "III 类审评经验值约 12–24 月（非法定时限）",
    },
    "EU": {
        "region": "欧盟",
        "authority": "公告机构 (Notified Body) + 主管机关；协调靠 MDCG",
        "classification": "MDR Annex VIII 22 条分类规则 → Class I / IIa / IIb / III（含 Is/Im/Ir 特殊子类）",
        "pathway": "Class I 自我声明 + DoC；IIa/IIb/III 需 NB 符合性评估（Annex IX-XI）",
        "rep": "EC REP（欧盟授权代表）+ PRRC（法规合规负责人）",
        "timeline": "NB 介入审评经验值约 9–18 月（非法定时限）",
    },
    "FDA": {
        "region": "美国",
        "authority": "FDA (CDRH)",
        "classification": "FD&C Act §513 + 21 CFR 860（分类程序）+ 各专科规定（骨科植入物 21 CFR 888）→ Class I/II/III",
        "pathway": "510(k)（实质等效）/ De Novo（新低风险）/ PMA（高风险）",
        "rep": "US Agent（美国代理人）；Establishment Registration + Device Listing",
        "timeline": "510(k) 经验值 3–12 月；PMA 更长（非法定时限）",
    },
    "PMDA": {
        "region": "日本",
        "authority": "PMDA / MHLW（厚生劳动省）",
        "classification": "薬機法 分类 → 一般医療機器（Ⅰ）/ 管理医療機器（Ⅱ–Ⅳ，Ⅳ 最严）",
        "pathway": "承認申請（Ⅱ–Ⅳ）／届出（Ⅰ）；外国制造须指定 MAH（国内管理人）",
        "rep": "MAH（国内管理人）+ 外国制造业者登录",
        "timeline": "审查经验值 9–18 月（非法定时限）",
    },
}

CLASS_GUIDE = [
    ("CN", "I", "第一类：风险低，备案管理", "常规操作足够安全"),
    ("CN", "II", "第二类：中度风险，省级注册", "需设计控制+临床评价（多数可免临床）"),
    ("CN", "III", "第三类：较高风险，NMPA 注册", "植入/生命支持等；需临床评价"),
    ("EU", "I", "Class I：自我声明（Is/Im/Ir 除外）", "灭菌/可重复使用等有附加要求"),
    ("EU", "IIa", "Class IIa：NB 介入", "中低风险（多数非植入）"),
    ("EU", "IIb", "Class IIb：NB 介入", "中高风险（含多数植入）"),
    ("EU", "III", "Class III：NB + 更严审评", "可吸收植入/长期植入心脏等"),
    ("FDA", "I", "Class I：一般控制（多数豁免 GMP 部分条款）", "510(k) 多数豁免"),
    ("FDA", "II", "Class II：一般+特殊控制", "510(k) 为主；特殊控制可豁免"),
    ("FDA", "III", "Class III：PMA", "生命支持/植入高风险"),
    ("PMDA", "Ⅰ", "一般医療機器：届出", "低风险"),
    ("PMDA", "Ⅱ", "管理医療機器：承認", "中风险"),
    ("PMDA", "Ⅲ", "管理医療機器：承認", "高风险"),
    ("PMDA", "Ⅳ", "管理医療機器：承認（最严）", "高度侵入/高风险"),
]


def _demo() -> int:
    print("通用器械跨辖区监管映射 · 演示\n")
    for j, d in JURISDICTIONS.items():
        print(f"### {j}（{d['region']}）")
        for k in ("authority", "classification", "pathway", "rep", "timeline"):
            print(f"  - {k}: {d[k]}")
        print()
    print("### 分类速查（部分）")
    for j, c, name, note in CLASS_GUIDE[:6]:
        print(f"  {j} {c}: {name} — {note}")
    print("\n[demo] 分类结论以官方分类目录/规则原文复核；周期为经验值非法定时限。")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="通用器械跨辖区监管映射")
    ap.add_argument("--demo", action="store_true", help="跑内置演示")
    ap.add_argument("--jurisdiction", help="CN/EU/FDA/PMDA/ALL")
    args = ap.parse_args()
    if args.demo:
        return _demo()
    if args.jurisdiction:
        js = JURISDICTIONS.keys() if args.jurisdiction.upper() == "ALL" else [args.jurisdiction.upper()]
        for j in js:
            if j not in JURISDICTIONS:
                print(f"[err] 未知辖区: {j}")
                return 2
            d = JURISDICTIONS[j]
            print(f"### {j}（{d['region']}）")
            for k in ("authority", "classification", "pathway", "rep", "timeline"):
                print(f"  - {k}: {d[k]}")
            print()
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
