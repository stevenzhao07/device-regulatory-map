# AGENTS.md · device-regulatory-map

> 机器可发现入口（AI 编码代理 / Codex / Claude / Cursor）。单一事实源：本文件。

## 这是什么
非软件类医疗器械的跨辖区监管映射：分类规则（NMPA《医疗器械分类规则》+ 分类目录、EU MDR Annex VIII 22 条分类规则、FDA 21 CFR 862–892 专科分类 + 860 程序、PMDA 药机法 Ⅰ–Ⅳ）、注册路径（注册/备案/510(k)/De Novo/PMA/THP）、代表机构要求（MAH/EC REP/US Agent）与典型周期经验值。

## 运行
```bash
python scripts/device_reg_map.py --demo
python scripts/device_reg_map.py --help
```

## 扩展契约（lgd-skeleton/1.0）
- **一切即插件**：仅依赖声明式 `module.json`，零配置。
- **按需装（lazy）**：仅 triggers 命中时加载。
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由。
- **扩展点**：`plugins/`(新增辖区：在 JURISDICTIONS 字典加一项。)

## 红线
纯技术贡献，不含商业营销；MedXpert 仅作为贡献者署名（@stevenzhao07）。
