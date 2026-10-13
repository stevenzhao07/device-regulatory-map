# device-regulatory-map

> **Contributed by [@stevenzhao07](https://github.com/stevenzhao07) · Affiliation: MedXpert (medical-device RA & regulatory consultancy) · Pure technical input, no commercial promotion.**

非软件类医疗器械的跨辖区监管映射：分类规则（NMPA《医疗器械分类规则》+ 分类目录、EU MDR Annex VIII 22 条分类规则、FDA 21 CFR 862–892 专科分类 + 860 程序、PMDA 药机法 Ⅰ–Ⅳ）、注册路径（注册/备案/510(k)/De Novo/PMA/THP）、代表机构要求（MAH/EC REP/US Agent）与典型周期经验值。

这是 MedXpert 把"医疗 AI 信任"方法论工程化落地的可插拔模块之一——把抽象的合规要求变成一条可重复运行的命令或参考实现。方法论四要素（白话版）：**治理守护者 XCGS** ＝ 为 AI 留下可核验的治理证据；**立法者 A³ Laws** ＝ 给自主系统划权限 / 监督 / 追责三条硬边界；**护照官 AI 护照** ＝ 为模型签发可追溯的身份凭证；**人机共存** ＝ 明确人类与 AI 的分工与兜底。

---

## 可插拔模块契约（lgd-skeleton/1.0）

本仓库是一个 **`lgd-skeleton/1.0` 可插拔模块**：

- **一切即插件**：仅依赖声明式 `module.json`，零配置；
- **按需装（lazy）**：仅 triggers 命中时加载；
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由发现；
- **扩展点**：`plugins/`(新增辖区：在 JURISDICTIONS 字典加一项。)。

机器可发现入口：`AGENTS.md` · `CLAUDE.md` · `llms.txt`。

## 特性

- 分类规则索引：EU MDR Annex VIII（22 条）、FDA 21 CFR 862–892、NMPA 分类规则+目录、PMDA Ⅰ–Ⅳ
- 路径对比：注册申报 vs 备案、510(k)/De Novo/PMA、CE 符合性评估路线
- 代表机构：MAH / EC REP / US Agent 职责对照
- 周期经验值显式标注「非法定时限」

**上游投稿目标**：OpenRegulatory/templates

## 内容说明

与 samd-ra-toolkit 互补：本仓管通用器械，samd 仓管 SaMD/AIaMD。分类结论须以官方分类目录/规则原文复核。

## 免责声明

本工具仅提供结构化模板与计算能力，**不构成法规建议、临床建议或产品合规结论**。具体产品的注册、临床评价、灭菌验证、风险分析、软件分级等决策，须由合资格人员依据目标辖区（NMPA / FDA / EU MDR / PMDA）最新法规文本作出；条款与限值以官方发布文本为准。使用本工具产生的一切后果由使用者自行承担。

## 使用

```bash
python scripts/device_reg_map.py --demo
python scripts/device_reg_map.py --jurisdiction EU
```

## 快速开始（30 秒）

```bash
git clone https://github.com/stevenzhao07/device-regulatory-map.git && cd device-regulatory-map
python scripts/device_reg_map.py --demo
```

> 想参与或遇到问题？[提 Issue](https://github.com/stevenzhao07/device-regulatory-map/issues) · 完整《AI 参与指南》见 [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)。

## 路由（总入口）

本模块由 **[medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)** 作为 `lgd-skeleton/1.0` 总入口自动路由发现。

## 关联模块

- [samd-ra-toolkit](https://github.com/stevenzhao07/samd-ra-toolkit)
- [udi-assignment](https://github.com/stevenzhao07/udi-assignment)
- [clinical-evaluation](https://github.com/stevenzhao07/clinical-evaluation)

## 许可

CC-BY-4.0 — 见 [LICENSE](./LICENSE)。

## 关联（方法论来源）

- 理念溯源：个人专家关于医疗 AI 信任与治理的公开方法论（个人观点，不构成标准）
- 同账号系列：见 `medical-ai-toolkit` 导航
